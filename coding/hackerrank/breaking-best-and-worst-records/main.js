function breakingRecords(scores){
  let min = scores[0]
  let max = scores[0]
  let minCount = 0
  let maxCount = 0
  for (const score of scores) {
    if (score < min) {
      min = score
      minCount++
    }
    if (score > max) {
      max = score
      maxCount++
    }
  }
  return [maxCount, minCount]
}
