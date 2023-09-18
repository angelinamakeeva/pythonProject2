#Makeeva Angelina 85%



from textblob import TextBlob
import nltk
import re
nltk.download('punkt')
text ="And convergence generally worked the way economists long thought it would. In China, low-wage manufacturing of cheap goods for export eventually evolved into the production of more sophisticated goods and services, as workers and firms accumulated knowledge and experience."
textblob = TextBlob(text)
glas = 'ауоыэяюёиеАУОЫЭЯЮЁИЕ'
glasen = "AEIOUYaeiouy"
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

print('Предложений: ', sentences)
print('Слов: ', words)
print('Слогов: ', slogi)
print('Средняя длина предложения в словах: ', total_len_by_words)
print('Средняя длина слова в слогах: ', total_len_by_slogi)
flash_ru = 206.835 - (1.3*(words/sentences))-(60.1*(slogi/words))
print('Индекс удобочитаемости Флеша: ', flash_ru)

if flash_ru > 80.0 :
  print("Текст очень легко читается (для младших школьников).")
if flash_ru > 50.0 and flash_ru < 80.0 :
  print("Простой текст(для школьников).")
if flash_ru > 25.0 and flash_ru < 50.0 :
  print("Текст немного трудно читать (для студентов).")
if flash_ru <= 25.0 :
  print("Текст трудно читается (для выпускников ВУЗов).")

pol = textblob.polarity
if pol  == 0.0  or pol < 0.3:
  print("Тональность текста: ",'нейтральная')
if pol < 0.0 :
  print("Тональность текста: ",'негативная')
if pol > 0.3 :
  print("Тональность текста: ",'позитивная')