from PIL import Image
im = Image.open('res.png')
q = 0
result = ""
input_string = ""
d = {'00000' : 'a',\
	 '00001' : 'b',\
	 '00010' : 'c',\
	 '00011' : 'd',\
	 '00100' : 'e',\
	 '00101' : 'f',\
	 '00110' : 'g',\
	 '00111' : 'h',\
	 '01000' : 'i',\
	 '01001' : 'j',\
	 '01010' : 'k',\
	 '01011' : 'l',\
	 '01100' : 'm',\
	 '01101' : 'n',\
	 '01110' : 'o',\
	 '01111' : 'p',\
	 '10000' : 'q',\
	 '10001' : 'r',\
	 '10010' : 's',\
	 '10011' : 't',\
	 '10100' : 'u',\
	 '10101' : 'v',\
	 '10111' : 'w',\
	 '11000' : 'x',\
	 '11001' : 'y',\
	 '11010' : 'z',\
	 '11011' : '1',\
	 '11100' : '2',\
	 '11101' : '3',\
	 '11110' : '4',\
	 '11111' : ' '}

raw_input_pixels = list(im.getdata())
input_binary_array = []


for i in raw_input_pixels:
	value = i[2]
	if (value%2)==0:
		input_binary_array.append(0)
	else:
		input_binary_array.append(1)


for i in range(0, len(input_binary_array)):
#for i in range(0, 20):
	input_string = input_string + str(input_binary_array[i])
	q = q + 1
	if (q > 4):
		if d.get(input_string) is not None:
			result = result + d.get(input_string)
			input_string = ""
			q = 0
		else:
			break
		
		
print result
#for i in range (0,8):
#	print input_binary_array[i]
