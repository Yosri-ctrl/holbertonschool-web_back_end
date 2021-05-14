export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  static get [Symbol.species]() {
    return this;
  }

  cloneCar() {
    const Spc = this.constructor[Symbol.species];
    return new Spc(this._brand, this._motor, this._color);
  }
}
