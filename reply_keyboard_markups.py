import telebot

class Keyboard:
    def __init__(self, bot):
        self.bot = bot

    def main_menu(self, message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
        user_markup.row("Получить расписание")
        user_markup.row("Получить расписание по подписке")
        user_markup.row("Время пар")
        user_markup.row('Обновления', 'Обратная связь')
        self.bot.send_message(message.from_user.id, 'Выберите пункт меню:', reply_markup=user_markup)
