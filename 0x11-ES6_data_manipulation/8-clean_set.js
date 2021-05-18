export default function cleanSet(set, start) {
  if (!start.length) return '';
  let result = '';
  set.forEach((x) => {
    if (x.startsWith(start)) result += `${x.slice(start.length)}-`;
  });
  return result.slice(0, result.length - 1);
}
