# CS 111
# Final Project
# Matthew Pohlhaus
# PARTNER: Rob Haversat: rhaver@bu.edu

import math

# Clean Text Function
def clean_text(txt):
    '''takes a string 'txt' as input and "cleans" it by returning it in a form
of a list of the words in the string separated word by word in lowercase with
punctuation removed--helper function for add_string method'''
    txt = txt.lower().replace("'", '')
    symbols = """ , / ? > < : ; ' " - _ ) ( * & ^ % $ # @ ! ~ . """.split()
    for i in range(len(txt)):
        if txt[i] in symbols:
            txt = txt.replace(txt[i], " ")
    txt1 = txt.split()
    return txt1

# File Writing Function
def file_write(filename, d):
    '''creates a file to save a dictionary 'd'--serves as a helper function for
save_model method--inspired by sample_file_write example function'''
    f = open(filename, 'w')
    f.write(str(d))
    f.close()

# Stems Helper Function
def stem(s):
    '''takes a single word string as input and returns the 'stem' of that word
determined by a multitude of possible cases'''
    if len(s) <= 1:
        s = s
    elif s[(len(s) - 4): len(s)] == 'ying' and s[-5] in 'aeiouAEIOU':
        s = s[:(len(s) - 3)]
    elif len(s) > 4 and s[(len(s) - 4)] == 'y' and s[(len(s) - 3): len(s)] == 'ing':
        s = s[:(len(s) - 4)]
    elif s[(len(s) - 3):] == 'ing':
        s = s[:(len(s) - 3)]
    elif s[(len(s) - 3):] == 'ier':
        s = s[:(len(s) - 3)]
    elif s[-1] == 'e':
        s = s[:-1]
    elif s[-1] == 'y' and s[-2] not in 'aeiouAEIOU':
        s = s[:-1]
    elif s[-1] == 'y' and s[-2] in 'aeiouAEIOU':
        s = s
    elif s[(len(s) - 2):] == 'ed':
        s = s[:(len(s) - 2)]
    elif s[-1] == 's':
        s = stem(s[:-1])
    return s

# Finding Sentences
def sentences(s):
    '''helper function for sentence_lengths attribute. Splits the input string 's'
by their sentence ending punctuations and returns a list of a length corresponding
to the respective length for each sentence within the inputted string'''
    lengths = []
    s = s.replace('?', '.')
    s = s.replace('!', '.')
    s = s.split('.')
    for i in s:
        if i != '':
            i = i.split(' ')
            lengths += [len(i)]
        else:
            lengths = lengths
    return lengths

# Lists for Numerical Values for Stems
def stems_list(lst):
    '''a helper function used for calculating stems and converting them into
dictionary keys for use with calculating their frequencies within the model'''
    stems = [0] * len(lst)
    for i in range(len(stems)):
        stems[i] = stem(lst[i])
    return stems

# Finding Quotes
def quotes(s):
    '''a helper function for out 'quotes' attribute--takes a string as an input
and returns a list of the lengths of sentences or phrases that appear in a text
in between '"' quote symbols'''
    count = 1
    test = 0
    stuff = []
    for i in range(len(s.split())):
        if s.split()[i][0] == '"' and i != (len(s.split()) - 1):
            while s.split()[i+test][-1] != '"':
                test += 1
                count += 1
            stuff += [count]
            count = 1
            test = 0
    return stuff


# Comparing Dictionaries
def compare_dictionaries(d1, d2):
    '''takes two dictionaries as inputs and returns a score based on the
contents' probability of appearing within its source based off of a version of
a Naive Bayes scoring algorithm'''
    score = 0
    total = 0
    for w in d1:
        total += d1[w]
    for w in d2:
        if w in d1:
            prob = d1[w] / total
            prob = math.log(prob) * d2[w]
            score += prob
        else:
            if total == 0:
                total = 1000000
            prob = 0.5 / total
            prob = math.log(prob) * d2[w]
            score += prob
    return score


