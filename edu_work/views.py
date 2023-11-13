from django.shortcuts import render, redirect
from .forms import ExperienceForm
from .models import Experience

def experience_list(request):
    experiences= Experience.objects.all()
    return render(request, 'experience/experience_list.html', {'experiences': experiences})

def experience_new(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience= form.save()
            return redirect('experience_list')
    else:
        form = ExperienceForm()

    return render(request, 'experience/experience_new.html', {
        'form': form
    })

