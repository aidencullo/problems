/*
  
The standard JavaScript environment provides another data structure called Set. Like an instance of Map, a set holds a collection of values. Unlike Map, it does not associate other values with those—it just tracks which values are part of the set. A value can be part of a set only once—adding it again doesn’t have any effect.

Write a class called Group (since Set is already taken). Like Set, it has add, delete, and has methods. Its constructor creates an empty group, add adds a value to the group (but only if it isn’t already a member), delete removes its argument from the group (if it was a member), and has returns a Boolean value indicating whether its argument is a member of the group.

Use the === operator, or something equivalent such as indexOf, to determine whether two values are the same.

Give the class a static from method that takes an iterable object as argument and creates a group that contains all the values produced by iterating over it.

*/

class Group {
  // Your code here.
  constructor(){
    this.content = [];
  }

  has(item){
    return this.content?.indexOf(item) !== -1;
  }

  add(item){
    if (!this.has(item)) {
      this.content?.push(item)
    }
  }  

  delete(item){
    const index = this.content?.indexOf(item)
    if (index === -1) {
      return false;
    }
    this.content?.splice(index, 1)
    return true;
  }
  
  static from(iterable){
    const newGroup = new Group()
    for (let item of iterable) {
      newGroup.add(item)
    }
    return newGroup;
  }
}

let group = Group.from([10, 20]);
console.log(group.has(10));
// → true
console.log(group.has(30));
// → false
group.add(10);
group.delete(10);
console.log(group.has(10));
// → false
