# Урок 1. Мій перший асистент у консолі
# Стартовий код: змініть ім'я, характер і додайте власні реакції.
import random

NAME = "Eset"          # ім'я асистента
STYLE = "Дурний"      # характер: дружній, суворий, смішний, спокійний...

GREETINGS = [
    "Привіт-привіт! Мені приємно!",
    "Ось і ти! Без розмови було нудно.",
    "Вітаю! Допомога вже в дорозі.",
]
MOTIVATION = [
    "Кожен експерт колись був новачком. Ти вже на шляху!",
    "Помилка — це не провал, а підказка. Спробуй ще раз!",
    "Маленький крок щодня — і за місяць ти не впізнаєш себе.",
]
JOKES = [
    "Баг — це не помилка, а фішка!",
    "Чому програмісти люблять темну тему? Світло притягує баги!",
]


def get_response(user_text):
    text = user_text.lower()

    if "привіт" in text:
        return random.choice(GREETINGS)
    if "як справи" in text:
        return "Працюю без перерв, а в тебе як?"
    if "мотив" in text:
        return random.choice(MOTIVATION)
    if "жарт" not in text:
        return "Цього я ще не вмію. Навчи мене"
    return random.choice(JOKES)


def main():
    print(f"{NAME}: Привіт! Я твій {STYLE} помічник.")
    print("(напиши «вихід», щоб завершити)")
    while True:
        user_text = input("Ти : ")

        if user_text.lower() == "вихід":
            print(f"{NAME}: Чао-Какао!")
            break
        print(f"{NAME}:  {get_response(user_text)} ")


if __name__ == "__main__":
    main()

#Кінець Програмипрти
