from django.shortcuts import redirect,render
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from store.models import Order,OrderItem

def index(request):
  if request.user.is_superuser:
    orders = Order.objects.all
  else:
    orders = Order.objects.filter(user=request.user)
  context = { 'orders': orders}
  return render(request, "store/orders/index.html",context)

def vieworder(request,t_no):
  if request.user.is_superuser:
    order = Order.objects.filter(tracking_no = t_no).first()
    orderitems = OrderItem.objects.filter(order=order)
  else:
    order = Order.objects.filter(tracking_no = t_no).filter(user = request.user).first()
    orderitems = OrderItem.objects.filter(order=order)
  context = {'order':order, 'orderitems': orderitems}
  return render(request,"store/orders/view.html",context)