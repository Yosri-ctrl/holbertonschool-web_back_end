import kue from 'kue';
const queue = kue.createQueue();

const obj = {
    phoneNumber: '4153518780',
    message: 'This is the code to verify your account',
}

const job = queue.create('push_notification_code', obj);

job.save();
job.on('enqueue', (id, type) => {
    console.log(`Notification job created: ${job.id}`);
}).on('complete', (result) => {
    console.log("Notification job completed");
}).on('failed', (errorMessage) => {
    console.log("Notification job failed");
});
