function buildGraph(connections){
  return connections.reduce((acc, el) => {
    const from = el[0];
    const to = el[1];
    function addEdge(from, to){
      if (!acc[from]) {
        acc[from] = [to];
      } else {
        acc[from].push(to);
      }
    }
    addEdge(to, from);
    addEdge(from, to);
    return acc;
  }, {})
}

module.exports = {
  buildGraph,
}
