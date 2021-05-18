export default function getListStudentIds(array) {
  if (array.constructor !== Array) { return []; }
  return array.map((x) => x.id);
}
