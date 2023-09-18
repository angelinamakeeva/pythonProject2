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