# TextModel Object Class
class TextModel:
    # 1
    # Constructor
    def __init__(self, model_name):
        '''constructor--initializes the object and its attributes'''
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.quotes = {}

    # 2
    # String Representation
    def __repr__(self):
        '''string representation of the object from the shell'''
        s = ''
        s += 'text model name: ' + self.name + '\n'
        s += ' number of words: ' + str(len(self.words)) + '\n'
        s += ' number of lengths: ' + str(len(self.word_lengths)) + '\n'
        s += ' number of stems: ' + str(len(self.stems)) + '\n'
        s += ' number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += ' number of quote lengths: ' + str(len(self.quotes)) + '\n'
        return s

    # 3
    # Add String Method
    def add_string(self, s):
        '''takes a string 's' as input and sorts the "cleaned" version of it into
its respective dictionaries--returns a dictionary of the words used and the word-
lengths represented in 's'''
        lengths = sentences(s)
        for i in range(len(lengths)):
            if lengths[i] not in self.sentence_lengths:
                self.sentence_lengths[lengths[i]] = lengths.count(lengths[i])
        quote_stuff = quotes(s)
        for i in range(len(quote_stuff)):
            if quote_stuff[i] not in self.quotes:
                self.quotes[quote_stuff[i]] = quote_stuff.count(quote_stuff[i])
        new_txt = clean_text(s)
        for w in new_txt:
            if w not in self.words:
                self.words[w] = new_txt.count(w)
        for w in new_txt:
            if len(w) not in self.word_lengths:
                self.word_lengths[len(w)] = 1
            else:
                self.word_lengths[len(w)] += 1
        for w in stems_list(new_txt):
            if w not in self.stems:
                self.stems[w] = 1
            else:
                self.stems[w] += 1

    # 4
    # Add File Method
    def add_file(self, filename):
        '''reads a saved file and stores its word dictionaries in the object through
its add_string method'''
        file = open(filename, 'r', encoding='utf8', errors='ignore')
        text = file.read()
        text = text.replace("'", '')
        self.add_string(text)
        file.close()

    # 5
    # Save Model Method
    def save_model(self):
        '''creates and saves a file storing a TextModel object's dictionaries--
'stuff' and 'dicts' lists are used so that we can add to them later when adding
new dictionary attributes to the model in the second half of the project'''
        stuff = ['words', 'word_lengths', 'stems', 'sentence_lengths', 'quotes']
        dicts = [self.words, self.word_lengths, self.stems, self.sentence_lengths, self.quotes]
        for i in range(len(stuff)):
            file_write((self.name + '_' + stuff[i]), dicts[i])

    # 6
    # Read Model Method
    def read_model(self):
        '''accesses a file from memory and absorbs its materials into its respective
word dictionaries'''
        file = open(self.name + '_words', 'r')
        pop = file.read()
        self.words = dict(eval(pop))
        file.close()
        file2 = open(self.name + '_word_lengths', 'r')
        pop2 = file2.read()
        self.word_lengths = dict(eval(pop2))
        file2.close()
        file3 = open(self.name + '_stems', 'r')
        pop3 = file3.read()
        self.stems = dict(eval(pop3))
        file3.close()
        file4 = open(self.name + '_sentence_lengths', 'r')
        pop4 = file4.read()
        self.sentence_lengths = dict(eval(pop4))
        file4.close()
        file5 = open(self.name + '_quotes', 'r')
        pop5 = file5.read()
        self.quotes = dict(eval(pop5))
        file5.close()
        
    # 7
    # Similarity Scores
    def similarity_scores(self, other):
        '''computes and returns a LIST of log siilarity scores (obtained by
a helper function above) measuring the similarity of 'self' and 'other'--one
score for each type of feature by making repeated calls to the compare_dictionaries
method'''
        lst = []
        word_score = compare_dictionaries(other.words, self.words)
        lst += [word_score]
        word_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        lst += [word_score]
        word_score = compare_dictionaries(other.stems, self.stems)
        lst += [word_score]
        word_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        lst += [word_score]
        word_score = compare_dictionaries(other.quotes, self.quotes)
        lst += [word_score]
        return lst

    # 8
    # Classifying Texts
    def classify(self, source1, source2):
        '''compares the called TextModel object (self) and two other source
text model objects and determines which of these other text models is the more
likely source of the called model'''
        source1_score = 0
        source2_score = 0
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        for i in range(len(scores1)):
            scores1[i] = round(scores1[i], 3)
            scores2[i] = round(scores2[i], 3)
            if scores1[i] > scores2[i]:
                source1_score += 1
            elif scores1[i] == scores2[i]:
                source1_score += 0
                source2_score += 0
            else:
                source2_score += 1
        print('scores for', source1.name, ':', scores1, '\n')
        print('scores for', source2.name, ':', scores2, '\n')
        if source1_score > source2_score:
            print(self.name, 'is more likely to have come from', source1.name)
        else:
            print(self.name, 'is more likely to have come from', source2.name)
        
'''def sample_file_read(filename):
    f = open(filename, 'r')
    d_str = f.read()
    f.close()
    d = dict(eval(d_str))
    print("Inside the newly-read dictionary, d, we have: ")
    print(d)
'''
