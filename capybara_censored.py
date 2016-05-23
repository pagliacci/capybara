#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
from lxml import html
import sys
import datetime
import time
import random
import datetime
import telepot
from imgurpython import ImgurClient
from random import randint
import requests
import json
import urllib2
chat_ids = [574068, 113206012, 54430588]

client_id = ''
client_secret = ''
client = ImgurClient(client_id, client_secret)
label = 0

def handle(msg):
    chat_id = msg['chat']['id']
    full = msg['text']                   #ves' input pol'zovatelya
    command = full.split(' ',1)[0]       #sama commanda
    if (len(full.split(' ', 1)) != 1):               #obrabatyvaem dlya funkciy bez argumentov
        argument = full.split(' ', 1)[1].lower()     #argument
    en_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ru_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    
    if command == '/atbash':
        result_string = ''
        for i in argument:
            if i.encode("utf-8") in en_alphabet:                                  #prover'aem est' li on v alfavite
                input_num = en_alphabet.index(i.encode("utf-8"))
                output_num = (len(en_alphabet) - (input_num + 1))
                result_elem = en_alphabet[output_num]
                result_string = result_string + result_elem
            elif i.encode("utf-8") in ru_alphabet:                                  #prover'aem est' li on v alfavite
                input_num = ru_alphabet.index(i.encode("utf-8"))
                output_num = (len(ru_alphabet) - (input_num + 1))
                result_elem = ru_alphabet[output_num]
                result_string = result_string + result_elem    
            else:                                              #esli net -> tupo ego dobavlyaem ne izmenaya
            	result_string = result_string + i.encode("utf-8") 
        bot.sendMessage(chat_id, result_string)

    if command.startswith('/hey'):
    	pic_links = []
    	items = client.get_album_images('Bp8I9')
        for item in items:
            pic_links.append(item.link)             #pihaem vse ssylki v odin list
        pics_quantity = len(pic_links)              #schitaem razmer lista berem randomnoe znachenie i vivodim na ekran
        pic_num = randint(0,pics_quantity)
        cap_img = urllib2.urlopen(pic_links[pic_num])
        cap_img.name = "cap_img.jpg"
        bot.sendMessage(chat_id, "Hello! I'm Capybara Bot!")
        bot.sendPhoto(chat_id, cap_img)
    
    if command == '/inst':
        r = requests.get('\')
        data = r.text
        parsed_json = json.loads(data)
        data = parsed_json['data'][0]['images']['standard_resolution']['url']
        f = urllib2.urlopen(data)
        f.name = "name.jpg"
        bot.sendPhoto(chat_id, f)
    
    if command.startswith('/menu'):
        response = requests.get('http://www.lamantin-kafe.ru/lamantin-menu-bistro-obuhov/')
        s = "*Меню на сегодня*" + " *(" + now.strftime("%d/%m/%y") +"):* " + "\n"
        soup = BeautifulSoup(response.text, 'html.parser')
        menu = soup.tbody
        for tag in menu.find_all("td")[4:]:
            try:
                if tag[u'width'] == "75%":
                    if tag.span:
                        temp_string = "\n" + "*" + tag.get_text() + "*"
                    else:
                        pre_temp_string = tag.get_text()
                        sep = '/'
                        temp_string = pre_temp_string.split(sep, 1)[0]
                    s = s + temp_string + "\n"
            except KeyError:
                pass
        s = s + "\n" + "Для вызова расширенной версии меню:" + "\n" + "/extend"  
        bot.sendMessage(chat_id, s, parse_mode='Markdown')

    if command.startswith('/extend'):
        response = requests.get('http://www.lamantin-kafe.ru/lamantin-menu-bistro-obuhov/')
        s = "*Расширенная версия меню:*"
        soup = BeautifulSoup(response.text, 'html.parser')
        menu = soup.tbody
        for tag in menu.find_all("td")[4:]:
            try:
                if tag[u'width'] == "75%":
                    if tag.span:
                        temp_string = "\n" + "*" + tag.get_text() + "*"
                        content_string = ""  
                    else:
                        pre_temp_string = tag.get_text()
                        sep = '/'
                        if (pre_temp_string.split(sep,1)[0] != pre_temp_string.split(sep,1)[-1]):
                            temp_string = pre_temp_string.split(sep, 1)[0]
                            pre_content_string = pre_temp_string.split(sep, 1)[-1]
                            content_string = " _(" + pre_content_string[:-1] + ")_ "
                        else:
                            temp_string = pre_temp_string.split(sep, 1)[0]
                            content_string = ""
                    s = s + temp_string + content_string + "\n"
                if tag[u'width'] == "10%" and tag.get_text()!="":
                    s = s + "Цена: " +  tag.get_text() + "\n"
            except KeyError:
                pass
        bot.sendMessage(chat_id, s, parse_mode='Markdown')

bot = telepot.Bot('\')
bot.notifyOnMessage(handle)
print ('I am listening ...')


while 1:
    time.sleep(1)
    now = datetime.datetime.now()
    if (now.hour==22 and now.minute==21 and label==0):
        for chat_id in chat_ids:
            bot.sendMessage(chat_id, "Get ready to make a wish!")
            time.sleep(1)
            label = 1
    elif (now.hour==22 and now.minute==22 and label==1):
        for chat_id in chat_ids:
            bot.sendMessage(chat_id, "Act now!")
            time.sleep(1)
        label = 2
    elif (now.hour==22 and now.minute==23 and label==2):
        for chat_id in chat_ids:
            bot.sendMessage(chat_id, "Your wish will definitely come true!")
            time.sleep(1)
        label = 0


