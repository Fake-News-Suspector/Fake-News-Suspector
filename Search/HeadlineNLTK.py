import nltk
headline = "Stepen Hawking, did not Died :Fake or Real"
words = nltk.word_tokenize(headline)
print(words) #Generally splits sentences into words with advance regex ,also seperates punctuations as seperate words eg. "Mr. Jack & Ms. Jill"-> (Mr.,Jack,&,Ms.,Jill)
print(nltk.wordpunct_tokenize(headline)) #More advanced word splitting with punctuation eg. "Mr. Jack & Ms. Jill"-> (Mr,.,Jack,&,Ms,.,Jill)
print(nltk.pos_tag(words))#Provides word a category refer categories listed below
token = nltk.wordpunct_tokenize(headline)

news_keywords=[token for token, pos in nltk.pos_tag(nltk.word_tokenize(headline)) if pos.startswith('N') or pos.startswith('J') or pos.startswith('V') or pos.startswith('R')]
##for i in range(0,length):
##    if tagged[i][1][0] in ('NNP','VBD','VB','NN','NNS','NNPS','JJ','JJR','JJS','RB'):
##        news_keywords.append(tag[i][0])
print(news_keywords)    
##def entities(headline):
##    return ne_chunk(pos_tag(word_tokenize(headline))) #More advance categorizing (eg. also gives whether persson name, organization etc)
##tree = entities("Adult-film star offers to pay back alleged Trump affair hush money: letter")
##tree.pprint()
##tree.draw() #To visualize splitting of word and category
"""
CATEGORIES
POS tag list:

CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when"""
