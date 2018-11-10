from django.shortcuts import render

# Create your views here.


def predictView(request):
    return render(request, "predictor/predictor.html", {})