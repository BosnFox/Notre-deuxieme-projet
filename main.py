import logging
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from random import choice, randint
import requests
import json
from pymorphy2 import MorphAnalyzer
from rus_eng_translate import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)

TOKEN = '5159855662:AAH1JR-a_ZjypmtsiaqsEPVfTfYQSvJHGp8'


def cl():
    with open('lang.txt', 'r') as l_file:
        return l_file.readlines()[0]


def start(update, context):
    update.message.reply_text(phrases['greeting_phrase'][cl()], reply_markup=markup)


def register(update, context):
    try:
        data = update.message.text.split()
        login, password = data[1:]
        try:
            if len(login) > 15 or len(login) < 8:
                raise Exception(phrases['register']['lenLogError'][cl()])
            if login.islower() or login.isupper():
                raise Exception(phrases['register']['caseLogError'][cl()])
            if login.isdigit() or not login.isalnum():
                raise Exception(phrases['register']['contLogError'][cl()])
            if len(password) < 8 or len(password) > 16:
                raise Exception(phrases['register']['lenPassError'][cl()])
            if password.islower() or password.isupper():
                raise Exception(phrases['register']['casePassError'][cl()])
            if password.isdigit() or password.isalpha() or not password.isalnum():
                raise Exception(phrases['register']['contPassError'][cl()])
            with open('user_data.json') as file:
                data = json.load(file)
                if login in data:
                    update.message.reply_text(phrases['register']['existedUserError'][cl()])
                    return
                else:
                    data[login] = {password: list()}
                    data[login]['password'] = password
                with open('user_data.json', 'w') as file:
                    json.dump(data, file)
                update.message.reply_text(phrases['register']['successfulRegistration'][cl()])

        except Exception as e:
            update.message.reply_text(e.__str__())

    except Exception:
        update.message.reply_text(phrases['register']['incorrectDataError'][cl()])


def add_new_post(update, context):
    line = update.message['caption'].split('; ')
    try:
        login, password, header, text = line
        login = login.split('login=')[-1]
        password = password.split('password=')[-1]
        header = header.split('header=')[-1]
        text = text.split('text=')[-1]
        with open('user_data.json') as file:
            data = json.load(file)
            if login in data and password in data[login]:
                fileID = update.message.photo[-1].file_id
                file_data = context.bot.get_file(fileID)
                downloaded_content = requests.get(file_data.file_path)
                with open(f'files/{login}_{len(data[login][password])}.jpg', 'wb') as file:
                    file.write(downloaded_content.content)
                update.message.reply_text(choice(phrases['newPostAdded']['successfulAddition'][cl()]))
            else:
                update.message.reply_text(phrases['newPostAdded']['nullUserError'][cl()])

        if login in data and password in data[login]:
            data[login][password].append([header, text, f'{login}_{len(data[login][password])}.jpg'])
            with open('user_data.json', 'w') as file:
                json.dump(data, file)
                file.close()
    except Exception:
        try:
            login, password, header = line
            login = login.split('login=')[-1]
            password = password.split('password=')[-1]
            header = header.split('header=')[-1]
            text = ''
            with open('user_data.json') as file:
                data = json.load(file)
                if login in data and password in data[login]:
                    fileID = update.message.photo[-1].file_id
                    file_data = context.bot.get_file(fileID)
                    downloaded_content = requests.get(file_data.file_path)
                    with open(f'files/{login}_{len(data[login][password])}.jpg', 'wb') as file:
                        file.write(downloaded_content.content)
                    update.message.reply_text(choice(phrases['newPostAdded']['successfulAddition'][cl()]))
                else:
                    update.message.reply_text(phrases['newPostAdded']['nullUserError'][cl()])
            if login in data and password in data[login]:
                data[login][password].append([header, text, f'{login}_{len(data[login][password])}.jpg'])
                with open('user_data.json', 'w') as file:
                    json.dump(data, file)
                    file.close()
        except Exception:
            update.message.reply_text(phrases['newPostAdded']['incorrectDataError'][cl()])


