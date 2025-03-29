from django.shortcuts import render
from .models import PersonalInfo, Education, Experience, Skill
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


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

@require_POST  # Ensures only POST requests are accepted
def send_email(request):
    try:
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if not name or not email or not message:
            return JsonResponse({"message": "All fields are required."}, status=400)

        subject = f"New Contact Form Submission from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        sender_email = "beautikumari2920@gmail.com"  # Replace with your SMTP-configured email
        recipient_email = "beautikumari2920@gmail.com"

        send_mail(subject, body, sender_email, [recipient_email])

        return JsonResponse({"message": "Message sent successfully!"})
    
    except BadHeaderError:
        return JsonResponse({"message": "Invalid email header."}, status=400)
    except Exception as e:
        return JsonResponse({"message": f"Error sending email: {str(e)}"}, status=500)
