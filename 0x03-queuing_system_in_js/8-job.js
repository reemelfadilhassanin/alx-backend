import kue from 'kue';

// Function to create push notification jobs
function createPushNotificationsJobs(jobs, queue) {
  // Check if jobs is an array
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  // Iterate over the jobs and create each job in the queue
  jobs.forEach((jobData) => {
    const job = queue.create('push_notification_code_3', jobData) // Create a new job in the 'push_notification_code_3' queue
      .save((err) => {
        if (err) {
          console.log('Notification job failed:', err);
        } else {
          // Log the job creation
          console.log(`Notification job created: ${job.id}`);
        }
      });

    // Job progress
    job.on('progress', (progress, data) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });

    // Job completion
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // Job failure
    job.on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: ${err.message}`);
    });
  });
}

export default createPushNotificationsJobs;
