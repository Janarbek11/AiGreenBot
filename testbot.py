import telebot
from telebot import types

bot = telebot.TeleBot('2090390473:AAHUP6CAvBopNiWNjlS62Vwjc0eMZgSirAc')

inf = '''Почему к фото Грин Кард на лотерею столько требований и почему нужно отнестись к каждому пункту серьезно? Дело в том, что все фотографии в заявке на лотерею Грин Карты проверяет не человек, а специальная компьютерная программа. И если фотография не подойдет, хотя бы, по одному требованию, то программа не сможет распознать ваше лицо и ваша заявка на лотерею гринки будет дисквалифицирована.

Вы можете самостоятельно сфотографироваться в домашних условиях, либо сходить в фото-сервис (где знакомы с этими требованиями). Внимание, я не сомневаюсь в профессионализме фото-сервисов, но придя домой, все же не поленитесь, проверить ваше фото Green Card на требования, мало ли что.

Для участия в DV лотерее Грин Карты, у вас должна быть электронная цифровая или отсканированная фотография, по следующим требованиям:
— она должна быть цветная;
— голова на фотографии должна занимать от 50% до 69% от общей высоты изображения, начиная с верхней части головы, включая волосы до нижней части подбородка;
— глаза должны находиться в промежутке от 56% до 69% от высоты изображения, то есть от нижней части изображения до уровня глаз;
— фотография должна быть квадратная. С 2019 года, размером только 600 пикселей (ширина) х 600 пикселей (высота);
— фотография должна быть не позже 6-ти месяцев, а еще лучше если вы сделали ее на прошлой неделе;
— фон фотографии должен быть хорошо освещен, белого или светло-желтоватого цвета (без каких-либо узоров, объектов, рисунков и прочих);
— ваш взгляд должен быть направлен прямо в камеру с обычным выражением лица и открытыми глазами;
— на фотографии вы должны быть в обычной одежде, которую вы носите каждый день. Не в рабочей спец. форме, если только это не религиозная одежда, которую носят постоянно;
— без какого-либо головного убора, которое скрывает ваши волосы, за исключением религиозных головных уборов, которые носят каждый день;
— если вы носите очки, то с 2016 года, фото следует делать без очков;
— отсканированные фотографии с водительских прав или других официальных документах не допускаются;
— фото должно быть без теней.

Технические характеристики фото Грин Кард для лотереи должны быть:
— в формате JPEG (JPG);
— с размером файла, равном или меньшим 240 Кб (килобайт);
— и как, я уже писал выше, в квадратной пропорции (высота должна быть равна ширине). Размеры 600px x 600px;
— фотография должна быть цветная (24 бит на пиксель) в спектре sRGB;
— возможно фотография на Грин Карту у вас будет весить больше требуемого, поэтому вам нужно ее сжать. Степень сжатия должна быть меньше или равна 20:1;
— если вы сканируете фото, то она должна быть отсканирована с разрешением 300 пикселей на дюйм (12 пикселей на миллиметр).'''


@bot.message_handler(commands=['start'])
def start_message(message):
    kbrd = types.InlineKeyboardMarkup()
    kbrd1 = types.InlineKeyboardButton(text='Способ оплаты', callback_data='payment')
    kbrd2 = types.InlineKeyboardButton(text='Стоимость услуги', callback_data='price')
    kbrd3 = types.InlineKeyboardButton(text='Эл. почта', callback_data='e-mail')
    kbrd4 = types.InlineKeyboardButton(text='Информация', callback_data='info')
    # kbrd5 = types.InlineKeyboardButton(text='Green Card 2023', callback_data='dv')
    kbrd.add(kbrd1, kbrd2, kbrd3, kbrd4)
    bot.send_message(message.chat.id, 'Здраствуйте Вас приветствует AiGreenBot', reply_markup=kbrd)


@bot.callback_query_handler(func=lambda ans: True)
def ans(call):
    if call.data == 'payment':
        bot.send_message(call.message.chat.id, text='MBank: 996509880980\n'
                                                    'Элсом: 0509880980\n'
                                                    'Демир банк: 4215890118866166\n'
                                                    'Оптима банк: 4169585341970571\n'
                                                    'Обязательно отправьте мне чек')

    elif call.data == 'price':
        bot.send_message(call.message.chat.id, text='Стоимость услуги 500 + фото в подарок')
    elif call.data == 'e-mail':
        bot.send_message(call.message.chat.id, text='a.bayazova@mail.ru')
    elif call.data == 'info':
        bot.send_message(call.message.chat.id, text=inf)
    # elif call.data == 'dv':
        # bot.send_message(501776073, text='Ваше имя?')
        # if call.data != '':
        #     bot.send_message(501776073,     call.data)



bot.polling(none_stop=True)
