import sys
import time
import random
import datetime
import telepot
from imgurpython import ImgurClient
from random import randint

client_id = ''
client_secret = ''
client = ImgurClient(client_id, client_secret)


def handle(msg):
    chat_id = msg['chat']['id']
    full = msg['text']                   #ves' input pol'zovatelya
    command = full.split(' ',1)[0]       #sama commanda
    if (len(full.split(' ', 1)) != 1):               #obrabatyvaem dlya funkciy bez argumentov
        argument = full.split(' ', 1)[1].lower()     #argument
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    if command == '/atbash':
    	result_string = ''
    	for i in argument:
    		if i in alphabet:                                  #prover'aem est' li on v alfavite
    		    input_num = alphabet.index(i)
                output_num = (len(alphabet) - (input_num + 1))
                result_elem = alphabet[output_num]
                result_string = result_string + result_elem
            else:                                              #esli net -> tupo ego dobavlyaem ne izmenaya
            	result_string = result_string + i 
    	bot.sendMessage(chat_id, result_string)

    if command == '/hey':
    	pic_links = []
    	items = client.get_album_images('Bp8I9')    #moi albom v imgur
        for item in items:                     
        	pic_links.append(item.link)             #pihaem vse ssylki v odin list
        pics_quantity = len(pic_links)              #schitaem razmer lista berem randomnoe znachenie i vivodim na ekran
        pic_num = randint(0,pics_quantity)
        bot.sendMessage(chat_id, "Hello! I'm Capybara Bot!")
        bot.sendMessage(chat_id, pic_links[pic_num])

bot = telepot.Bot('')
bot.notifyOnMessage(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)
