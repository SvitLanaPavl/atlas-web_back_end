const sinon = require('sinon');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestAPI', function() {
  afterEach(function() {
    sinon.restore();
  })

	it('calls the CalculateNumber with correct args', () => {
		const calculateNumberSpy = sinon.spy(Utils, 'CalculateNumber');

		sendPaymentRequestToApi(100, 20);
		sinon.assert.calledOnce(calculateNumberSpy);
		sinon.assert.calledOnceWithExactly(calculateNumberSpy, 'SUM', 100, 20);
	});

	it('Displays the console message', () => {
		const consoleMsg = sinon.spy(console, 'log');
	
		sendPaymentRequestToApi(100, 20);
		sinon.assert.calledOnce(consoleMsg);
		sinon.assert.calledOnceWithExactly(consoleMsg, 'The total is: 120');
	});
});
