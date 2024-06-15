const { readDatabase } = require("../utils");


class StudentsController {
    static async getAllStudents(req, res) {
        try {
            const filepath = '../../databse.csv';
            const studentData = await readDatabase(filepath);
            let responseMessage = 'This is the list of our students\n';
            const sortedFields = Object.keys(studentData).sort((a, b) => a.localeCompare(b, 'en', { sensitivity: 'base'}));
            sortedFields.forEach(field => {
                const students = studentData[field];
                responseMessage += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
            });
            res.status(200).send(responseMessage);
        } catch (error) {
            res.status(500).send('CAnnot load the database');
        }
    }
}

module.exports = StudentsController;