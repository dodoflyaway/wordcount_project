from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    #return HttpResponse('hello')
    return render(request,'home.html',{'annoucment':'content available'})

#def cuku(request):
#    return HttpResponse("you found the cukus eggs")

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    word_dict = dict()
    for word in wordlist:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    sortedwords = sorted(word_dict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'dictionary':sortedwords})

def aboutt(request):
    return render(request,'about.html')
