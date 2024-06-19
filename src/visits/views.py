from django.shortcuts import render
from .models import Visit
def all_visits(request):
    template = 'visits_list.html'
    path = request.path
    Visit.objects.create(path=path)
    context = {
        "queryset": Visit.objects.all(),
        "title": "Visits List"
    }
    return render(request ,template, context)
