const fs = require('fs');


async function readDatabase(filepath) {
    try {
        const data = await fs.readFile(filepath, 'utf8');
        const lines = data.trim().split('\n');
        const database = {};

        lines.forEach(line => {
            const [firstname, lastname, age, field] = line.split(',');
            if (!database[field]) {
                database[field] = [];
            }
            database[field].push(firstname);
        });
        return database;
    } catch (error) {
        throw new Error(`Cannot read database: ${error.message}`)
    }
};

module.exports = readDatabase;