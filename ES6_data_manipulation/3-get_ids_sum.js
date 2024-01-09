export default function getStudentIdsSum(list) {
  return list.reduce((accumulator, item) => {
    return accumulator + item.id;
  }, 0);
}
