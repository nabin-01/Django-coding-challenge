from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from .models import *

def mail_to_client(self, request):
    user = request.user.username
    created_date = License.objects.get()
    exp_date = 


def license_data(request, id):
    license_id = License.objects.get(id=id)
    if request.method == 'POST':
        license_type = request.POST['license_type']
        package = request.POST['package']

        license_data = License.objects.create(
            license_type=license_type,
            package=package,
        )

        client_name = request.POST['client_name']
        poc_contact_name = request.POST['poc_contact_name']
        poc_contact_email = request.POST['poc_contact_email']

        client_data = Client.objects.create(
            client_name = client_name,
            poc_contact_name = poc_contact_name,
            poc_contact_email = poc_contact_email,
        )


        send_email = EmailMessage(
            'contact from your website',
            f'license id ->{license_id}'
            f'license_type -> {license_type}',
            settings.EMAIL_HOST_USER,
            [email],
        )
        send_email.fail_silently = False
        send_email.send()
        license_data.save()
        client_data
        return redirect('/', kwargs={'messages': messages.success(request, '✔ Contact Saved and an'
                                                                               ' email is sent to you.')})
    return render(request, 'contact.html')

