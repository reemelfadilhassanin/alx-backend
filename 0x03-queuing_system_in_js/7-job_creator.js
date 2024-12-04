import kue from 'kue';

// Create the queue for push notifications
const queue = kue.createQueue();

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notification
function sendNotification(phoneNumber, message, job, done) {
  // Track job progress at the beginning (0%)
  job.progress(0, 100);

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job if phone number is blacklisted
    job.failed(new Error(`Phone number ${phoneNumber} is blacklisted`));
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    console.log(`Notification job #${job.id} failed: Phone number ${phoneNumber} is blacklisted`);
  } else {
    // Track job progress to 50% after initial check
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

    // Simulate sending the notification and mark job as completed
    setTimeout(() => {
      job.complete();
      console.log(`Notification job #${job.id} completed`);
      done();
    }, 2000); // Simulate a delay of 2 seconds for sending the notification
  }
}

// Create a queue process that will handle up to 2 jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  // Extract phone number and message from the job data
  const { phoneNumber, message } = job.data;

  // Call the sendNotification function with job data
  sendNotification(phoneNumber, message, job, done);
});
