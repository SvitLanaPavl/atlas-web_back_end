const fs = require('node:fs');

function countStudents(path) {
    try {
        const data = fs.readFileSync(path, 'utf8');
        const lines = data.trim().split('\n');
        lines.shift();
        const total = lines.length;
        fields = {};
        lines.forEach(line => {
            const [firstname, lastname, age, field] = line.split(',');
            if (!fields[field]) {
                fields[field] = [];
            }
            fields[field].push(firstname)
        });
        console.log(`Number of students: ${total}`);
        for (const [field, students] of Object.entries(fields)) {
            console.log(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}`)
        }
    } catch (err) {
        console.error('Cannot load the database');
        throw err;
    }
    
}

module.exports = countStudents;
