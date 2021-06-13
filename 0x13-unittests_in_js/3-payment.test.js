const sendPaymentRequestToApi = require('./3-payment.js');
const sinon = require('sinon');
const chai = require('chai');
const Utils = require('./utils.js');

describe('sendPaymentRequestToApi', () => {
  const spyUtils = sinon.spy(Utils, 'calculateNumber');

  it('checks the output', () => {
    sendPaymentRequestToApi(100, 20);
    chai.expect(spyUtils.calledOnce).to.be.true;
    chai.expect(spyUtils.calledWith('SUM', 100, 20)).to.be.true;
    spyUtils.restore()
  });
});