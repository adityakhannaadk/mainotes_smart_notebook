import syntactics

def bigramsplit(text):
    bigrams = []
    split = text.split(" ")
    i = 0
    while i < len(split):
        bigrams.append(split[i-1]+" "+split[i])

        i = i+1
    return bigrams
def syntactic_bigram(answer,text):
    bigram_syntactic = bigramsplit(text)
    to_sum = []
    i = 0
    while i < len(bigram_syntactic):
        to_sum.append(syntactics.syntactic(answer,bigram_syntactic[i]))
        i = i + 1
    return str(sum(to_sum)/len(to_sum))

def mark(text1,text2,marks):
     return round(syntactic_bigram(text1,text2)*marks)

