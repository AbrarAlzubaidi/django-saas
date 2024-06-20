from django.shortcuts import render
from .models import Visit
def all_visits(request):
    template = 'visits_list.html'
    path = request.path
    Visit.objects.create(path=path)
    context = {
        "queryset": Visit.objects.all().count(),
        "title": "Visits List",
        "page": path,
        "total_visit_per_page": Visit.objects.filter(path=path).count()
    }
    return render(request ,template, context)
