from django.shortcuts import render, get_object_or_404
from .models import Job
# Create your views here.
def home(requset):
    jobs = Job.objects.all()
    return render(requset, 'jobs/home.html', {'jobs':jobs})

def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job': job_detail })

def login(request):
    return render(request, 'jobs/login.html')