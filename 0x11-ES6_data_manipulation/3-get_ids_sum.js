export default function getStudentIdsSum(array) {
  if (array.constructor !== Array) { return []; }

  return array.reduce((a, c) => a + c.id, 0);
}
