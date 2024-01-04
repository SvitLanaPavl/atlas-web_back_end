import ClassRoom from '0-classroom.js'

export function initializeRooms() {
  const sizes = [19, 20, 34];
  const rooms = [];
  for (const size of sizes) {
    rooms.push(new ClassRoom(size));
  }
  return rooms;
}
