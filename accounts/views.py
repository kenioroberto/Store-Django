import email
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.models import Account
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
# verificar email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]

            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()


            # Ativação do usuario cadastrado
            current_site = get_current_site(request)
            mail_subject = 'Ativação de sua conta'
            message = render_to_string('accounts/account_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()



            # messages.success(request, 'Obrigado pelo cadastro. Enviamos um email de verificação. Por favor verifique.')
            return redirect('/accounts/login/?command=verification&email='+email)
    else:
        form = RegistrationForm()
            
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(
            email=email,
            password=password
        )

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Você está logado!')
            return redirect('dashboard')

        else:
            messages.error(request, 'Usuário ou senha inválidos')
            return redirect('login')


    return render(request, 'accounts/login.html')



@login_required(login_url= 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Sessão encerrada')
    return redirect('login')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Conta ativada com sucesso! Boas compras.')
        return redirect('login')
    else:
        messages.error(request, 'Link inválido para ativação')
        return redirect('register')


@login_required(login_url= 'login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            #resert password email
            current_site = get_current_site(request)
            mail_subject = 'Redefinir sua senha'
            message = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request,'Redefinição de senha enviado para seu email.')
            return redirect('login')

        else:
            messages.error(request,'Essa conta não existe!')
            return redirect('forgotPassword')
    return render(request, 'accounts/forgotPassword.html')

def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request,'Redefine sua senha')
        return redirect('resetPassword')
    else:
        messages.error(request,'Esse link já expirou!')
        return redirect('login')

def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request,'Senha redefinida com sucesso!')
            return redirect('login')

        else:
            messages.error(request,'Senha nâo confere!')
            return redirect('resetPassword')
    else:
        return render(request, 'accounts/resetPassword.html')
