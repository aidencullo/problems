/*

A modular robot
These are the bindings that the project from Chapter 7 creates:

roads
buildGraph
roadGraph
VillageState
runRobot
randomPick
randomRobot
mailRoute
routeRobot
findRoute
goalOrientedRobot

If you were to write that project as a modular program, what modules
would you create? Which module would depend on which other module, and
what would their interfaces look like?

village

roads
VillageState
mailRoute
runRobot

robot -> alg

randomRobot
routeRobot
goalOrientedRobot

alg
 
randomPick
findRoute

graph
 
buildGraph
roadGraph

Which pieces are likely to be available prewritten on NPM?

// established algs
buildGraph
findRoute
villageState

Would you
prefer to use an NPM package or write them yourself?

// i would want to test my own specific algs
robots

*/
