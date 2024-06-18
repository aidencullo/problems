/*

  Iterable groups
  Make the Group class from the previous exercise iterable. Refer to the section about the iterator interface earlier in the chapter if you aren’t clear on the exact form of the interface anymore.

  If you used an array to represent the group’s members, don’t just return the iterator created by calling the Symbol.iterator method on the array. That would work, but it defeats the purpose of this exercise.

  It is okay if your iterator behaves strangely when the group is modified during iteration.

*/


class Iterator {
  constructor(index, group){
    this.index = index 
    this.group = group
  }
  next(){
    this.index++
    if (this.index > this.group.lastIndex){
      return {
        done: true,
      }
    }
    return {
      value: this.group.get(this.index - 1),
      done: false,
    }
  }
}

class Group {
  
  constructor(){
    this.content = {};
    this.lastIndex = 0;
  }
  
  add(item){
    this.content[this.lastIndex] = item;
    this.lastIndex++;
  }

  get(index){
    return this.content[index];
  }

  [Symbol.iterator](){
    return new Iterator(0, this)
  }

  static from(iterable) {
    const group = new Group()
    for (let item of iterable) {
      group.add(item);
    }
    return group;
  }
}

// Your code here (and the code from the previous exercise)

for (let value of Group.from(["a", "b", "c"])) {
  console.log(value);
}
// → a
// → b
// → c
