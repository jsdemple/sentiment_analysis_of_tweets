"""VADER tutorial from nltk website"""
"""Citation for VADER: 
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
    Sentiment Analysis of Social Media Text. Eighth International Conference on
    Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014."""

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

"""EXAMPLE DATA"""
sentences = ["VADER is smart, handsome, and funny.", # positive sentence example
"VADER is smart, handsome, and funny!", # punctuation emphasis handled correctly (sentiment intensity adjusted)
"VADER is very smart, handsome, and funny.",  # booster words handled correctly (sentiment intensity adjusted)
"VADER is VERY SMART, handsome, and FUNNY.",  # emphasis for ALLCAPS handled
"VADER is VERY SMART, handsome, and FUNNY!!!",# combination of signals - VADER appropriately adjusts intensity
"VADER is VERY SMART, really handsome, and INCREDIBLY FUNNY!!!",# booster words & punctuation make this close to ceiling for score
"The book was good."]       # positive sentence

tricky_sentences = [
"Most automated sentiment analysis tools are shit.",
"VADER sentiment analysis is the shit.",
"Sentiment analysis has never been good.",
"Sentiment analysis with VADER has never been this good.",
"Warren Beatty has never been so entertaining.",
"I won't say that the movie is astounding and I wouldn't claim that the movie is too banal either."]

paragraph = "It was one of the worst movies I've seen, despite good reviews. Unbelievably bad acting!! Poor direction. VERY poor production. The movie was bad. Very bad movie. VERY bad movie. VERY BAD movie. VERY BAD movie!"

"""TOKENIZE SENTS AND COMBINE DATA LISTS"""
lines_list = tokenize.sent_tokenize(paragraph)
sentences.extend(lines_list)

"""SENTIMENT ANALYSIS"""
sid = SentimentIntensityAnalyzer()

for sentence in sentences:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print ()



