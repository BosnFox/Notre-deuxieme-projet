import logging
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
from random import randint
import requests
import json
from pymorphy2 import MorphAnalyzer

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

logger = logging.getLogger(__name__)

TOKEN = '5159855662:AAH1JR-a_ZjypmtsiaqsEPVfTfYQSvJHGp8'


def echo(update, context):
    update.message.reply_text(update.message.text)


def start(update, context):
    update.message.reply_text('Здесь будет описание', reply_markup=markup)


def register(update, context):
    try:
        data = update.message.text.split()
        login, password = data[1:]
        try:

            if len(login) > 15 or len(login) < 8:
                raise Exception('Длина логина должна быть не меньше 8 и не больше 15 символов!')
            if login.islower() or login.isupper():
                raise Exception('В логине должны присутствовать символы верхнего и нижнего регистров!')
            if login.isdigit() or not login.isalnum():
                raise Exception('Логин может состоять из цифр и букв латиницы!')

            if len(password) < 8 or len(password) > 16:
                raise Exception('Длина пароля не должна быть меньше 8 или больше 16 символов!')
            if password.islower() or password.isupper():
                raise Exception('В пароле должны быть как символы верхнего регистра, так и нижнего!')
            if password.isdigit() or password.isalpha() or not password.isalnum():
                raise Exception('Правильный пароль обязан состоять из цифр и букв латинского алфавита')

            with open('user_data.json') as file:
                data = json.load(file)
                if login in data:
                    update.message.reply_text('Такой пользователь уже существует!')
                    return
                else:
                    data[login] = {password: list()}
                    data[login]['password'] = password
                with open('user_data.json', 'w') as file:
                    json.dump(data, file)
                update.message.reply_text('Вы успешно зарегистрировались в системе!\n'
                                          'Теперь можете начать делать публикации с помощью'
                                          ' команды /add_new_post!')

        except Exception as e:
            update.message.reply_text(e.__str__())
    except Exception:
        update.message.reply_text('Вы неправильно ввели данные для регистрации!\n'
                                  'Правильная регистрация выглядит так:\n'
                                  '/register NewUser123 Password@123')


def add_new_post(update, context):
    line = update.message['caption'].split('; ')
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

        else:
            update.message.reply_text('Данный пользователь не может делать посты, так как он '
                                      'не зарегистрирован в системе')

    if login in data and password in data[login]:
        data[login][password].append([header, text, f'{login}_{len(data[login][password])}.jpg'])
        with open('user_data.json', 'w') as file:
            json.dump(data, file)


def find_user(update, context):
    login = update.message.text.split()[-1]
    with open('user_data.json') as file:
        data = json.load(file)
    if login in data:
        word = morph.parse('пост')[0]
        count = len(data[login][data[login]["password"]])
        update.message.reply_text(f'У данного пользователя '
                                  f'{count} {word.make_agree_with_number(count).word}.')
    else:
        update.message.reply_text('Пользователь не найден')


def show_userpost(update, context):
    login = update.message.text.split()[-1]
    with open('user_data.json') as file:
        data = json.load(file)
    if login in data:
        post = data[login][data[login]['password']][-1]
        header, text, image = post
        update.message.reply_text(header)
        context.bot.send_photo(update.message.chat_id, photo=open(f'files/{image}', 'rb'))
        update.message.reply_text(text)
    else:
        update.message.reply_text('Пользователь не найден')


if __name__ == '__main__':

    updater = Updater(TOKEN)
    dp = updater.dispatcher
    morph = MorphAnalyzer()

    reply_keyboard = [['/help']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    photo_handler = MessageHandler(Filters.photo, add_new_post)
    text_handler = MessageHandler(Filters.text & ~Filters.command, echo)

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('register', register))
    dp.add_handler(CommandHandler('find_user', find_user))
    dp.add_handler(CommandHandler('show_userpost', show_userpost))

    dp.add_handler(photo_handler)
    dp.add_handler(text_handler)
    updater.start_polling()

    updater.idle()
