const chai = require('chai');
const expect = chai.expect;
const app = require('./api');
const chaiHttp = require('chai-http');

chai.use(chaiHttp);

describe('Index page', () => {
  it('returns status 200', (done) => {
    chai.request(app).get('/')
    .end((err, res) => {
      expect(res).to.have.status(200);
      done();
    });
  });

  it('returns correct result', () => {
    chai.request(app).get('/')
    .end((err, res) => {
      expect(res).to.equal('Welcome to the payment system');
      done();
    });
  });
});
