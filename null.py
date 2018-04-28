import base64, hashlib
def encode(text, password):
    output = base64.b64encode(text) + hashlib.md5(password).hexdigest()
    output = base64.b64encode(output)
    return output
def decode(encoded_text, password):
    output = base64.b64decode(encoded_text)
    if hashlib.md5(password).hexdigest() not in output:
        return False
    else:
        output = output.replace(hashlib.md5(password).hexdigest(),'')
        decoded_text = base64.b64decode(output)
        return decoded_text