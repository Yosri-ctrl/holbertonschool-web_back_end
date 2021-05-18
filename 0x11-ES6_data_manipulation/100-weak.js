export const weakMap = new WeakMap();

export function queryAPI(point) {
  if (weakMap.has(point)) {
    const nQuery = weakMap.get(point);
    if (nQuery >= 5) {
      throw Error('Endpoint load is high');
    }
    weakMap.set(point, weakMap.get(point) + 1);
  } else {
    weakMap.set(point, 1);
  }
}
