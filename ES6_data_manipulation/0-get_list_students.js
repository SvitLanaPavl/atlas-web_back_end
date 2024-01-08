
function getListStudents() {
  const arrObj = [];
  const obj1 = {};
  obj1.id = 1;
  obj1.firstName = 'Guillaume';
  obj1.location = 'San Francisco';
  arrObj.push(obj1);
  
  const obj2 = {};
  obj2.id = 2;
  obj2.firstName = 'James';
  obj2.location = 'Columbia';
  arrObj.push(obj2);

  const obj3 = {};
  obj3.id = 5;
  obj3.firstName = 'Serena';
  obj3.location = 'San Francisco';
  arrObj.push(obj3);

  return arrObj;
}