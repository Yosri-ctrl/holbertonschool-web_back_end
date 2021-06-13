const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', () => {
  it('checks the output', () => {
    assert.strictEqual(calculateNumber('SUM', 1, 3), 4);
    assert.strictEqual(calculateNumber('SUM', 1, 3.7), 5);
    assert.strictEqual(calculateNumber('SUM', 3.7, 1), 5);
		assert.strictEqual(calculateNumber('SUBTRACT', 5, 3), 2);
    assert.strictEqual(calculateNumber('SUBTRACT', 3.1, 2.5), 0);
    assert.strictEqual(calculateNumber('SUBTRACT', 4.5, 2), 3);
		assert.strictEqual(calculateNumber('DIVIDE', 0.0, 2), 0);
    assert.strictEqual(calculateNumber('DIVIDE', -1, 1), -1);
    assert.strictEqual(calculateNumber('DIVIDE', 1, 0), 'Error');
  });
});
