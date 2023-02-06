# telegramBot8

[Ru] echo_bot - эхо‑бот будет получать от пользователя текстовое сообщение и возвращать его

Взят по рекондации Хауди Хо https://mastergroosha.github.io/telegram-tutorial/docs/pyTelegramBotAPI/lesson_00/

## Требования:
* $ pip install -r requirements.txt
* создать файл config.py, в котором будут храниться токен для доступа к боту в виде
```python 
token = "1234567890:ASDFGHH..."
```

## Где взять token?
* https://xakep.ru/2021/11/28/python-telegram-bots/

## Примеры использования

#### Получение сообщений от юзера
```python
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)
```

#### Запускаем бота
```python
if __name__ == '__main__':
     bot.infinity_polling()  # бот будет стараться не прекращать работу при возникновении каких-либо ошибок
```