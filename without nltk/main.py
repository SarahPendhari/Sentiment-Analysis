import string
from collections import Counter
import matplotlib.pyplot as pt
#Opening the file sd 
text = open('sd.txt', encoding='utf-8').read()
#Convert everything to lowercase
lower_case = text.lower()
#removing punctuations
clean_data = lower_case.translate(str.maketrans('','',string.punctuation))
#print(clean_data)
#Tokenisation basically means separating words form a sentence and storing them in a list
tokenzised_words = clean_data.split()
#print(tokenzised_words)
#stop words: don't add any emotion or have any significance in emotional analysis
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []
for i in tokenzised_words:
    if i not in stop_words:
        final_words.append(i)
        
#print(final_words)
emotions_list = []
with open('emotions.txt','r') as file:
    #i represents line yaha pe
    for i in file:
        compact_line = i.replace("\n","").replace(",","").replace("'","").strip()   #strip : word ke pehle wala space nikal ne ke liye
        #print(compact_line)
        #splitting: word before ':' goes into word and after ':' goes into emotion
        word,emotion = compact_line.split(':')
        #print("Word: " + word +"  "+ "Emotion: " + emotion)
        
        if word in final_words:
            emotions_list.append(word)
            
#print(emotions_list)
c = Counter(emotions_list)
#print(c)
fig, ax = pt.subplots()
ax.bar(c.keys(),c.values())
fig.autofmt_xdate()
pt.savefig('graph.png')
pt.show()