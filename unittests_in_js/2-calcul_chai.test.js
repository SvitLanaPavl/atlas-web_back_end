const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', () => {
  describe('Addition', function() {
    it('SUM two floats', function() {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
    it('SUM one float', function() {
      expect(calculateNumber('SUM', 1.4, 4)).to.equal(5);
    });
    it('SUM one str argument', function() {
      expect(calculateNumber('SUM', 1.4, 'b')).to.equal(NaN);
    });
    it('SUM two str arguments', function() {
      expect(calculateNumber('SUM', 'a', 'b')).to.equal(NaN);
    });
    it('SUM two floats one negative', function() {
      expect(calculateNumber('SUM', 1.4, -4.5)).to.equal(-3);
    });
    it('SUM two floats two negative negative', function() {
      expect(calculateNumber('SUM', -1.4, -4.5)).to.equal(-5);
    });
  })
  describe('Subtraction', function() {
    it('SUB two floats', function() {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });
    it('SUB one float', function() {
      expect(calculateNumber('SUBTRACT', 1.4, 4)).to.equal(-3);
    });
    it('SUB one str srg', function() {
      expect(calculateNumber('SUBTRACT', 1.4, 'b')).to.equal(NaN);
    });
    it('SUB two str args', function() {
      expect(calculateNumber('SUBTRACT', 'a', 'b')).to.equal(NaN);
    });
    it('SUB one negative', function() {
      expect(calculateNumber('SUBTRACT', -1.4, 4.5)).to.equal(-6);
    });
    it('SUB two negative', function() {
      expect(calculateNumber('SUBTRACT', -1.4, -4.5)).to.equal(3);
    });
  })
  describe('Division', function() {
    it('DIV', function() {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    it('DIV by 0', function() {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    })
    });
  });
});
