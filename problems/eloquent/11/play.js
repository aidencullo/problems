// async function error() {
//   throw Error()
// }

// // console.log(error())
// new Promise((res, rej) => {
//   res(error())
// })
//   .then(console.log)
//   .catch(console.log)

new Promise((res, rej) => {
  // res(throw Error())
  res(new Error())
})
  .then(console.log)
  .catch(console.log)
