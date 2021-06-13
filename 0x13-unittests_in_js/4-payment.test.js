const sendPaymentRequestToApi = require('./4-payment.js');
const sinon = require('sinon');
const chai = require('chai');
const Utils = require('./utils.js');

describe('sendPaymentRequestToApi', () => {
  const spyConsole = sinon.spy(console, 'log');

  it('checks the output', () => {
    const stub = sinon.stub(Utils, 'calculateNumber');
    stub.withArgs('SUM', 100, 20).returns(10);
    sendPaymentRequestToApi(100, 20);
    chai.expect(spyConsole.calledOnce).to.be.true;
    chai.expect(spyConsole.calledWith('The total is: 10')).to.be.true;
    stub.restore()
    spyConsole.restore();
  });
});