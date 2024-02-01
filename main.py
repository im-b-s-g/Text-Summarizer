import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = " Stop words are a set of commonly used words in a language. Examples of stop words in English are “a,” “the,” “is,” “are,” etc. Stop words are commonly used in Text Mining and Natural Language Processing (NLP) to eliminate words that are so widely used that they carry very little useful information. In order to remove stop words from the text in python, we have to use from nltk. corpus import stopwords and then create an object of stopwords by passing language as a parameter in stopwords. words(). Now this object is nothing but the list of all possible stop words in the language you mentioned"

def summarizer(raw):
    stopwords = list(STOP_WORDS)
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(raw)

    tokens = [token.text for token in doc]
    word_freq = {}

    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] =1
            else:    
                word_freq[word.text]+=1

    max_freq = max(word_freq.values())

    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq


    sent_tokens = [sent for sent in doc.sents ]
    sent_scores={}


    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent]=word_freq[word.text]
                else:
                    sent_scores[sent]+=word_freq[word.text]


    select_len = int(len(sent_tokens)*0.4)
    summary = nlargest(select_len, sent_scores, key= sent_scores.get)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)

    return summary,doc
