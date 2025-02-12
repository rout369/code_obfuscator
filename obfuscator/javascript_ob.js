const fs = require("fs");
const crypto = require("crypto");
const zlib = require("zlib");

// XOR Encryption Function
function xorEncrypt(data, key) {
    let keyBuffer = Buffer.from(key);
    let dataBuffer = Buffer.from(data);
    let encrypted = Buffer.alloc(dataBuffer.length);

    for (let i = 0; i < dataBuffer.length; i++) {
        encrypted[i] = dataBuffer[i] ^ keyBuffer[i % keyBuffer.length];
    }
    return encrypted;
}

// XOR Decryption Function (same as encryption)
function xorDecrypt(data, key) {
    return xorEncrypt(data, key);
}

// Function to derive a key from the password
function deriveKey(password) {
    return crypto.createHash("sha256").update(password).digest().slice(0, 12); // 12-byte key
}

// Function to obfuscate JavaScript code
function obfuscateJavaScript(code, password) {
    let key = deriveKey(password);

    // First obfuscation: Compress, Encrypt, Base64 Encode
    let compressed = zlib.deflateSync(Buffer.from(code, "utf-8"));
    let encrypted = xorEncrypt(compressed, key);
    let encoded = Buffer.from(encrypted).toString("base64");

    // Second obfuscation: Encrypt again with XOR
    let secondEncrypted = xorEncrypt(Buffer.from(encoded, "utf-8"), key);
    let finalEncoded = Buffer.from(secondEncrypted).toString("base64");

    // Return obfuscated JavaScript code that can decrypt itself
    return `
const crypto = require("crypto");
const zlib = require("zlib");

function xorDecrypt(data, key) {
    let keyBuffer = Buffer.from(key);
    let decrypted = Buffer.alloc(data.length);
    for (let i = 0; i < data.length; i++) {
        decrypted[i] = data[i] ^ keyBuffer[i % keyBuffer.length];
    }
    return decrypted;
}

function deriveKey(password) {
    return crypto.createHash("sha256").update(password).digest().slice(0, 12);
}

function executeObfuscatedCode(password) {
    let encoded = "${finalEncoded}";
    let data = Buffer.from(encoded, "base64");

    let key = deriveKey(password);
    let decryptedSecondLayer = xorDecrypt(data, key);
    let decodedFirstLayer = Buffer.from(decryptedSecondLayer).toString("utf-8");
    let decryptedFirstLayer = xorDecrypt(Buffer.from(decodedFirstLayer, "base64"), key);
    
    let decompressed = zlib.inflateSync(decryptedFirstLayer).toString("utf-8");
    eval(decompressed);
}

const password = require("readline-sync").question("Enter password to decrypt the code: ", { hideEchoBack: true });
executeObfuscatedCode(password);
`;
}

// Read input file, obfuscate, and write to output file
const inputFile = process.argv[2];
const outputFile = process.argv[3];
const password = process.argv[4];

if (!inputFile || !outputFile || !password) {
    console.error("Usage: node javascript_ob.js <inputFile> <outputFile> <password>");
    process.exit(1);
}

fs.readFile(inputFile, "utf8", (err, data) => {
    if (err) {
        console.error("Error reading file:", err);
        return;
    }

    let obfuscatedCode = obfuscateJavaScript(data, password);

    fs.writeFile(outputFile, obfuscatedCode, (err) => {
        if (err) {
            console.error("Error writing file:", err);
            return;
        }
    });
});
