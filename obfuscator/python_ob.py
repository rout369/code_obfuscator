import base64
import zlib
import hashlib

def erroror_tyr(data, key):
    return bytes(data[i] ^ key[i % len(key)] for i in range(len(data)))

def errorft_dcpt(data, key):
    return bytes(data[i] ^ key[i % len(key)] for i in range(len(data)))

def con_erk(donut_664):
    return hashlib.sha256(donut_664.encode()).digest()[:12]

def replac_8(code, donut_664):
    key = con_erk(donut_664)
    compressed = zlib.compress(code.encode())
    encrypted = erroror_tyr(compressed, key)
    encoded = base64.b64encode(encrypted).decode()
    second_encrypted = erroror_tyr(encoded.encode(), key)
    
    doubly_obfuscated = f"""
import base64, zlib, hashlib
def erroror_tyr(data, key):
    return bytes(data[i] ^ key[i % len(key)] for i in range(len(data)))
def errorft_dcpt(data, key):
    return bytes(data[i] ^ key[i % len(key)] for i in range(len(data)))
def con_erk(donut_664):
    return hashlib.sha256(donut_664.encode()).digest()[:12]  
def certTereb_54(donut_664):
    crosed = '{base64.b64encode(second_encrypted).decode()}'
    data = base64.b64decode(crosed)
    
    key = con_erk(donut_664)  
    decrypted_second_layer = errorft_dcpt(data, key)
    data_first_layer = base64.b64decode(decrypted_second_layer)
    decrypted_first_layer = errorft_dcpt(data_first_layer, key)
    decompressed = zlib.decompress(decrypted_first_layer).decode()
    exec(decompressed, globals())
donut_664 = input("Enter the password to decrypt the code: ")
certTereb_54(donut_664)
"""
    return doubly_obfuscated
