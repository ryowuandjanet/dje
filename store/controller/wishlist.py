from django.http.response import JsonResponse
from django.shortcuts import redirect,render
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from store.models import Wishlist,Product

@login_required(login_url='loginpage')
def index(request):
  wishlist = Wishlist.objects.filter(user=request.user)
  context = { 'wishlist': wishlist}
  return render(request,"store/wishlist.html",context)

def addtowishlist(request):
  if request.method == 'POST':
    if request.user.is_authenticated:
      prod_id = int(request.POST.get('product_id'))
      product_check = Product.objects.get(id=prod_id)
      if(product_check):
        if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
          return JsonResponse({'status': "產品已加入願望清單"})
        else:
          Wishlist.objects.create(user=request.user,product_id=prod_id)
          return JsonResponse({'status': "產品已添加至願望清單"})
      else:
        return JsonResponse({'status': "沒有找到該產品"})
    else:
      return JsonResponse({'status': "登錄以繼續"})
  return redirect('/')

def deletewishlistitem(request):
  if request.method == 'POST':
    if request.user.is_authenticated:
      prod_id = int(request.POST.get('product_id'))
      if(Wishlist.objects.filter(user=request.user,product_id=prod_id)):
        wishlistitem = Wishlist.objects.get(product_id = prod_id)
        wishlistitem.delete()
        return JsonResponse({'status': "產品已從願望清單中刪除"})
      else:
        return JsonResponse({'status': "在願望清單中找不到產品"})
    else:
      return JsonResponse({'status': "登錄以繼續"})
  return redirect('/')