from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
	return render(request, 'home.html', {'hithere':'this is me'})

def count(request):
	fulltext = request.GET['fulltext']
	wordlist = fulltext.split()
	worddict = dict()

	for word in wordlist:
		if word in worddict:
			# increase
			worddict[word] += 1
		else:
			# add the word
			worddict[word] = 1
	sortedwords = sorted(worddict.items(), key = operator.itemgetter(1), reverse = True)

	return render(request, 'count.html', {'fulltext' : fulltext, 'count': len(wordlist), 'worddict' : sortedwords, 'wordlist' : worddict.items() })

def aboutpage(request):
	return render(request, 'about.html')
