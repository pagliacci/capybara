from PIL import Image
im = Image.open('lena.png')
binary_message = ""
d = {'a' : '00000',\
	 'b' : '00001',\
	 'c' : '00010',\
	 'd' : '00011',\
	 'e' : '00100',\
	 'f' : '00101',\
	 'g' : '00110',\
	 'h' : '00111',\
	 'i' : '01000',\
	 'j' : '01001',\
	 'k' : '01010',\
	 'l' : '01011',\
	 'm' : '01100',\
	 'n' : '01101',\
	 'o' : '01110',\
	 'p' : '01111',\
	 'q' : '10000',\
	 'r' : '10001',\
	 's' : '10010',\
	 't' : '10011',\
	 'u' : '10100',\
	 'v' : '10101',\
	 'w' : '10111',\
	 'x' : '11000',\
	 'y' : '11001',\
	 'z' : '11010',\
	 '1' : '11011',\
	 '2' : '11100',\
	 '3' : '11101',\
	 '4' : '11110',\
	 ' ' : '11111'}

raw_input_pixels = list(im.getdata())
width, height = im.size
input_binary_array = []
test = []
raw_output_pixels = raw_input_pixels

for i in raw_input_pixels:
	value = i[2]
	if (value%2)==0:
		input_binary_array.append(0)
	else:
		input_binary_array.append(1)

message = 'simon'
for i in message:
	print i
	print d.get(i)
	binary_message = binary_message + d.get(i)

for i in range(0, len(binary_message)):
    input_binary_array[i] = int(binary_message[i])   #delaem binary massiv iz kotorogo budem vosstanavlivat' izobrazhenie

for i in range(0, len(binary_message)):
	if (input_binary_array[i] != ((raw_input_pixels[i])[2]%2)):
		raw_output_pixels[i] = ((raw_input_pixels[i])[0], (raw_input_pixels[i])[1], ((raw_input_pixels[i])[2] + 1))

newimg = Image.new('RGB', im.size)

newimg.putdata(raw_output_pixels)
newimg.save('res.png', 'PNG')
