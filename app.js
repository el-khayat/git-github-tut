let min = 1;
let max = 100;

function getRandomNumber() {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

console.log(getRandomNumber());