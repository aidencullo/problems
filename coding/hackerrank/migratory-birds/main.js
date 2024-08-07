function migratoryBirds(arr) {
  const counter = {}
  for (const bird of arr) {
    if (counter[bird]) {
      counter[bird]++
    } else {
      counter[bird] = 1
    }
  }

  const max = Math.max(...Object.values(counter))
  const maxes = arr.filter(bird => counter[bird] === max)
  return Math.min(...maxes)
}


// tests

console.log(migratoryBirds([1, 4, 4, 4, 5, 3])) // 4
