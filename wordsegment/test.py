# coding: utf-8
import wordsegment
with open('vn_unigrams.txt') as reader:
    lines = (line.split('\t') for line in reader)
    result = dict()
    for word, number in lines:
        result[word] = float(number)
wordsegment.unigram_counts = result
with open('vn_bigrams.txt') as reader:
    lines = (line.split('\t') for line in reader)
    result = dict()
    for word, number in lines:
        result[word] = float(number)
        
wordsegment.bigram_counts = result
print wordsegment.segment("phimnguoilon")
