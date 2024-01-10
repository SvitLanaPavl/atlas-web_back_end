export default function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw new Error('Cannot process');
  }
  const newMap = new Map;
  for (const [key, value] of map) {
    value === 1 ? newMap.set(key, 100) : newMap.set(key, value);
    }
    return newMap;
  }
