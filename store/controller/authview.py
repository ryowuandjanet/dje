from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect,render
from django.contrib import messages

from store.forms import CustomUserForm

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