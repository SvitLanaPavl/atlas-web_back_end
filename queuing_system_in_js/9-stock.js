import express, { json } from 'express';
import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
const app = express();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const listProducts = [
  {
    Id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4,
  },
  {
    Id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10,
  },
  {
    Id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2,
  },
  {
    Id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5,
  },
];

function getItemById(id) {
  return listProducts.find(item => item.Id === parseInt(id, 10));
};

async function reserveStockById(itemId, stock) {
  await setAsync(`item.${itemId}`, stock);
};

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : null;
}

app.get('/list_products', (req, res) => {
  const products = listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    itemPrice: product.price,
    itemQuantity: product.stock,
  }));
  res.json(products)
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' })
  };

  const currentQuantity = await getCurrentReservedStockById(itemId);
  const available = currentQuantity !== null ? currentQuantity : product.stock;
  res.json({ itemId: product.id,
    itemName: product.name,
    itemPrice: product.price,
    itemQuantity: available, })
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = req.params.itemId;
  const product = getItemById(itemId);
  if (!product) {
    return res.json({ status: 'Product not found' });
  };

  const currentQuantity = await getCurrentReservedStockById(itemId);
  const available = currentQuantity !== null ? currentQuantity : product.stock;
  if (available < 1) {
    return res.json({ status: 'Not enough stock available', itemId: product.id });
  };
  await reserveStockById(itemId, available - 1);
  res.json({ status: 'Reservation confirmed', itemId: product.id });
});

app.listen(1245, () => {
  console.log('Listening to the port 1245');
});
