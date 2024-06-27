import createPushNotificationsJobs from './8-job';
import kue from 'kue';
import { expect } from 'chai';

const queue = kue.createQueue();

const jobs = [
  {
    phoneNumber: '5456768777',
    message: 'This is the code 123 to verify your account',
  }
]

describe('testing createPushNotificationsJobs', () => {
  before(() => {
    queue.testMode.enter();
  });
  afterEach(() => {
    queue.testMode.clear();
  });
  after(() => {
    queue.testMode.exit();
  });
  it('throw error when jobs not an array - object', () => {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });
  it('throw error when jobs not an array - number', () => {
    expect(() => createPushNotificationsJobs(3, queue)).to.throw('Jobs is not an array');
  });
  it('throw error when jobs not an array - string', () => {
    expect(() => createPushNotificationsJobs('Atlas', queue)).to.throw('Jobs is not an array');
  });
});
