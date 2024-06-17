const readDatabase = require('../utils');

const filepath = './database.csv';

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const studentData = await readDatabase(filepath);
      let responseMessage = 'This is the list of our students\n';
      const sortedFields = Object.keys(studentData).sort((a, b) => a.localeCompare(b, 'en', { sensitivity: 'base' }));
      sortedFields.forEach((field) => {
        const students = studentData[field];
        responseMessage += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
      });
      responseMessage = responseMessage.trim();
      res.status(200).send(responseMessage);
    } catch (error) {
      console.error(error);
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    try {
      const students = await readDatabase(filepath);
      const majorStu = students[major] || [];
      res.status(200).send(`List: ${majorStu.join(', ')}`);
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }
}

module.exports = StudentsController;
