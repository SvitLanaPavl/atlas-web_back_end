const fs = require('fs');


async function readDatabase(filepath) {
    return new Promise((resolve, reject) => {
        fs.readFile(filepath, 'utf8', (error, data) => {
            if (error) {
                reject(new Error(`Cannot read database: ${error.message}`));
            } else {
                const lines = data.trim().split('\n');
                const database = {};

                lines.forEach(line => {
                    const [firstname, lastname, age, field] = line.split(',');
                    if (!database[field]) {
                        database[field] = [];
                    }
                    database[field].push(firstname);
                });
                resolve(database);
            }
        })
    });
}

module.exports = readDatabase;