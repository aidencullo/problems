function decipher(ciphertext, needle) {
  candidates = ciphertext.split(' ').filter(word => word.length === needle.length);
  const newCandidates = candidates.map(candidate => testCandidate(candidate, needle));
  const difference = newCandidates.filter(candidate => candidate !== null)[0];
  if (difference === null) {
    return 'No solution found';
  }
  return incrementLetters(ciphertext, -difference);
}

function testCandidate(candidate, needle) {
  let difference = null;
  for (let index = 0; index < candidate.length; index++) {
    const lastDifference = difference;
    difference = Math.abs(candidate.charCodeAt(index) - needle.charCodeAt(index));
    if (lastDifference && lastDifference !== difference){
      return null;
    }
  }
  return difference;
};

function incrementLetters(str, incrementBy = 1) {
    let incrementedStr = '';
    for (let i = 0; i < str.length; i++) {
        let char = str[i];
        if (char.match(/[a-zA-Z]/)) {
            let charCode = char.charCodeAt(0);
            let baseCode = char >= 'a' ? 97 : 65; // 97 for 'a', 65 for 'A'
          let newCharCode = ((charCode - baseCode + incrementBy) % 26)
	  if (newCharCode < 0) {
	    newCharCode += 26;
	  }
	  newCharCode += baseCode;
          incrementedStr += String.fromCharCode(newCharCode);
        } else {
            incrementedStr += char;
        }
    }
    
    return incrementedStr;
}

const result = decipher('Eqfkpi vguvu ctg hwp!', 'tests');
const result2 = decipher('cdeb nqxg', 'love');
console.log(result2);
console.log(result);
