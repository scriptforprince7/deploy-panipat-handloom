from django.shortcuts import render, redirect
from userauths.forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from userauths.models import User
from django.utils.crypto import get_random_string
from userauths.models import EmailVerificationToken
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from userauths.models import EmailVerificationToken
from django.urls import reverse_lazy
from django.template.loader import render_to_string
# User = settings.AUTH_USER_MODEL

def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            token = get_random_string(length=32)  # Generate a random token
            EmailVerificationToken.objects.create(user=new_user, token=token)
            send_verification_email(new_user, token)
            username = form.cleaned_data.get("username")
            messages.success(request, f" Hey {username}, Your account has been created successfully. Please check your email for verification instructions.") 
            return redirect("userauths:sign-in")  # Redirect to the login page
    else:
        form = UserRegistrationForm()    

    context = {
        'form' : form,
    }
    return render(request, "userauths/sign-up.html", context)


def send_verification_email(user, token):
    subject = "Verify Your Email"
    verification_url = f"{settings.BASE_URL}{reverse_lazy('userauths:verify-email', args=[token])}"

    context = {
        'user': user,
        'verification_url': verification_url,
    }

    message = render_to_string('userauths/email_template.html', context)

    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    send_mail(
    subject,
    '',
    from_email,
    recipient_list,
    html_message=message,  # Pass your HTML content here
    fail_silently=False,
)


def login_view(request):
    if request.user.is_authenticated:
        if request.user.email_verified:
            return redirect("core:index")
        else:
            messages.warning(request, "Your email is not verified yet. Please verify your email before logging in.")
            return redirect("userauths:sign-in")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
            if user.email_verified:  # Check if the email is verified
                user = authenticate(request, email=email, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, "You are logged in.")
                    return redirect("core:index")
                else:
                    messages.warning(request, "Invalid credentials.")
            else:
                messages.warning(request, "Your email is not verified yet. Please verify your email before logging in.")
        except User.DoesNotExist:
            messages.warning(request, f"User with {email} does not exist")

    return render(request, "userauths/sign-in.html")




def logout_view(request):
    logout(request)
    messages.success(request, "You Logged Out.")
    return redirect("userauths:sign-in")



def verify_email(request, token):
    verification_token = get_object_or_404(EmailVerificationToken, token=token)
    user = verification_token.user
    user.email_verified = True
    user.save()
    verification_token.delete()  # Token is no longer needed
    return render(request, "userauths/email_verified.html")  # Create this template




