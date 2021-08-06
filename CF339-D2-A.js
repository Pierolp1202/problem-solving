var input  = window.prompt()

let arr = input.split("+");

let results = arr.sort((a,b) => a-b);

console.log(results.join("+"))