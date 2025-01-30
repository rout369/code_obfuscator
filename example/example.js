// A simple JavaScript example for obfuscation
function greet(name) {
    return "Hello, " + name + "!";
}

function calculateSum(a, b) {
    let result = a + b;
    console.log("Sum: " + result);
    return result;
}

const userName = "Alice";
const num1 = 5;
const num2 = 7;

console.log(greet(userName));
calculateSum(num1, num2);

// Function that uses a closure
function createMultiplier(factor) {
    return function (x) {
        return x * factor;
    };
}

const double = createMultiplier(2);
console.log("Double of 10:", double(10));

// Obfuscated function for demonstration
(function() {
    var hiddenVariable = "This is hidden";
    console.log(hiddenVariable);
})();