def find_user(update, context):
    data = update.message.text.split()
    if len(data) > 1:
        login = update.message.text.split()[-1]
        with open('user_data.json') as file:
            data = json.load(file)
            file.close()
        if login in data:
            word = morph.parse('пост')[0]
            count = len(data[login][data[login]["password"]])
            update.message.reply_text(f'У данного пользователя '
                                      f'{count} {word.make_agree_with_number(count).word}'
                                      if cl() == 'rus' else f'The number of posts of this user is {count}')
        else:
            names = []
            for key in data:
                if login in key and len(names) < 10:
                    names.append(key)
            if names:
                update.message.reply_text(f"{phrases['findingUser']['matchesFound'][cl()]}\n" + '\n'.join(names))
            else:
                update.message.reply_text(phrases['findingUser']['nullFound'][cl()])
    else:
        update.message.reply_text(phrases['findingUser']['nullInput'][cl()])


def show_user_post(update, context):
    try:
        line = update.message.text.split()[1:]
        login, *number = line
        number = list(map(int, number))
        with open('user_data.json') as file:
            data = json.load(file)
            file.close()
        if login in data:
            if len(data[login][data[login]['password']]) != 0:
                if len(number) == 1:
                    length = len(data[login][data[login]['password']])
                    if number[0] < 0:
                        number[0] = length + number[0]
                    post = data[login][data[login]['password']][number[0]]
                    num = f"{number[0]} {phrases['showUser']['countState'][cl()]} {login}:"
                    header, text, image = post
                    update.message.reply_text(num)
                    update.message.reply_text(header)
                    context.bot.send_photo(update.message.chat_id, photo=open(f'files/{image}', 'rb'))
                    if text:
                        update.message.reply_text(text)
                elif len(number) == 2:
                    update.message.reply_text(phrases['showUser']['collectionShow'][cl()])
                    a, b = int(number[0]), max(1, min(10, int(number[1])))
                    for i in range(a - 1, min(a + b - 1, len(data[login][data[login]['password']]))):
                        post = data[login][data[login]['password']][i]
                        num = f"{i + 1} {phrases['showUser']['countState'][cl()]} {login}:"
                        header, text, image = post
                        update.message.reply_text(num)
                        update.message.reply_text(header)
                        context.bot.send_photo(update.message.chat_id,
                                               photo=open(f'files/{image}', 'rb'))
                        if text:
                            update.message.reply_text(text)
                elif len(number) > 2:
                    raise Exception()
                else:
                    post = data[login][data[login]['password']][-1]
                    num = f"{phrases['showUser']['lastPost'][cl()]} {login}:"
                    header, text, image = post
                    update.message.reply_text(num)
                    update.message.reply_text(header)
                    context.bot.send_photo(update.message.chat_id, photo=open(f'files/{image}', 'rb'))
                    if text:
                        update.message.reply_text(text)
            else:
                update.message.reply_text(phrases['showUser']['nullPost'][cl()])
        else:
            update.message.reply_text(phrases['showUser']['noUserFound'][cl()])
    except Exception:
        update.message.reply_text(phrases['showUser']['incorrectData'][cl()])


def help(update, context):
    update.message.reply_text(phrases['helpNote'][cl()])


def change_language(update, context):
    with open('lang.txt', 'r') as l_file:
        corr = l_file.readlines()[0]
        with open('lang.txt', 'w') as le_file:
            le_file.truncate(0)
            le_file.write('rus' if corr == 'eng' else 'eng')
            le_file.close()
        l_file.close()
        update.message.reply_text(
            'Язык был изменён на Русский' if corr != 'rus' else 'Language has been changed to English')


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    morph = MorphAnalyzer()

    reply_keyboard = [['/help']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    photo_handler = MessageHandler(Filters.photo, add_new_post)

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('register', register))
    dp.add_handler(CommandHandler('find_user', find_user))
    dp.add_handler(CommandHandler('show_user_post', show_user_post))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('change_language', change_language))
    dp.add_handler(CommandHandler('cl', change_language))

    dp.add_handler(photo_handler)
    updater.start_polling()

    updater.idle()
