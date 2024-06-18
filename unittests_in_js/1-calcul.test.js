const assert = require("assert");
const calculateNumber = require("./1-calcul.js");

describe('calculateNumber', () => {
  it('SUM', function() {
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
  });
  it('SUB', function() {
    assert.strictEqual(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
  });
  it('DIV', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
  });
  it('DIV by 0', function() {
    assert.strictEqual(calculateNumber('DIVIDE', 1.4, 0), 'Error');
  });
});
