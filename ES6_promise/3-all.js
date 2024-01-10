import {uploadPhoto, createUser} from './utils.js'

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
  .then(([uploadPhoto, createUser]) => {
    console.log(`${uploadPhoto.body} ${createUser.firstName} ${createUser.lastName}`);
  })
}
