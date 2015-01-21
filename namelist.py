import nltk
from nltk.corpus import names

labeled_names = ([(name, 'male') for name in names.words('male.txt')] + 
				 [(name, 'female') for name in names.words('female.txt')])
print len(labeled_names)
type(names)
labeled_names[3311]
s = sorted(names.words('male.txt') + names.words('female.txt'))

for i in range(len(s)) :
	if i > 1 and s[i] == s[i-1] :
		print 'yes'
