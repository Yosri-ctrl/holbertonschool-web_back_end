const sendPaymentRequestToApi = require('./5-payment.js');
const sinon = require('sinon');
const chai = require('chai');
const Utils = require('./utils.js');

describe('sendPaymentRequestToApi', () => {
  let spyConsole;
  beforeEach(() => spyConsole = sinon.spy(console, 'log'));
  afterEach(() => spyConsole.restore());

  it('checks the output 100, 20', () => {
    sendPaymentRequestToApi(100, 20);
    chai.expect(spyConsole.calledOnce).to.be.true;
    chai.expect(spyConsole.calledWith('The total is: 120')).to.be.true;
  });
  it('checks the output 10, 10', () => {
    sendPaymentRequestToApi(10, 10);
    chai.expect(spyConsole.calledOnce).to.be.true;
    chai.expect(spyConsole.calledWith('The total is: 20')).to.be.true;
  });
});