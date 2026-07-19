from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, About
from .forms import ContactForm

def home(request):
    projects = Project.objects.all().order_by('-created_at')
    skills = Skill.objects.all().order_by('category')
    about = About.objects.first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
            return redirect('home')
    else:
        form = ContactForm()

    context = {
    'projects': projects,
    'skills': skills,
    'about': about,
    'form': form,
    'version': 'DEPLOY TEST 123',
    }
    return render(request, "portfolio_app/home.html", context)