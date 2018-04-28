import null


print('\t[1] Encode text')
print('\t[2] Decode text')
print('\t[3] Encode file')
options = ['1','2','3']
q = raw_input('\nSelect a option> ')


if q not in options:
    print('Invalid option selected')
    exit()


if q == options[0]:
    text_to_encode = raw_input('\nText to encode> ')
    passw = raw_input('Password to use> ')
    encoded_text = null.encode(text_to_encode,passw)
    print('Encoded text: %s' %encoded_text)


if q == options[1]:
    text_to_decode = raw_input('\nTexto to decode> ')
    passw = raw_input('Your password> ')
    decoded_text = null.decode(text_to_decode,passw)
    if decoded_text == False:
        print('Invalid password!')
    else:
	print('Decoded text: %s' %decoded_text)
if q == options [2]:
	file_to_encode = raw_input('\nFile to encode> ')
	passw = raw_input('Password to use> ')
	with open(file_to_encode) as file:
		content = file.read()
		encoded_content = null.encode(content,passw)
		file.close()
		with open(file_to_encode,'w') as encoded_file:
			encoded_file.write(encoded_content)
			encoded_file.close()