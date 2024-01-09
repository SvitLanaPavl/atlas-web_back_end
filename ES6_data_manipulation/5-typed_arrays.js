export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }
  const arrbuffer = new ArrayBuffer(length);
  const int8 = new Int8Array(arrbuffer);
  int8[position] = value;
  return new DataView(arrbuffer);
}
