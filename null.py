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
    output = base64.b64encode(text) + base64.b64encode(hashlib.md5(password).hexdigest()) 
    output = base64.b64encode(output)
    output = cesar(output, 9)
    return output.replace(' ','F==x8*/e)I')
def decode(encoded_text, password):
    encoded_text = encoded_text.replace('F==x8*/e)I',' ')
    output = decode_cesar(encoded_text, 9)
    output = base64.b64decode(output)
    passw = base64.b64encode(hashlib.md5(password).hexdigest())
    if passw not in output:
        return False
    else:
        output = output.replace(passw,'')
        decoded_text = base64.b64decode(output)
        return decoded_text
