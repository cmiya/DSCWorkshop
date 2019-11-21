
# coding: utf-8

# In[224]:

import nltk

#Load text from a text file

f1 = open('/Users/chelseamiya/Desktop/Sondland.txt')
f2 = open('/Users/chelseamiya/Desktop/Yovanovitch.txt')


# In[267]:

#Create a FUNCTION to tokenize texts

def tokenize(text):
    from nltk.tokenize import word_tokenize
    tokenized_word=word_tokenize(text.read())
    return nltk.Text(tokenized_word)


# In[211]:

#Create a FUNCTION to remove punctuation:

def clean_up(text):
    
    #Call Tokenize FUNCTION
    text2 = tokenize(text)

    #Create a empty "list" (like a bin) to put the words in
    clean_text = []
    #For each word that contains only numbers or letters, add it to the list
    for word in text2:
        if word.isalpha():
            clean_text.append(word)

    #Print the contents of our (now full) list
    return clean_text

    #Print the length of items in the list
    #print(len(clean_text))


# In[226]:

#Create a FUNCTION to calculate lexical diversity

def lexical_diversity(text):

    textWords = []
    
    text2 = tokenize(text)
    
    for word in text2:
        if word.isalpha():
            textWords.append(word)

    return len(set(word.lower() for word in textWords)) / len(textWords)


# In[212]:

#Create a FUNCTION to filter Stop Words

def filter_stop(text):
    from nltk.corpus import stopwords
    stop_words=set(stopwords.words("english"))
    #print(stop_words)
    
    filtered_text=[]
    final = clean_up(text)
    for w in final:
        if w not in stop_words:
            filtered_text.append(w)
    
    return filtered_text
    print(len(filtered_text))


# In[213]:

#Create a FUNCTION to calculate Word Frequency

def word_frequency(text):
    
    from nltk.probability import FreqDist
    filter2 = filter_stop(text)
    fdist = FreqDist(filter2)
    #print(fdist)
    
    # Frequency Distribution Plot
    import matplotlib.pyplot as plt
    fdist.plot(30,cumulative=False)
    return plt.show()


# In[214]:

#Call FUNCTION

word_frequency(f1)


# In[215]:

#Call FUNCTION

word_frequency(f2)


# In[216]:

#Create a FUNCTION to calculate concordance

def word_concord(text, word):
    text2 = tokenize(text)
    text2.concordance(word)


# In[217]:

#Create a FUNCTION to find words that appear in similar contexts

def word_similar(text, word):
    text2 = tokenize(text)
    text2.similar(word)


# In[218]:

#Load text from a text file
f1 = open('/Users/chelseamiya/Desktop/Sondland.txt')
f2 = open('/Users/chelseamiya/Desktop/Yovanovitch.txt')

#CALL FUNCTION

word_similar(f2, 'Trump')


# In[220]:

#Load text from a text file
f1 = open('/Users/chelseamiya/Desktop/Sondland.txt')
f2 = open('/Users/chelseamiya/Desktop/Yovanovitch.txt')

#CALL FUNCTION

word_concord(f2, 'Trump')


# In[221]:

f1 = open('/Users/chelseamiya/Desktop/Sondland.txt')
f2 = open('/Users/chelseamiya/Desktop/Yovanovitch.txt')

#Compare Lexical Dispersion Plot

tokenize(f1).dispersion_plot(["Trump", "Ukraine", "Russia", "I"])
tokenize(f2).dispersion_plot(["Trump", "Ukraine", "Russia", "I"])


# In[230]:

#Parts of Speech Tagging

#Load text from a text file
f1 = open('/Users/chelseamiya/Desktop/Sondland.txt')
f2 = open('/Users/chelseamiya/Desktop/Yovanovitch.txt')

nltk.pos_tag(tokenize(f1))


# In[299]:

#Load text from a text file
f1 = open('/Users/chelseamiya/Desktop/Sondland.txt')
f2 = open('/Users/chelseamiya/Desktop/Yovanovitch.txt')

import nltk, re, pprint
from nltk import word_tokenize

text = f2

#Tag text using 12 universal POS tags
tok = tokenize(text)
new2 = nltk.pos_tag(tok, tagset='universal')
#print(new2)

