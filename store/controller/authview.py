from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect,render
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

from store.forms import CustomUserForm

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'store/auth/password_reset.html'
    email_template_name = 'store/auth/password_reset_email.html'
    subject_template_name = 'store/auth/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'store/auth/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')
    
def register(request):
  form  = CustomUserForm()
  if request.method == 'POST':
    form = CustomUserForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, "註冊成功！登錄以繼續")
      return redirect('/login')
  context = {
    'form':form
  }
  return render(request, "store/auth/register.html", context)

def loginpage(request):
  if request.user.is_authenticated:
    messages.warning(request, "您已經登錄")
    return redirect('/')
  else:
    if request.method == 'POST':
      name = request.POST.get('username')
      passwd = request.POST.get('password')

      user = authenticate(request, username=name, password=passwd)

      if user is not None:
        login(request, user)
        messages.success(request, "登錄成功")
        return redirect('/')
      else:
        messages.error(request, "用戶名或密碼無效")
        return redirect('/login')
  return render(request, "store/auth/login.html")

def logoutpage(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request, "登出成功")
  return redirect('/')