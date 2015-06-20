import os, sys, random
import django
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from biodivhack.models import Paper, Review, StatusChangeEvent

def index(request):
    papers = Paper.objects.all()[:100]
    for paper in papers:
        reviews = Review.objects.filter(paper=paper)
        paper.reviews = reviews
        paper.score = random.randrange(1, 100)
        status = StatusChangeEvent.objects.filter(paper=paper)[len(StatusChangeEvent.objects.filter(paper=paper)) - 1]
        paper.status = status.status
    papers = list(reversed(sorted(papers, key=lambda x: x.score)))
    context = {
        'papers': papers
        }
    
    return render(request, 'biodivhack/index.html', context)

def keyword_summary(request, paper_id):
    paper = Paper.objects.get(id=paper_id)
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud
    text = paper.abstract
    wordcloud = WordCloud().generate(text)
    dirpath = settings.BASE_DIR + '/biodivhack/static/biodivhack/{}'.format(paper_id)
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
        filepath = settings.BASE_DIR + '/biodivhack/static/biodivhack/{}/wordcloud.png'.format(paper_id)
        if not os.path.exists(filepath):
            wordcloud.to_file(filepath)
    url = settings.STATIC_URL + '/biodivhack/{}/wordcloud.png'.format(paper_id)
    return HttpResponse(paper.abstract + '<br /><img src="{}"></img>'.format(url))


def review(request, paper_id, review_id):
    paper = Paper.objects.get(id=paper_id)
    review = Review.objects.get(id=review_id)
    context = {
        'paper': paper,
        'review': review,
        }
    return render(request, 'biodivhack/review.html', context)

def status(request, paper_id):
    paper = Paper.objects.get(id=paper_id)
    statuses = StatusChangeEvent.objects.filter(paper=paper)
    context = {'statuses': statuses}
    return render(request, 'biodivhack/statuses.html', context)

def add_to_database(request):
    return HttpResponse("Nice! Added to the database")
