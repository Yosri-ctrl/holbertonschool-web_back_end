export default function getStudentsByLocation(array, city) {
  if (array.constructor !== Array) { return []; }
  return array.filter((x) => x.location === city);
}
