const request = require('request');
const chai = require('chai');

describe('app test', () => {
	it('check result', (done) => {
		const call = {
			url: 'http://localhost:7865',
			method: 'GET',
		};
		request(call, (err, res, body) => {
			chai.expect(res.statusCode).to.equal(200);
			chai.expect(body).to.equal('Welcome to the payment system');
			done();
		});
	});
});