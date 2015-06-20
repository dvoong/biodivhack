import datetime
import django
from django.db.models import Model, CharField, URLField, ForeignKey, IntegerField, DateField

class Paper(Model):
    title = CharField(max_length=100)
    abstract = CharField(max_length=10000)
    url = URLField()
    status = CharField(max_length=100, default="Unreviewed")
    doi = CharField(max_length=100)
    def __str__(self):
        return self.title

class Review(Model):
    reviewer = CharField(max_length=100)
    paper = ForeignKey(Paper)
    notes = CharField(max_length=1000)
    date = DateField()
    def __str__(self):
        return 'Review: {}'.format(self.paper.title)

class KeywordAnalysis(Model):
    keyword = CharField(max_length=100)
    count = IntegerField()
    paper = ForeignKey(Paper)
    def __str__(self):
        return 'Review: {}'.format(self.paper.title)

class StatusChangeEvent(Model):
    author = CharField(max_length=100)
    paper = ForeignKey(Paper)
    notes = CharField(max_length=1000)
    date = DateField(default=datetime.datetime.now())
    status = CharField(max_length=100, default="Unreviewed")
    
