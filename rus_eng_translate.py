phrases = {
    'greeting_phrase': {
        'rus': 'Вас приветствует авторское програмное обеспечение, '
               'предоставляющее Вас возможность беспрепятственно публиковать '
               'свои записи, а также просматривать публикации других пользователей.'
               ' Для большей осведомлённости рекомендуем начать взаимодействие с'
               ' программным обеспечием через команду /help',
        'eng': 'You are welcomed to be seen in our authoring software, with which you can freely'
               ' publish your posts and view the posts of other users. For greater awareness, we'
               ' recommend that you start interacting with the program through the /help command'
    },
    'register': {
        'lenLogError': {
            'rus': 'Длина логина должна быть не меньше 8 и не больше 15 символов!',
            'eng': 'Login length must be between 8 and 15 characters'
        },
        'caseLogError': {
            'rus': 'В логине должны присутствовать символы верхнего и нижнего регистров!',
            'eng': 'Login must contain both uppercase and lowercase characters'
        },
        'contLogError': {
            'eng': 'Login must contain both digits and Latin characters',
            'rus': 'Логин должен состоять из цифр и букв латиницы!'
        },
        'lenPassError': {
            'rus': 'Длина пароля не должна быть меньше 8 или больше 16 символов!',
            'eng': 'Password length must be between 8 and 16 characters'
        },
        'casePassError': {
            'rus': 'В пароле должны быть как символы верхнего регистра, так и нижнего!',
            'eng': 'Password must contain both uppercase and lowercase characters'
        },
        'contPassError': {
            'eng': 'Password must contain both digits and Latin characters',
            'rus': 'Правильный пароль обязан состоять из цифр и букв латинского алфавита!'
        },
        'existedUserError': {
            'eng': "A user with this login already exists",
            'rus': 'Такой пользователь уже существует!'
        },
        "successfulRegistration": {
            'eng': "User has been successfully registered. Use the /add_new_post command to post",
            'rus': 'Вы успешно зарегистрировались в системе!\n'
                   'Теперь можете начать делать публикации с помощью команды /add_new_post!'
        },
        "incorrectDataError": {
            'eng': "Incorrect registration data was entered.\n"
                   "Example of correct registration: /register NewUser123 Password@123",
            'rus': 'Вы неправильно ввели данные для регистрации!\n'
                   'Правильная регистрация выглядит так:\n'
                   '/register NewUser123 Password@123'
        }
    },
    'newPostAdded': {
        'successfulAddition': {
            'rus': ["Новая запись данного содержания была успешно добавлена",
                    "Очередная запись была добалена в поплняющийся список Ващих записей",
                    "Преинтересная запись, повествующая о чём-то интересном стала "
                    "частью Вашей истории наравне с другими",
                    "Просто описанная и задокументированная в цифровом коде, запись была успешно добавлена",
                    "Новая запись  - новое желание записать прекрасный день своей жизни",
                    "Запись добавлена", "Запись успешно добавлена", "Данным пользователем была добавлена запись"],
            'eng': ["A new entry of this content has been successfully added",
                    "Another entry has been added to the growing list of your entries",
                    "An interesting entry that tells about something interesting has become part of your story"
                    " along with others,"
                    "Simply described and digitally documented, the entry has been successfully added",
                    "New entry - a new desire to record a beautiful day of your life",
                    "Entry has been added", "Entry has been added successfully", "Entry has been added by this user"]
        },
        'nullUserError': {
            'rus': 'Данный пользователь не может делать посты, так как он не зарегистрирован в системе!',
            'eng': 'This user cannot publish messages due to his non-existence in the database'
        },
        'incorrectDataError': {
            'rus': 'Введены некорректные данные для публикации поста',
            'eng': 'Incorrect data entered for publishing a post'
        }
    },
    'findingUser': {
        'matchesFound': {
            'rus': 'Возможно, вы имели в виду пользователей:',
            'eng': 'Did you mean:'
        },
        'nullFound': {
            'rus': 'Пользователь не найден',
            'eng': 'User is not found'
        }
    },
    'showUser': {
        'countState': {
            'rus': 'пост пользователя',
            'eng': 'post of'
        },
        'collectionShow': {
            'rus': 'Коллекция постов:',
            'eng': 'Post collection:'
        },
        'lastPost': {
            'rus': 'Последний пост пользователя',
            'eng': 'User last post'
        },
        'nullPost': {
            'rus': 'У данного пользователя нет публикаций',
            'eng': 'This user has no posts'
        },
        'noUserFound': {
            'rus': 'Пользователь не найден',
            'eng': 'This user is not found'
        }
    },
    'helpNote': {
        'rus': 'Команды:\n\n'
               '"/register [логин] [пароль]" - логин должен состоять из нижнего и '
               'верхнего регистров латинского алфавита, может содержать цифры\n\nПример:  '
               '/register NewUser123 Password2022\n\n'
               'Команда, добавляющая прикреплённую фотографию к вашим постам:\n\n'
               '"/add_new_post login=[ваш логин]; password=[ваш пароль]; '
               'header=[заголовок поста]; text=[содержимое публикации, но данный '
               'параметр необязательный]"\n\n'
               'Пример(прикрепляете фотографию):  /add_new_post login=NewUser123; '
               'password=Password2022; header=New post; text=Some description\n\n'
               '"/find_user [user]" - команда скажет, есть ли такой пользователь '
               'в системе, и если да, то проинформирует о его опублкованных постах, '
               'если нет, то выведет пользователей, чьи логины содержать данную '
               'строку\n\n'
               'Пример:  /find_user NewUser123\n\n'
               '"/show_user_post [user]"\n\n',
        'eng': 'Commands:\n\n'
               '"/register [login] [password]" - login must consist of lower and upper cases of '
               'the Latin alphabet, may contain numbers\n\nExample: '
               '/register NewUser123 Password2022\n\n'
               'Command to add attached photo to your posts:\n\n'
               '"/add_new_post login=[your login]; password=[your password]; '
               'header=[post title]; text=[post content, optional parameter]"\n\n'
               'Example (attach photo): /add_new_post login=NewUser123; '
               'password=Password2022; header=new post; text=Some description\n\n'
               '"/find_user [user]" - the command will tell if there is such a user in the system, '
               'and if yes, it will inform about his published posts, if not, it will '
               'display users whose logins contain this string\n\n'
               'Example: /find_user NewUser123\n\n'
               '"/show_user_post [user]"\n\n'
    }
}
