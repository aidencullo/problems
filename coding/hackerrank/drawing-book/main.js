function pageCount(n, p) {
  if (n % 2 === 0) {
    n++;
  }
  return Math.min(
    Math.floor(p/2),
    Math.floor((n-p)/2)
  );
}
