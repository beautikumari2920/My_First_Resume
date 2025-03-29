from django.shortcuts import render
from .models import PersonalInfo, Education, Experience, Skill

def resume_view(request):
    personal_info = PersonalInfo.objects.first()
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills = Skill.objects.all()
    return render(request, 'beauti_resume/resume.html', {
        'personal_info': personal_info,
        'education': education,
        'experience': experience,
        'skills': skills,
    })
