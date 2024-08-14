function smallestAndLargestNodes(root) {
  function searchTree(root) {
    if (!root) return;
    if (root.data === -1) return;
    lowest = Math.min(lowest, root.data);
    highest = Math.max(highest, root.data);
    searchTree(root.left);
    searchTree(root.right);
  }
  
  let lowest = Infinity;
  let highest = -Infinity;
  searchTree(root);
  return [lowest, highest];
}
