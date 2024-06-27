import createPushNotificationsJobs from './8-job';
import kue from 'kue';
import { expect } from 'chai';

const queue = kue.createQueue();

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

  it('creates jobs for each object', () => {
    const jobs = [
      {
        phoneNumber: '5456768777',
        message: 'This is the code 123 to verify your account',
      },
      {
        phoneNumber: '5456768778',
        message: 'This is the code 124 to verify your account',
      }
    ];
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
  })

  it('logs messages when jobs are created, completed, failed or in progress', () => {
    const jobs = [
      {
        phoneNumber: '5456768777',
        message: 'This is the code 123 to verify your account',
      }
    ]
    createPushNotificationsJobs(jobs, queue);
    const job = queue.testMode.jobs[0];
    job.on('enqueue', () => {
      console.log(`Notification job created: ${job.id}`);
    });
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });
    job.on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err}`);
    })
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
    job.save(() => {
      job.progress(50, 100);
      job.complete();
    });
  });
});
