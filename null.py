import base64, hashlib

def cesar(text, n):
    byte = []
    for i in text:
        byte.append(ord(i))
    output = ''
    for b in byte:
        output+=chr(b+n)
    return output
def decode_cesar(text, n):
    byte = []
    for i in text:
        byte.append(ord(i))
    output = ''
    for b in byte:
        output+=chr(b-n)
    return output
def encode(text, password):
    text = cesar(text, 18)
    output = base64.b64encode(text) + base64.b64encode(hashlib.md5(password).hexdigest()) 
    output = base64.b64encode(output)
    output = cesar(output, 9)
    return output
def decode(encoded_text, password):
    output = base64.b64decode(encoded_text)
    passw = base64.b64encode(hashlib.md5(password).hexdigest())
    if passw not in output:
        return False
    else:
        output = decode_cesar(output, 9)
        output = output.replace(passw,'')
        decoded_text = base64.b64decode(output)
        decoded_text = decode_cesar(decoded_text, 18)
        return decoded_text
