from nltk.corpus import stopwords
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import datetime
# nltk.download('punkt')
# pickle
stemmer = nltk.stem.porter.PorterStemmer()
#from stemming.porter2 import stem
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)


def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]


def normalize(text):
    return stem_tokens(
        nltk.word_tokenize(
            text.lower().translate(remove_punctuation_map)))


vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')


# Load library

# You will have to download the set of stop words the first time
nltk.download('stopwords')

# Load stop words
stop_words = stopwords.words('english')


def sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0, 1]


def search_1(threshold, searchlist, searchquery):
    finalist = []
    x = 0
    while(x < len(searchlist)):
        if(sim(searchquery, searchlist[x])):
            finalist.append(searchlist[x])
        x = x + 1
    return finalist


def stem_all(sentence):
    documents = [[stem(word) for word in sentence.split(" ")]].join * (" ")


def remove_stop(sentence):
    sentence = [word for word in sentence.split(
        " ") if word not in stop_words].join(" ")
    return sentence


def append_if_not(list1, list2):
    final = []
    for item in list2:
        if(item not in list1):
            final.append(item)
        else:
            pass
    return final

# Finding further links between


def clump(notes, search_t):
    ret_docs = []
    docs = search_1(0.4, notes, search_t)
    for doc in docs:
        ret_docs.extend(append_if_not(ret_docs, search_1(0.6, notes, doc)))

    return ret_docs


def search_final(threshold, searchlist, searchquery):
    x = 0
    finalist = clump(searchlist, searchquery)

    finalist.insert(0, " Matching notes to {} \n".format(searchquery))
    return " ".join(finalist)

    # Search suggestions and predictions, todo for layer
