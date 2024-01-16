export default function appendToEachArrayValue(array, appendString) {
  const array_new = [];
  for (const index of array) {
    array_new.push(appendString + index);
  }

  return array_new;
}
