from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .tokens import account_activation_token
from django.template.loader import render_to_string
from myshop.forms import SignUpForm, SignInForm
from utils.after_login import do_after_login_tasks

def signin_view(request):
    errors = []
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Do post login tasks
            do_after_login_tasks(request, user)
            # Redirect to a success page.
            return redirect(request.GET.get('next', 'home'))
        else:
            form = SignInForm(request.POST)
            errors.append('User not found')
            return render(request, 'auth/signin.html', {'form': form, 'errors': errors})
            # Return an 'invalid login' error message.
    else:
        form = SignInForm() 
    return render(request, 'auth/signin.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')

def activation_sent_view(request):
    return render(request, 'auth/activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true 
        user.is_active = True
        # set signup_confirmation true
        if user.customer.signup_confirmation == False:
            user.customer.signup_confirmation = True
            user.save()
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'activation/activation_invalid.html')

def signup_view(request):
    if request.method  == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.customer.first_name = form.cleaned_data.get('first_name')
            user.customer.last_name = form.cleaned_data.get('last_name')
            user.customer.email = form.cleaned_data.get('email')
            # user can't login until link confirmed
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            # load a template like get_template() 
            # and calls its render() method immediately.
            message = render_to_string('auth/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect(reverse('auth:activation_sent'))
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form})

def password_forget_view(request):
    if request.method == 'POST':
        pass
    else:
        form = PasswordResetForm()
        return render(request, "auth/password_forget.html", {'form': form})

@login_required
def password_reset_view(request):
    if request.method == 'POST':
        pass
    else:
        form = PasswordChangeForm(request.user)
        return render(request, "auth/password_reset.html", {'form': form})

def home_view(request):
    return render(request, 'index.html')

def file_not_found_404(request):
    return render(request, '404.html')

