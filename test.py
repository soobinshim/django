import googletrans
from googletrans import Translator
 
d = googletrans.LANGUAGES
 
text1 = "안녕하세요"
translator = Translator()

for i in d:
    trans1 = translator.translate(text1, src='ko', dest=i)
    print(f"{d.get(i)}의 인삿말: ", trans1.text)
