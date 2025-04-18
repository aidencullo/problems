// Building Promise.all
// As we saw, given an array of promises, Promise.all returns a promise that waits for all of the promises in the array to finish. It then succeeds, yielding an array of result values. If a promise in the array fails, the promise returned by all fails too, passing on the failure reason from the failing promise.

// Implement something like this yourself as a regular function called Promise_all.

// Remember that after a promise has succeeded or failed, it can’t succeed or fail again, and further calls to the functions that resolve it are ignored. This can simplify the way you handle a failure of your promise.

function Promise_all(promises) {
  let resolved = 0;
  const results = [];
  return new Promise((resolve, reject) => {
    promises.forEach((promise, i) => {
      promise
	.then((value) => {
	  results[i] = value;
	  resolved++;
	  if (resolved === promises.length) resolve(results);
	})
	.catch(reject);
    })
    if (promises.length === 0) resolve(results);
  });
}

// Test code.
Promise_all([]).then(array => {
  console.log("This should be []:", array);
});
function soon(val) {
  return new Promise(resolve => {
    setTimeout(() => resolve(val), Math.random() * 500);
  });
}
Promise_all([soon(1), soon(2), soon(3)]).then(array => {
  console.log("This should be [1, 2, 3]:", array);
});
Promise_all([soon(1), Promise.reject("X"), soon(3)])
  .then(array => {
    console.log("We should not get here");
  })
  .catch(error => {
    if (error != "X") {
      console.log("Unexpected failure:", error);
    }
  });

