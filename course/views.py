from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import ApplicationForm
from django.core.mail import send_mail

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

def apply_course(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.course = course
            application.save()

            # 📧 Send confirmation email
            subject = f"Application Received for {course.name}"
            message = f"""
Dear {application.student_name},

Thank you for applying to the course '{course.name}' at BCIIT.

We have received your application and will contact you shortly.

Regards,
Admission Team
BCIIT
            """.strip()
            recipient_list = [application.email]
            send_mail(subject, message, 'your_email@gmail.com', recipient_list)

            return render(request, 'success.html', {'course': course})
    else:
        form = ApplicationForm()
    return render(request, 'apply_course.html', {'form': form, 'course': course})
