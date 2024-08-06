function pageCount(n, p) {
  if (n % 2 === 0) {
    return Math.min(
      Math.floor(p/2),
      Math.floor((n-p+1)/2)
    );
  }
  return Math.min(
    Math.floor(p/2),
    Math.floor((n-p)/2)
  );
}

