import pymorphy3
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='auto', target='en')
morph = pymorphy3.MorphAnalyzer()

dc = {}

with open('dialog.txt', encoding='utf-8') as f:
    lines = f.read().splitlines()

for line in lines:
    words = line.split()
    for word in words:
        normal_form = morph.parse(word)[0].normal_form
        dc[normal_form] = dc.get(normal_form, 0) + 1

with open('result.txt', 'w', encoding='utf-8') as file:
    file.write('Исходное слово | Перевод | Количество упоминаний\n')
    for word, count in sorted(dc.items(), key=lambda item: item[1], reverse=True):
        translation = translator.translate(word)
        file.write(f'{word} | {translation} | {count}\n')
