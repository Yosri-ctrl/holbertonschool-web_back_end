export default function createInt8TypedArray(length, position, value) {
	const array = new ArrayBuffer(length);
  const data = new DataView(array, 0);
  if (position > length - 1) throw Error('Position outside range');
  data.setInt8(position, value);
  return data;
}
