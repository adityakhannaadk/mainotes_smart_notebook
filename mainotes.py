#Search algorithm
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer

#nltk.download('punkt')
# pickle
stemmer = nltk.stem.porter.PorterStemmer()
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)


def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]


def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))


vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')


def sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0, 1]

def search(threshold,searchlist,searchquery):
  finalist = []
  x = 0
  while(x < len(searchlist)):
        if(sim(searchquery,searchlist[x])):
          finalist.append(searchlist[x])
        x = x + 1  
  finalist.insert(0," Matching notes to {} \n".format(searchquery))        
  return " ".join(finalist)

#Predict and suggest algorithm (ongoing, not ready to release)


