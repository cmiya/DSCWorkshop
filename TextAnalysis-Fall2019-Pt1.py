
# coding: utf-8

# # Intro to Text Analysis
# 
# ## <font color='orange'>Workshop Description</font>
# 
# This hands-on workshop will introduce students to the basics of text analysis using Python’s Natural Language Toolkit (NLTK) library. Students will learn how to search for patterns in a text and extract and summarize information about its features. This class is designed for beginners and will especially appeal to those in humanities fields.
# 
# By the end of the workshop, students will know how to:
# 
# - Setup and install required software
# - Load a text file
# - Clean up and tokenize a text
# - Search for words in context
# - Chart word frequency
# - Tag parts-of-speech
# 
# ### Requirements:
# - Bring a laptop
# - Download the latest version of anaconda: (https://docs.anaconda.com/anaconda/install/)
# - If you already have an older version of anaconda installed, make sure to update it:  (https://docs.anaconda.com/anaconda/install/update-version/)
# 
# ### Resources:
# - Getting Started with NLTK [(online)](https://www.nltk.org/book/ch01.html)
# - Data Camp's Beginner's Guide to NLTK [(online)](https://www.datacamp.com/community/tutorials/text-analytics-beginners-nltk)
# - Markdown Cheat Sheet [(online)](https://www.markdownguide.org/cheat-sheet/)
# - Programming Historian [(online)](https://programminghistorian.org/)

# ## <font color='orange'>What is Text Analysis?</font> 
# - Searching for patterns in a text
# - Comparative
# - What makes a feature significant?

# ## <font color='orange'>What is Jupyter Notebook?</font> 
# 
# - Jupyter Notebook is a Graphic User Interface (GUI aka "gooey") that sits on top of the computer code and makes it easier to interact with.
# - Jupyter Notebook is for:
#     - a) writing and executing "live" computer code
#     - b) creating written and visual notes or commentary (like for tutorials!)
# 
# ### Using Jupyter:
# - **Cells** are boxes for entering code or text.
# - Switch between **Cell Types** using the dropdown menu:
#     - a) **Code**: e.g. Python, Java, R
#     - b) **Markdown**: create text and visual content, easy-to-read and write
#     
# ### Working with Cells
# - **Double-click** a Cell to edit it.
# - You can **Insert** Cells above or below, **Copy and Paste** Cells contents, **Move** Cells up/down, and **Delete** Cells.
# - Click **Shift + Return** to execute Cell contents (run code).
# - Click the **STOP** icon to stop (interrupt) code.

# ## <font color='orange'>Getting Started with NLTK</font>
# 
# ### Open Jupyter Notebook
# - Open Anaconda-Navigator (in Applications)
# - Under Home, click the 'Jupyter Notebook' icon to launch.

# ### Import the NLTK Library

# In[43]:

#Import the NLTK library 

import nltk
nltk.download('popular')


# ### Load Text from Text File

# In[325]:

#Load text from a text file

f1 = open('/Users/chelseamiya/Desktop/Sondland.txt')
f2 = open('/Users/chelseamiya/Desktop/Yovanovitch.txt')

#raw = f1.read()
#print(raw)


# ### Calculate number of words

# In[315]:

#Compare the length of each testimony

len(f2.read())


# ### Tokenize Words

# In[332]:

#Tokenize words

from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(raw)
print(tokenized_word)


# ### Clean up text

# In[317]:

#Remove numbers and punctuation

#Create a empty "list" (like a bin) to put the words in
clean_text = []

#For each word that contains only numbers or letters, add it to the list
for word in tokenized_word:
    if word.isalpha():
        clean_text.append(word)

#Print the contents of our (now full) list
print(clean_text)

#Print the length of items in the list
len(clean_text)


# ### Calculate lexical diversity

# In[318]:

#Calculate lexical diversity by...
#Dividing the total number of words by the number of unique words

len(set(word.lower() for word in clean_text)) / len(clean_text)


# In[328]:

#What if you want to repeat a calculation on several texts?

#Create a FUNCTION to build a tool from a block of code

def lexical_diversity(text):

    textWords = []
    
    from nltk.tokenize import word_tokenize
    tokenized_word=word_tokenize(text)
    
    for word in tokenized_word:
        if word.isalpha():
            textWords.append(word)

    return len(set(word.lower() for word in textWords)) / len(textWords)


# In[330]:

f1 = open('/Users/chelseamiya/Desktop/Sondland.txt')
f2 = open('/Users/chelseamiya/Desktop/Yovanovitch.txt')

raw = f1.read()

lexical_diversity(raw)


# ### Word Frequency

# In[188]:

from nltk.probability import FreqDist
fdist = FreqDist(clean_text)
print(fdist)


# In[189]:

fdist.most_common(2)


# In[122]:

# Frequency Distribution Plot
import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()


# ### Eliminate Stopwords

# In[123]:

from nltk.corpus import stopwords

stop_words=set(stopwords.words("english"))
print(stop_words)


# In[124]:

filtered_word=[]
for w in clean_text:
    if w not in stop_words:
        filtered_word.append(w)
print("Tokenized Sentence:",tokenized_word)
print(len(tokenized_word))

print("Filtered Sentence:",filtered_word)
print(len(filtered_word))


# ### Plot Frequency Distibution

# In[275]:

from nltk.probability import FreqDist
fdist = FreqDist(filtered_word)
print(fdist)

# Frequency Distribution Plot
import matplotlib.pyplot as plt
fdist.plot(30,cumulative=False)
plt.show()


# ### Find words in context

# In[276]:

##Find word concordance for raw text

text = nltk.Text(clean_text)
text.concordance('Trump')


# In[321]:

#Find words that appear in similar contexts

text.similar("July")


# ### Plot Lexical Dispertion
# - Compare how different words are distributed over the text

# In[143]:

text.dispersion_plot(["US", "Trump", "public", "my", "aid", "Ukraine"])


# ### Label Parts-of-Speech

# In[337]:

#Load text from a text file
f1 = open('/Users/chelseamiya/Desktop/Sondland.txt')
f2 = open('/Users/chelseamiya/Desktop/Yovanovitch.txt')

import nltk, pprint
from nltk import word_tokenize

text = f2

#Tokenize text
tokenized_word=word_tokenize(text.read())
tok = nltk.Text(tokenized_word)

#Tag text using 12 universal POS tags
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


# In[ ]:



