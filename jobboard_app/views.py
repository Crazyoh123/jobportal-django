from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobPostingForm
from .models import JobPosting

def home(request):
    return render(request, 'jobboard_app/home.html')

def create_job_posting(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  
    else:
        form = JobPostingForm()
    return render(request, 'jobboard_app/create_job_posting.html', {'form': form})

def job_list(request):
    jobs = JobPosting.objects.all()
    return render(request, 'jobboard_app/job_list.html', {'jobs': jobs})

def view_job(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
    return render(request, 'jobboard_app/job_details.html', {'job': job})
