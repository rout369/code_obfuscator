// const fs = require('fs');
// const crypto = require('crypto');

// /**
//  * Generate a random alphanumeric name.
//  * @param {number} length Length of the name.
//  * @returns {string} Random name.
//  */
// function randomName(length = 8) {
//     return crypto.randomBytes(length).toString('hex').slice(0, length);
// }

// /**
//  * Rename variables in JavaScript code.
//  * @param {string} code JavaScript code.
//  * @returns {string} Obfuscated code.
//  */
// function renameVariables(code) {
//     const variableNames = [...code.matchAll(/\b(?:var|let|const)\s+(\w+)/g)].map(match => match[1]);
//     const mapping = {};

//     variableNames.forEach(varName => {
//         if (!mapping[varName]) {
//             mapping[varName] = randomName();
//         }
//     });

//     Object.entries(mapping).forEach(([oldName, newName]) => {
//         const regex = new RegExp(`\\b${oldName}\\b`, 'g');
//         code = code.replace(regex, newName);
//     });

//     return code;
// }

// /**
//  * Encode string literals as hexadecimal.
//  * @param {string} code JavaScript code.
//  * @returns {string} Obfuscated code.
//  */
// function encodeStrings(code) {
//     return code.replace(/(["'`])([^"'`]+?)\1/g, (match, quote, str) => {
//         const encoded = Buffer.from(str, 'utf8').toString('hex');
//         return `${quote}${encoded}${quote}`;
//     });
// }

// /**
//  * Flatten JavaScript code by removing line breaks and extra spaces.
//  * @param {string} code JavaScript code.
//  * @returns {string} Flattened code.
//  */
// function flattenCode(code) {
//     return code.split(/\r?\n/).map(line => line.trim()).filter(Boolean).join('; ') + ';';
// }

// /**
//  * Main obfuscation function.
//  * @param {string} code JavaScript code.
//  * @param {Object} options Obfuscation options.
//  * @returns {string} Obfuscated code.
//  */
// function obfuscateCode(code, options = { rename: true, encode: true, flatten: true }) {
//     if (options.rename) {
//         code = renameVariables(code);
//     }
//     if (options.encode) {
//         code = encodeStrings(code);
//     }
//     if (options.flatten) {
//         code = flattenCode(code);
//     }
//     return code;
// }

// // Usage
// const inputFilePath = process.argv[2];
// const outputFilePath = process.argv[3];

// if (!inputFilePath || !outputFilePath) {
//     console.error('Usage: node obfuscator.js <input-file> <output-file>');
//     process.exit(1);
// }

// try {
//     const code = fs.readFileSync(inputFilePath, 'utf8');
//     const obfuscatedCode = obfuscateCode(code, { rename: true, encode: true, flatten: true });
//     fs.writeFileSync(outputFilePath, obfuscatedCode, 'utf8');
//     console.log(`Obfuscated code saved to ${outputFilePath}`);
// } catch (err) {
//     console.error(`Error: ${err.message}`);
//     process.exit(1);
// }


const fs = require('fs');
const crypto = require('crypto');

/**
 * Generate a random alphanumeric name.
 * @param {number} length Length of the name.
 * @returns {string} Random name.
 */
function randomName(length = 8) {
    return crypto.randomBytes(length).toString('hex').slice(0, length);
}

/**
 * Rename variables in JavaScript code.
 * @param {string} code JavaScript code.
 * @returns {string} Obfuscated code.
 */
function renameVariables(code) {
    const variableNames = [...code.matchAll(/\b(?:var|let|const)\s+(\w+)/g)].map(match => match[1]);
    const mapping = {};

    variableNames.forEach(varName => {
        if (!mapping[varName]) {
            mapping[varName] = randomName();
        }
    });

    Object.entries(mapping).forEach(([oldName, newName]) => {
        const regex = new RegExp(`\\b${oldName}\\b`, 'g');
        code = code.replace(regex, newName);
    });

    return code;
}

/**
 * Encode string literals as hexadecimal.
 * @param {string} code JavaScript code.
 * @returns {string} Obfuscated code.
 */
function encodeStrings(code) {
    return code.replace(/(["'`])([^"'`]+?)\1/g, (match, quote, str) => {
        const encoded = Buffer.from(str, 'utf8').toString('hex');
        return `${quote}${encoded}${quote}`;
    });
}

/**
 * Flatten JavaScript code by removing line breaks and extra spaces.
 * @param {string} code JavaScript code.
 * @returns {string} Flattened code.
 */
function flattenCode(code) {
    return code.split(/\r?\n/).map(line => line.trim()).filter(Boolean).join('; ') + ';';
}

/**
 * Add anti-debugging measures to the code.
 * @param {string} code JavaScript code.
 * @returns {string} Code with anti-debugging added.
 */
function antiDebugger(code) {
    const antiDebuggerCode = `
        // Anti-debugging: Check for breakpoints or debugging tools
        if (typeof navigator !== 'undefined' && /Chrome|Firefox/.test(navigator.userAgent)) {
            const start = Date.now();
            while (Date.now() - start < 1000) {
                if (window.document.location.href.indexOf("debugger") !== -1) {
                    alert("Debugger detected!");
                    throw new Error("Debugger detected!");
                }
            }
        }
        
        // Simple timing-based check (slows execution during debugging)
        let startTime = new Date();
        debugger;
        if (new Date() - startTime < 100) {
            throw new Error("Debugger detected!");
        }
    `;

    return code + antiDebuggerCode;
}

/**
 * Main obfuscation function.
 * @param {string} code JavaScript code.
 * @param {Object} options Obfuscation options.
 * @returns {string} Obfuscated code.
 */
function obfuscateCode(code, options = { rename: true, encode: true, flatten: true, antiDebugger: true }) {
    if (options.rename) {
        code = renameVariables(code);
    }
    if (options.encode) {
        code = encodeStrings(code);
    }
    if (options.flatten) {
        code = flattenCode(code);
    }
    if (options.antiDebugger) {
        code = antiDebugger(code);
    }
    return code;
}

// Usage
const inputFilePath = process.argv[2];
const outputFilePath = process.argv[3];

if (!inputFilePath || !outputFilePath) {
    console.error('Usage: node obfuscator.js <input-file> <output-file>');
    process.exit(1);
}

try {
    const code = fs.readFileSync(inputFilePath, 'utf8');
    const obfuscatedCode = obfuscateCode(code, { rename: true, encode: true, flatten: true, antiDebugger: true });
    fs.writeFileSync(outputFilePath, obfuscatedCode, 'utf8');
    console.log(`Obfuscated code saved to ${outputFilePath}`);
} catch (err) {
    console.error(`Error: ${err.message}`);
    process.exit(1);
}
