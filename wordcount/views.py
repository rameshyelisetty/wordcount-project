from django.http import HttpResponse
from django.shortcuts import render

def myhome(request):
    return render(request, 'home.html', {'var1': "this is my first variable"})

def aboutpage(request):
    return render(request, 'aboutus.html', {'title': "About Us"})

def count(request):
    fulltext = request.GET['fulltext']
    word_list = fulltext.split()
    word_stats = {}
    for word in word_list:
        if word not in word_stats:
            word_stats[word] = 0
        else:
            word_stats[word] += 1

    return render(request, 'count.html', {'myfulltext': fulltext, 'wordcount':len(word_list), 'wordstats': word_stats.items(),})
