const {
  compareRobots,
} = require('./measuringARobot')

const {
  findRoute,  
  goalOrientedRobot,  
  roadGraph,  
} = require('./module/robot')

/*

Can you write a robot that finishes the delivery task faster than goalOrientedRobot? If you observe that robot’s behavior, what obviously stupid things does it do? How could those be improved?

If you solved the previous exercise, you might want to use your compareRobots function to verify whether you improved the robot.

*/

// Your code here

function myRobot({place, parcels}, route) {
  if (route.length == 0) {
    const parcel = parcels.find((parcel) => parcel.place !== place)
    if (parcel) {
      route = findRoute(roadGraph, place, parcel.place);
    } else {
      route = findRoute(roadGraph, place, parcels[0].address);
    }
  }
  return {direction: route[0], memory: route.slice(1)};
}

compareRobots(myRobot, [], goalOrientedRobot, []);
