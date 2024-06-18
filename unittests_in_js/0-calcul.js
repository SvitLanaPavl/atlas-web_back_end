function calculateNumber(a, b, roundA = Math.round, roundB = Math.round) {
	return roundA(a) + roundB(b);
}

module.exports = calculateNumber;
