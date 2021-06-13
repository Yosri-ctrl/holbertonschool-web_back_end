const chai = require('chai');
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', () => {
  it('checks the output', () => {
    chai.expect(calculateNumber('SUM', 1, 3)).to.equal(4);
    chai.expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
    chai.expect(calculateNumber('SUM', 3.7, 1)).to.equal(5);
		chai.expect(calculateNumber('SUBTRACT', 5, 3)).to.equal(2);
    chai.expect(calculateNumber('SUBTRACT', 3.1, 2.5)).to.equal(0);
    chai.expect(calculateNumber('SUBTRACT', 4.5, 2)).to.equal(3);
		chai.expect(calculateNumber('DIVIDE', 0.0, 2)).to.equal(0);
    chai.expect(calculateNumber('DIVIDE', -1, 1)).to.equal(-1);
    chai.expect(calculateNumber('DIVIDE', 1, 0)).to.equal('Error');
  });
});
