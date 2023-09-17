from django.http.response import JsonResponse
from django.shortcuts import redirect,render
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from store.models import Product,Cart

def addtocart(request):
  if request.method == 'POST':
    if request.user.is_authenticated:
      prod_id = int(request.POST.get('product_id'))
      product_check = Product.objects.get(id=prod_id)
      if(product_check):
        if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
          return JsonResponse({'status':'產品已在購物車中'})
        else:
          prod_qty = int(request.POST.get('product_qty'))
          remark =request.POST.get('remark')
          print(remark)

          if product_check.quantity >= prod_qty:
            Cart.objects.create(user=request.user, product_id=prod_id, product_qty=prod_qty,remark=remark)
            return JsonResponse({'status':'產品添加成功'})
          else:
            return JsonResponse({'status':"Only "+str(product_check.quantity)+' quantity available'})
      else:
        return JsonResponse({'status':'沒有找到該產品'})
    else:
      return JsonResponse({'status':'登錄以繼續'})
  return redirect('/')

@login_required(login_url='loginpage')
def viewcart(request):
  cart = Cart.objects.filter(user=request.user)
  context = {'cart':cart}
  return render(request,"store/cart.html",context)

def updatecart(request):
  if request.method == 'POST':
    prod_id = int(request.POST.get('product_id'))
    if(Cart.objects.filter(user=request.user, product_id=prod_id)):
      prod_qty = int(request.POST.get('product_qty'))
      remark = request.POST.get('remark')
      cart = Cart.objects.get(product_id=prod_id, user=request.user)
      cart.product_qty = prod_qty
      cart.remark = remark
      cart.save()
      return JsonResponse({'status':'更新成功'})
  return redirect('/')


def deletecartitem(request):
  if request.method == 'POST':
    prod_id = int(request.POST.get('product_id'))
    if(Cart.objects.filter(user=request.user, product_id=prod_id)):
      cartitem = Cart.objects.get(product_id=prod_id, user=request.user)
      cartitem.delete()
    return JsonResponse({'status':'刪除成功'})
  return redirect('/')