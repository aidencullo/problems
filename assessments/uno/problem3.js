function graphDiameter(graph, numNodes) {
  function dfs(node, dist){
    if (node === numNodes - 1) {
      diameter = Math.min(diameter, dist)
      return
    }
    if (visited.has(node)) {
      return
    }
    visited.add(node)
    for (const neighbor of adjList[node]) {
      dfs(neighbor, dist + 1)
    }
    visited.delete(node)
  }

  let diameter = Infinity
  const visited = new Set()
  const adjList = new Array(numNodes).fill(null).map(() => [])
  for (const [u, v] of graph) {
    adjList[u].push(v)
    adjList[v].push(u)
  }
  dfs(0, 0)
  return diameter
}

// const graph = [ [ 0, 1 ], [ 1, 2 ], [ 2, 3 ] ]
// const result = graphDiameter(graph, 4)
// console.log(result) // 3
