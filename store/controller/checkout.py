from django.http.response import JsonResponse
from django.http import HttpResponse
from django.shortcuts import redirect,render
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from store.models import Cart,Order,OrderItem,Product,Profile
from django.contrib.auth.models import User
import random

@login_required(login_url='loginpage')
def index(request):
  rawcart = Cart.objects.filter(user=request.user)
  for item in rawcart:
    if item.product_qty > item.product.quantity:
      Cart.objects.delete(id=item.id)
  
  remarkcart = Cart.objects.filter(user=request.user)
  for item in remarkcart:
    if item.remark:
      remark = item.remark
    else:
      remark = ""

  cartitems = Cart.objects.filter(user=request.user)
  total_price = 0
  total_price_tax = 0
  for item in cartitems:
    if item.product_qty >= 100:
      total_price = total_price + item.product.selling_price * item.product_qty
      total_price_tax = total_price * 1.05
    else:
      total_price = total_price + item.product.original_price * item.product_qty
      total_price_tax = total_price * 1.05

  userprofile = Profile.objects.filter(user=request.user)

  context = { 'cartitems': cartitems, "total_price":total_price,"total_price_tax":total_price_tax,"userprofile":userprofile,"remark":remark}
  return render(request,"store/checkout.html",context)

@login_required(login_url='loginpage')
def placeorder(request):
  if request.method == 'POST':
    currentuser = User.objects.filter(id=request.user.id).first()
    if not currentuser.first_name:
      currentuser.first_name = request.POST.get('fname')
      currentuser.save()
    
    if not Profile.objects.filter(user=request.user):
      userprofile = Profile()
      userprofile.user = request.user
      userprofile.phone = request.POST.get('phone')
      userprofile.uniNumber = request.POST.get('uniNumber')
      userprofile.address = request.POST.get('address')
      userprofile.city = request.POST.get('city')
      userprofile.pincode = request.POST.get('pincode')
      userprofile.save()


    neworder = Order()
    neworder.user = request.user
    neworder.fname = request.POST.get('fname')
    neworder.uniNumber = request.POST.get('uniNumber')
    neworder.email = request.POST.get('email')
    neworder.phone = request.POST.get('phone')
    neworder.address = request.POST.get('address')
    neworder.city = request.POST.get('city')
    neworder.pincode = request.POST.get('pincode')

    neworder.payment_mode = request.POST.get('payment_mode')
    neworder.payment_id = request.POST.get('payment_id')

    cart = Cart.objects.filter(user = request.user)

    cart_total_price = 0
    for item in cart:
      if item.product_qty >= 100:
        cart_total_price = cart_total_price + item.product.selling_price * item.product_qty
      else:
        cart_total_price = cart_total_price + item.product.original_price * item.product_qty

    if neworder.uniNumber:
      neworder.total_price = cart_total_price * 1.05
    else:
      neworder.total_price = cart_total_price
    
    trackno ='bigbear'+str(random.randint(1111111,9999999))
    while Order.objects.filter(tracking_no = trackno) is None:
      trackno ='bigbear'+str(random.randint(1111111,9999999))
    
    neworder.tracking_no = trackno
    neworder.save()

    neworderitems = Cart.objects.filter(user = request.user)
    for item in neworderitems:
      OrderItem.objects.create(
        order = neworder,
        product = item.product,
        price = item.product.selling_price,
        quantity = item.product_qty,
        remark =item.remark,
      )

      orderproduct = Product.objects.filter(id=item.product_id).first()
      orderproduct.quantity = orderproduct.quantity - item.product_qty
      orderproduct.save()
    
    Cart.objects.filter(user=request.user).delete()

    payMode = request.POST.get('payment_mode')
    if (payMode == "Paid by Razorpay" or payMode == "Paid by PayPal"): 
      return JsonResponse({'status': "Your order has been placed successfully"})
    else:
      messages.success(request,"Your order has been placed successfully")
  return redirect('/')

@login_required(login_url='loginpage')
def razorpaycheck(request):
  cart = Cart.objects.filter(user=request.user)
  total_price = 0
  for item in cart:
    if item.product_qty >= 100:
      total_price = total_price + item.product.selling_price * item.product_qty
    else:
      total_price = total_price + item.product.original_price * item.product_qty  
  return JsonResponse({
    'total_price': total_price
  })

def orders(request):
  return HttpResponse("My Order page")