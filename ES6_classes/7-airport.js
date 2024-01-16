export default class Airport {
  constructor(name, code) {
    if (typeof name !== 'string') {
      throw new TypeError('name must be a string');
    }
    if (typeof code !== 'number') {
      throw new TypeError('code must be a number');
    }
    this._name = name;
    this._code = code;
  }

  toString(){
    return `[object ${this._code}]`;
  }
}
