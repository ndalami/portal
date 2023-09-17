from django.shortcuts import redirect, render
from . models import Job,Choice
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    return render(request,'jobs/index.html')


def home(request):
    available_jobs = Job.objects.all()
    category = Choice.objects.all()

    p = Paginator(Job.objects.all().order_by('-id'),4)
    page = request.GET.get('page')
    job = p.get_page(page)
    return render(request,'jobs/home.html',{'available_jobs':available_jobs,
    'category':category,'job':job})

def detail(request, job_id):
    category = Choice.objects.all()
    job = Job.objects.get(pk=job_id)
    context ={'job':job,'category':category}
    return render(request,'jobs/detail.html',context)

def search_job(request):
    if request.method == "POST":
        searched = request.POST['searched']
        jobs = Job.objects.filter(title__contains = searched)
        context ={'searched':searched, 'jobs':jobs}
        return render(request,'jobs/search_job.html',context)
    else:
        return render(request,'jobs/search_job.html')
    

