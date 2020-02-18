import pymorphy2
from string import punctuation
import operator


morph = pymorphy2.MorphAnalyzer()

#task 1
text = open('textforlesson3.txt', 'r', encoding='utf-8')
text = text.read()
#task2
punctuation += "—»«"
text.replace('-', ' ')
cleanText = ''.join(x for x in text if x not in punctuation)

wordlist = cleanText.split()


wordlist = list(map(lambda x: x.lower(), wordlist))

for i in range(len(wordlist)):
    lemma = morph.parse(wordlist[i])[0]
    print(wordlist[i], ' - ', lemma.normal_form) #вывести слово и его лемму, на повторения не обращаем внимания
#task 3
word_dic = {}

for i in range(len(wordlist)):
    word_dic[wordlist[i]] = wordlist.count(wordlist[i])

x = word_dic
word_dic = sorted(x.items(), key=operator.itemgetter(1), reverse= True)
#task 4
for i in range(5):
    print(word_dic[i])
