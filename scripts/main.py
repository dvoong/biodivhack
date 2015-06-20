import csv
from biodivhack.models import Paper

filepath = '/home/dvoong/biodatahack/virtualenv/biodivhack/predicts.csv'

f = open(filepath)
reader = csv.DictReader(f)

for row in reader:
    paper = Paper.objects.get(title=row['Source_title'])
    print paper
