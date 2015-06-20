from django.contrib import admin

# Register your models here.

from .models import Paper, Review, KeywordAnalysis, StatusChangeEvent

admin.site.register(Paper)
admin.site.register(Review)
admin.site.register(KeywordAnalysis)
admin.site.register(StatusChangeEvent)
