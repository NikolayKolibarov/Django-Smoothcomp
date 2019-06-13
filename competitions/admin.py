from django.contrib import admin

from .models import Competition, CompetitionCategory

# Register your models here.
admin.site.register(Competition)
admin.site.register(CompetitionCategory)
