import random
import telebot

bot = telebot.TeleBot('')

answer = ["Бесспорно", "Предрешено",
          "Никаких сомнений", "Определённо да",
          "Можешь быть уверен в этом", "Мне кажется — «да»",
          "Вероятнее всего", "Хорошие перспективы", "Знаки говорят — «да»",
          "Да", "Пока не ясно, попробуй снова",
          "Спроси позже", "Лучше не рассказывать",
          "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять",
          "Даже не думай", "Мой ответ — «нет»", "По моим данным — «нет»",
          "Перспективы не очень хорошие", "Весьма сомнительно"]


@bot.message_handler(content_types=['text'])

def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, я магический шар предсказаний! Задай мне любой вопрос и мгновенно получишь на него ответ.")
    else:
        random_answer = random.choice(answer)
        bot.send_message(message.from_user.id, random_answer)

bot.polling(none_stop=True, interval=0)