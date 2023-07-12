// Dominant writing direction
// Write a function that computes the dominant writing direction in a string of text. Remember that each script object has a direction property that can be "ltr" (left to right), "rtl" (right to left), or "ttb" (top to bottom).

// The dominant direction is the direction of a majority of the characters that have a script associated with them. The characterScript and countBy functions defined earlier in the chapter are probably useful here.
require('./aux/scripts.js')

function within(range, char) {
  return range[0] <= char.codePointAt(0) && range[1] >= char.codePointAt(0);
}

function findScript(char) {
  return SCRIPTS.filter((script) => script.ranges.some((range) =>
    within(range, char)))[0];
}

function findMax(acc, el) {
  return el.count > acc.count ? el : acc;
}

function countItems(acc, el) {
  if (acc.some((data) => data.name === el)) {
    const target = acc.filter((data) => data.name === el)[0]
    target.count++;

  } else {
    acc.push({
      name: el,
      count: 1,
    })
  }
  return acc;
}

function dominantDirection(text) {
  // Your code here.
  return text.split('')
        .map((char) => findScript(char))
        .filter((script) => script)
        .map((script) => script.direction)
        .reduce(countItems, [])
        .reduce(findMax).name
}

console.log(dominantDirection("Hello!"));
// → ltr
console.log(dominantDirection("Hey, مساء الخير"));
// → rtl
