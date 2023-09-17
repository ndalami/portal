from django.shortcuts import redirect, render
from jobs.models import Choice, Job
from .forms import CategoryForm, JobForm
from django.core.paginator import Paginator

# Create your views here.

# view to render category list
def category(request):
    category_list = Choice.objects.all()
    context ={'category_list':category_list}
    return render(request, 'userpages/category.html',context)

# view to update category
def category_update(request, category_id):
    category = Choice.objects.get(pk=category_id)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('userpages:category')
    context = {'category':category, 'form':form}
    return render(request, 'userpages/category_update.html',context)

# view to add category
def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
           form.save()
           return redirect('userpages:category')
    
    else:
        form = CategoryForm()
    return render(request, 'userpages/category_add.html',{'form':form})

# view to delete category
def delete_category(request,category_id):
    category = Choice.objects.get(pk=category_id)
    category.delete()
    return redirect('userpages:category')


# view to render job list
def job(request):
    available_jobs = Job.objects.all()
    category = Choice.objects.all()

    p = Paginator(Job.objects.all().order_by('-id'),5)
    page = request.GET.get('page')
    job = p.get_page(page)
    return render(request,'userpages/job.html',{'available_jobs':available_jobs,
    'category':category,'job':job})

# view to update job info
def job_update(request,job_id):
    job = Job.objects.get(pk = job_id)
    form = JobForm(request.POST or None, instance=job)
    if form.is_valid():
        form.save()
        return redirect('userpages:job')
    context = {'job':job, 'form':form}
    return render(request, 'userpages/job_update.html',context)

# view to add job
def job_add(request):
    if request.method == 'POST':
        form = JobForm(request.POST)

        if form.is_valid():
           form.save()
           return redirect('userpages:job')
    
    else:
        form = JobForm()
    return render(request, 'userpages/job_add.html',{'form':form})

# view to delete a particular job
def delete_job(request,job_id):
    job = Job.objects.get(pk=job_id)
    job.delete()
    return redirect('userpages:job')

# view to render main dashboard page
def home(request):
    job_count = Job.objects.all().count
    category_count = Choice.objects.all().count
    return render(request, 'userpages/home.html',{'job_count':job_count,'category_count':category_count})