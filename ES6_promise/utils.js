export default function uploadPhoto() {
  return new Promise(() => {
    return {
      status: 200,
      body: 'photo-profile-1',
    }
  })
}

export function createUser() {
  return new Promise(() => {
    return {
      firstName: 'Guillaume',
      lastName: 'Salva',
    }
  })
}