#Extract POS and add to list
final = []
for word, pos in new2:
    #print(word, pos)
    final.append(pos)
#print(final)

#Join list into single string
final2 = ' '.join(final)
#print(final2)

#Count POS
from collections import Counter
count = Counter([pos for word,pos in new2])
print(count)

#Calculate POS as percentage of total words

#f2 = open('/Users/chelseamiya/Desktop/Yovanovitch.txt')

textWords = []
    
for word in tok:
    if word.isalpha():
        textWords.append(word)

tot_words = len(textWords)
print(tot_words)

NOUN = count['NOUN']/tot_words
VERB = count['VERB']/tot_words
ADP = count['ADP']/tot_words
DET = count['DET']/tot_words
PRON = count['PRON']/tot_words
ADJ = count['ADJ']/tot_words
ADV = count['ADV']/tot_words
CONJ = count['CONJ']/tot_words
PRT = count['PRT']/tot_words
NUM = count['NUM']/tot_words
X = count['X']/tot_words
print("Nouns: "+"{:.0%}".format(NOUN));
print("Verbs: "+"{:.0%}".format(VERB));
print("Adpositions: "+"{:.0%}".format(ADP));
print("Determiners: "+"{:.0%}".format(DET));
print("Pronouns: "+"{:.0%}".format(PRON));
print("Adverbs: "+"{:.0%}".format(ADV));
print("Adjectives: "+"{:.0%}".format(ADJ));
print("Conjunctions: "+"{:.0%}".format(CONJ));
print("Particles: "+"{:.0%}".format(PRT));
print("Numbers: "+"{:.0%}".format(NUM));
print("Other: "+"{:.0%}".format(X));


# In[311]:

def pos_profile(text):

    import nltk, re, pprint
    from nltk import word_tokenize

    #Tag text using 12 universal POS tags
    tok = tokenize(text)
    new2 = nltk.pos_tag(tok, tagset='universal')
    #print(new2)

    #Extract POS and add to list
    final = []
    for word, pos in new2:
        #print(word, pos)
        final.append(pos)
    #print(final)

    #Join list into single string
    final2 = ' '.join(final)
    #print(final2)

    #Count POS
    from collections import Counter
    count = Counter([pos for word,pos in new2])
    print(count)

    #Calculate POS as percentage of total words

    #f2 = open('/Users/chelseamiya/Desktop/Yovanovitch.txt')

    textWords = []

    for word in tok:
        if word.isalpha():
            textWords.append(word)

    tot_words = len(textWords)
    print(tot_words)

    NOUN = count['NOUN']/tot_words
    VERB = count['VERB']/tot_words
    ADP = count['ADP']/tot_words
    DET = count['DET']/tot_words
    PRON = count['PRON']/tot_words
    ADJ = count['ADJ']/tot_words
    ADV = count['ADV']/tot_words
    CONJ = count['CONJ']/tot_words
    PRT = count['PRT']/tot_words
    NUM = count['NUM']/tot_words
    X = count['X']/tot_words
    print("Nouns: "+"{:.0%}".format(NOUN));
    print("Verbs: "+"{:.0%}".format(VERB));
    print("Adpositions: "+"{:.0%}".format(ADP));
    print("Determiners: "+"{:.0%}".format(DET));
    print("Pronouns: "+"{:.0%}".format(PRON));
    print("Adverbs: "+"{:.0%}".format(ADV));
    print("Adjectives: "+"{:.0%}".format(ADJ));
    print("Conjunctions: "+"{:.0%}".format(CONJ));
    print("Particles: "+"{:.0%}".format(PRT));
    print("Numbers: "+"{:.0%}".format(NUM));
    print("Other: "+"{:.0%}".format(X));


# In[314]:

f1 = open('/Users/chelseamiya/Desktop/Sondland.txt')
f2 = open('/Users/chelseamiya/Desktop/Yovanovitch.txt')
pos_profile(f1)


# In[315]:

#Load text from a text file
f1 = open('/Users/chelseamiya/Desktop/Sondland.txt')
f2 = open('/Users/chelseamiya/Desktop/Yovanovitch.txt')

pos_profile(f2)


# In[ ]:



