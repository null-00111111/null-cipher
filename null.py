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
    output = output.replace('`','27+A==x1x1*/e[I')
    output = output.replace('{','09+D==x4*/[K')
    output = output.replace('}','99+G==x8x1*/[L')
    output = output.replace('}','99+G==x8x2*/[L')
    output = output.replace('>','52+N==x16x1*/[Q')
    output = output.replace('<','52+N==x16x2*/[Q')
    output = output.replace('\\','04+Q==x32*/[Q')
    output=output.replace('^','01+B==x2*/[J')
    return output.replace(' ','F==x8*/e)I')
def decode(encoded_text, password):
    output = encoded_text.replace('F==x8*/e)I',' ')
    output=output.replace('01+B==x2*/[J','^')
    output=output.replace('09+D==x4*/[K','{')
    output=output.replace('99+G==x8x1*/[L','}')
    output=output.replace('99+G==x8x2*/[L','}')
    output=output.replace('52+N==x16x1*/[Q','>')
    output=output.replace('52+N==x16x2*/[Q','<')
    output=output.replace('04+Q==x32*/[Q','\\')
    output=output.replace('27+A==x1x1*/e[I','`')
    output = decode_cesar(output, 9)
    output = base64.b64decode(output)
    passw = base64.b64encode(hashlib.md5(password).hexdigest())
    if passw not in output:
        return False
    else:
        output = output.replace(passw,'')
        decoded_text = base64.b64decode(output)
        return decoded_text
