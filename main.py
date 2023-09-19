#Makeeva Angelina 85%
#Kareva Alena 70%
#Osokina Anastasya 80%

import ru_local as ru
from textblob import TextBlob
import nltk
import re
nltk.download('punkt')
text = input(ru.text)
glas = ru.ru_vowels
glasen = ru.en_vowels
slogi = 0

def sent_count(text):
  total_words = 0
  new_text = re.sub(r'[.!?]\s', r'|', text)
  text_for_count = new_text.split('|')
  sent_num = len(new_text.split('|'))
  for i in range (sent_num):
    total_words += len(TextBlob(text_for_count[i]).words)

  return sent_num,total_words


words = len(TextBlob(text).words)
sentences = sent_count(text)[0]
total_words = sent_count(text)[1]
total_len_by_words = total_words / sentences



for i in TextBlob(text).words:
  counter = 0
  for k in range (len(i)):
    if i[k] in glas or i[k] in glasen:
      counter+=1
  slogi += counter

total_len_by_slogi = slogi / total_words

count_symb = 0
summ = 0
for i in text:
  count_symb += 1
  n = str(i)
  summ += ord(n)
sr = summ/count_symb

detect_language = 0
if sr < 800:
  detect_language = 'en'
else:
  detect_language = 'ru'


if detect_language == 'en':
  flash_en = 206.835 - (1.015 * (words / sentences)) - (84.6 * (slogi / words))
if detect_language == 'ru':
  flash_ru = 206.835 - (1.3 * (words / sentences)) - (60.1 * (slogi / words))


print(ru.sentence, sentences)
print(ru.words, words)
print(ru.syllables, slogi)
print(ru.sr_word, total_len_by_words)
print(ru.sr_syllables, total_len_by_slogi)
if detect_language == 'en':
  print(ru.flash, flash_en)
  if flash_en > 80.0:
    print(ru.easy)
  if flash_en > 50.0 and flash_en <=80.0:
    print(ru.simple)
  if flash_en > 25.0 and flash_en <= 50.0 :
    print(ru.difficult)
  if flash_en <= 25.0 :
    print(ru.hard)
else:
  print(ru.flash, flash_ru)
  if flash_ru > 80.0:
    print(ru.easy)
  if flash_ru > 50.0 and flash_ru <= 80.0:
    print(ru.simple)
  if flash_ru > 25.0 and flash_ru <= 50.0 :
    print(ru.difficult)
  if flash_ru <= 25.0 :
    print(ru.hard)
