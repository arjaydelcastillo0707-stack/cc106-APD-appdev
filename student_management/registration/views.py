from django.shortcuts import redirect, render

from .models import Student


def student_registration(request):
    if request.method == 'POST':
        Student.objects.create(
            student_id=request.POST.get('student_id'),
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            gender=request.POST.get('gender'),
            date_of_birth=request.POST.get('date_of_birth'),
            contact_number=request.POST.get('contact_number'),
        )
        return redirect('registration_success')

    return render(request, 'registration/student_registration.html')


def registration_success(request):
    return render(request, 'registration/registration_success.html')
