const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', () => {
  it('check result', () => {
    assert.strictEqual(calculateNumber(1, 3), 4);
    assert.strictEqual(calculateNumber(1, 3.7), 5);
    assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    assert.strictEqual(calculateNumber(1.5, 3), 5);
    assert.strictEqual(calculateNumber(-1, 3), 2);
    assert.strictEqual(calculateNumber(1, -3),-2);
    assert.strictEqual(calculateNumber(-1, -3), -4);
    assert.strictEqual(isNaN(calculateNumber(0)), true);
    assert.strictEqual(isNaN(calculateNumber()), true);
  });
});
