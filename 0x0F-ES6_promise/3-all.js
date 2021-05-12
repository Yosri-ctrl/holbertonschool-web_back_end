import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const myPromise = Promise.all([uploadPhoto(), createUser()]);
  myPromise.then((resp) => {
    const { body } = resp[0];
    const { firstName, lastName } = resp[1];
    console.log(`${body} ${firstName} ${lastName}`);
  }).catch(() => console.log('Signup system offline'));
  return myPromise;
}
