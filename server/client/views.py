from django.shortcuts import render
# email imports start
from django.core.mail import send_mail
from django.conf import settings
# email imports end

# Create your views here.


def IndexView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        businessName = request.POST.get('business_name')
        service_type = request.POST.get('service_type')
        contact_number = request.POST.get('contact_number')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # ========== Email myself new registration ==========
        subject = "New Registration Submitted"
        message = f"""
        A new registration has been submitted:

        Name: {name}
        Business Name: {businessName}
        Service Type: {service_type}
        Contact: {contact_number}
        Email: {email}
        message: {message}
                """

        # Step 2: try sending email
        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['stride.sa.za@gmail.com', 'thulanencholo95@gmail.com'],
                fail_silently=False,
            )
            form_status = 'success'  # Step 3a: success if no error
        except Exception as e:
            form_status = 'error'  # Step 3b: error if email fails

    return render(request, 'client/index.html')
