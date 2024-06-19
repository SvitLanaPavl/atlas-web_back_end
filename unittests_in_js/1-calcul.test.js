const assert = require("assert");
const calculateNumber = require("./1-calcul.js");

describe('calculateNumber', () => {
  describe('Addition', function() {
    it('SUM two floats', function() {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    });
    it('SUM one float', function() {
      assert.strictEqual(calculateNumber('SUM', 1.4, 4), 5);
    });
    it('SUM one str argument', function() {
      assert.strictEqual(calculateNumber('SUM', 1.4, 'b'), NaN);
    });
    it('SUM two str arguments', function() {
      assert.strictEqual(calculateNumber('SUM', 'a', 'b'), NaN);
    });
    it('SUM two floats one negative', function() {
      assert.strictEqual(calculateNumber('SUM', 1.4, -4.5), -3);
    });
    it('SUM two floats two negative negative', function() {
      assert.strictEqual(calculateNumber('SUM', -1.4, -4.5), -5);
    });
  })
  describe('Subtraction', function() {
    it('SUB two floats', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
    it('SUB one float', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4), -3);
    });
    it('SUB one str srg', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 'b'), NaN);
    });
    it('SUB two str args', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', 'a', 'b'), NaN);
    });
    it('SUB one negative', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', -1.4, 4.5), -6);
    });
    it('SUB two negative', function() {
      assert.strictEqual(calculateNumber('SUBTRACT', -1.4, -4.5), 3);
    });
  })
  describe('Subtraction', function() {
    it('DIV', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    it('DIV by 0', function() {
      assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    })
    });
  });
});
