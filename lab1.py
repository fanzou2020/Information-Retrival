import nltk
from nltk.corpus import reuters
nltk.download("reuters")

len(reuters.fileids())  # number of documents

reuters.raw("training/9920")  # raw text of file "training/9920"


from nltk import word_tokenize
nltk.download("punkt")  # 
text = reuters.raw("training/9920")
word_tokenize(text)  # word tokenizer
len(word_tokenize(text))  # 69 words

from nltk import sent_tokenize
sent_tokenize(text)  # sentence tokenizer
len(sent_tokenize(text))  # 3 sentences

# tokens to terms (unique tokens)
len(set(word_tokenize(text)))  # 54 unique tokens

# todo: find how many prepositions are there in the tokens
prepositions = ["about", "beside", "near", "to", "above", "between", "of", "towards", "across", "beyond", "off", "under", "after", "by", "on", "underneath", "against", "despite", "onto", "unlike", "along", "down", "opposite", "until", "among", "during", "out", "up", "around", "except", "outside", "upon", "as", "for", "over", "via", "at", "from", "past", "with", "before", "in", "round", "within", "behind", "inside", "since", "without", "below", "into", "than", "beneath", "like", "through"]

from nltk import pos_tag
nltk.download("averaged_perceptron_tagger")
tokens = word_tokenize(text)
pos_tag(tokens)  # tag each tokens
# "TO" and "IN" means prepositions
# VB -> verb, VBD -> past sense of verb

reuters.categories()

files_each_categories = []
for category in reuters.categories():
    files_each_categories.append(reuters.fileids(category))
    print(reuters.fileids(category))

reuters.raw("training/9920").count('to')

def word_freq(word, fileid):
    return reuters.raw(fileid).count(word)
    
word_freq('to', 'training/9920')
reuters.raw('training/9920')
