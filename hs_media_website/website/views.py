from datetime import datetime
from email.message import EmailMessage

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView,TemplateView

from .forms import ProfileForm, SignUpForm, StartContractForm
from .models import (
    Contact1,Logo
)
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve the logo instance
        logo_instance = Logo.objects.first()

        # Add the logo URL to the context
        context['logo_image_url'] = logo_instance.image.url if logo_instance else None

        return context

# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "commons/signup.html"


# Edit Profile View
class ProfileView(UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy("home")
    template_name = "commons/profile.html"


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        desc = request.POST["desc"]
        contact = Contact1(
            name=name, email=email, phone=phone, desc=desc, date=datetime.today()
        )
        contact.save()

        # sendEmail
        email_send = EmailMessage(
    "Welcome to HS MEDIA SOLUTION - Your Digital Marketing Partner",  # subject
    f"Hi {name}!\n\nThank you for reaching out to HS MEDIA SOLUTION, where your digital journey begins!\n\nWe've received your message and will get back to you shortly.\n\nIn the meantime, here's a quick summary:\n\nPhone: {phone}\n\nMessage:\n{desc}\n\nYour success is our priority at HS MEDIA SOLUTION. Stay tuned for innovative digital solutions!\n\nBest regards,\nThe HS MEDIA SOLUTION Team",
    settings.EMAIL_HOST_USER,
    [email],
)


        email_send.fail_silently = True
        email_send.send()

        messages.success(request, "A Contact Message Received.")
    # return HttpResponse("This is Service page")
    # return HttpResponse("This is Contact page")
    return render(request, "contact.html", {})


def UploadFile(request):
    if request.method == "POST":
        form = StartContractForm(request.POST, request.FILES)
        name = request.POST["name"]

        email = request.POST["email"]
        price = request.POST["price"]
        phone = request.POST["phone"]
        desc = request.POST["desc"]

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            form.save()

            # sendEmail
        email_send = EmailMessage(
                "Welcome to HA MEDIA Solutions - Your Contract Submission",
                f"Hi {name}!\n\nThank you for choosing HA MEDIA Solutions. We're delighted to embark on this journey with you!\n\nYour contract submission details:\n\nPhone: {phone}\nPrice Mentioned: {price}\nContract Details: {desc}\n\nConfirmation Date: {datetime.today()}\n\nGet ready for an innovative collaboration. Our team is excited to bring your vision to life!\n\nBest regards,\nThe HA MEDIA Solutions Team",
                settings.EMAIL_HOST_USER,
                [email],
            )

        email_send.fail_silently = True
        email_send.send()
        return redirect("home")
    else:
        form = StartContractForm()

        context = {
            "form": form,
        }

    return render(request, "upload.html", context)







