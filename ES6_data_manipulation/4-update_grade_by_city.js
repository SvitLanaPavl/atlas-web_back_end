export default function updateStudentGradeByCity(list, city, newGrades) {
  const filtStu = list.filter((item) => item.location === city);
  const mapStu = filtStu.map((item) => {
    const newGrade = newGrades.find((grade) => grade.stuId === item.id);
    const grade = newGrade ? newGrade.grade : 'N/A';
    return {
      ...item,
      grade,
    };
    });
  return mapStu;
}
