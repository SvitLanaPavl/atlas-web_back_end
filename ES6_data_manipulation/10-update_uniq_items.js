export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }
  const newMap = new Map();
  for (const [key, value] of map) {
    if (value === 1) {
      newMap.set(key, 100);
    } else {
      newMap.set(key, value); 
    }
  }
  return newMap;
}
