from django.http import HttpResponse
from django.template import loader

from .models import Competition, CompetitionCategory

def home(request):
    competitions = Competition.objects.all()
    template = loader.get_template('competitions/home.html')
    context = {
        'competitions': competitions
    }

    return HttpResponse(template.render(context, request ))

# Create your views here.
def index(request):
    competitions = Competition.objects.all()
    template = loader.get_template('competitions/index.html')
    context = {
        'competitions': competitions
    }

    return HttpResponse(template.render(context, request ))

def show(request, id):
    competition = Competition.objects.get(pk=id)
    competition_categories = CompetitionCategory.objects.filter(competition_id=id)
    template = loader.get_template('competitions/show.html')
    context = {
        'competition': competition,
        'competition_categories': competition_categories
    }

    return HttpResponse(template.render(context, request))

def register(request, id):
    template = loader.get_template('competitions/register.html')

    return HttpResponse(template.render({}, request))
