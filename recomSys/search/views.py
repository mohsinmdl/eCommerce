from django.shortcuts import render
from django.views.generic import ListView


def predictView(request):
    return render(request, "search/view.html", {})