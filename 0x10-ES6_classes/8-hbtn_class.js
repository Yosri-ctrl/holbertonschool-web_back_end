export default class HolbertonClass {
	constructor(size, location) {
		this._size = size;
		this._location = location;
	}

	[Symbol.toPrimitive](cst) {
		if (cst === 'number') return this._size;
    if (cst === 'string') return this._location;
  }
}