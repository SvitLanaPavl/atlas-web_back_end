export default function returnHowManyArguments(...args) {
  let total = 0;
  for (const arg of args) {
    // eslint-disable-next-line no-unused-vars
    const _ = arg;
    total += 1;
  }
  return total;
}
