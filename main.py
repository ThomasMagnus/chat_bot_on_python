import random
import nltk

def random_num(arr):
    return random.choice(arr)

BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': ['привет', 'hello', 'здравствуйте', 'hi'],
            'answers': ['Привет!', 'Здравствуйте', 'Здравствуй', 'Hi', 'Ну привет']
        },
        'bye': {
            'examples': ['пока', 'by', 'до свидания', 'прощай'],
            'answers': ['Пока', 'До свидания', 'Прощайте', 'Увидимся', 'До встречи']
        }
    },
    'default_phrases': ['Не совсем понимаю вас', 'Я всего лишь бот и пока не всё понимаю'],
}

question = input()

def filter_text(text):
    text = text.lower()
    text = [c for c in text if c in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-']
    text = ''.join(text)
    return text

def get_intent():
    answer = random_num(BOT_CONFIG['default_phrases'])
    for intents, items in BOT_CONFIG['intents'].items():
        for examples in items['examples']:
            dist = nltk.edit_distance(filter_text(examples), filter_text(answer))
            if dist/len(items['examples']) > 0.5:
                answer = random_num(items['examples'])
                return answer
    return answer

def return_answer():
    print(get_intent())


while True:
    print(get_intent())
    if get_intent() in BOT_CONFIG['intents']['bye']['examples']:
        break
    question = input()
