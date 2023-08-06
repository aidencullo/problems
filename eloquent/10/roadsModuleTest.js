const {
  VillageState,
  goalOrientedRobot,
  runRobot,
} = require('./module/robot');

runRobot(VillageState.random(), goalOrientedRobot, []);
