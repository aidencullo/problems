const {
  runRobotRaw,
  goalOrientedRobot,  
  randomRobot,  
  VillageState,  
  findRoute,  
} = require('./module/robot')

/*

Measuring a robot
It’s hard to objectively compare robots by just letting them solve a few scenarios. Maybe one robot just happened to get easier tasks or the kind of tasks that it is good at, whereas the other didn’t.

Write a function compareRobots that takes two robots (and their starting memory). It should generate 100 tasks and let each of the robots solve each of these tasks. When done, it should output the average number of steps each robot took per task.

For the sake of fairness, make sure you give each task to both robots,
rather than generating different tasks per robot.
  
*/

function randomRun(robot1, memory1) {
  // Your code here
  return runRobotRaw(VillageState.random(), robot1, memory1);
}

function compareRobots(robot1, memory1, robot2, memory2) {
  // Your code here
  const result = Array.from({length:100}).reduce((acc, el) => acc +
                                                 randomRun(robot1, memory1) / 100, 0)
  
  const result2 = Array.from({length:100}).reduce((acc, el) => acc +
                                                  randomRun(robot2, memory2) / 100, 0)

  console.log(`robot1: ${result}`)
  console.log(`robot2: ${result2}`)
}

// compareRobots(routeRobot, [], goalOrientedRobot, []);

module.exports = {
  compareRobots,
};

