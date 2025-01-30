
import fs from 'fs';

const greeting = "Hello, World!";
let count = 0;

function sayHello() {
    console.log(greeting);
}

function addNumbers(a, b) {
    let sum = a + b;
    console.log(`Sum: ${sum}`);
    return sum;
}

class Calculator {
    multiply(a, b) {
        return a * b;
    }

    divide(a, b) {
        if (b !== 0) {
            return a / b;
        } else {
            console.log("Division by zero!");
            return null;
        }
    }
}

const calc = new Calculator();
sayHello();
addNumbers(3, 4);
console.log(calc.multiply(2, 5));
console.log(calc.divide(10, 2));
console.log(calc.divide(10, 0));
