from django.db import models
from django.contrib.auth.models import User

import datetime
import os

def get_file_path(request,filename):
  original_filename = filename
  nowTime = datetime.datetime.now().strftime('$Y%m%d%H:%M:%S')
  filename = "%s%s" % (nowTime,original_filename)
  return os.path.join('uploads/',filename)

class Category(models.Model):
  slug = models.CharField(max_length=150, null=False, blank=False)
  name = models.CharField(u'目錄名稱',max_length=150, null=False, blank=False)
  image = models.CharField(u'圖片網址',max_length=500, null=False, blank=False)
  description = models.TextField(max_length=500,null=False,blank=False)
  status = models.BooleanField(default=False,help_text="0=default, 1=Hidden")
  trending = models.BooleanField(default=False,help_text="0=default, 1=Trending")
  meta_title = models.CharField(max_length=150, null=False, blank=False)
  meta_keywords = models.CharField(max_length=150, null=False, blank=False)
  meta_description = models.TextField(max_length=500, null=False, blank=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name
  
class Product(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  slug = models.CharField(u'slug',max_length=150, null=False, blank=False)
  name = models.CharField(u'產品名稱',max_length=150, null=False, blank=False)
  product_image = models.CharField(u'主圖網址',max_length=500, null=True, blank=True)
  product_sub_image = models.CharField(u'次圖網址',max_length=500, null=True, blank=True)
  description = models.TextField(u'其他說明',max_length=500,null=True,blank=True)
  small_description = models.TextField(u'說明(紅字)',max_length=250,null=True,blank=True)
  meta_title = models.TextField(u'說明(藍字)',max_length=150, null=True, blank=True)
  meta_keywords = models.TextField(u'說明(綠字)',max_length=150, null=True, blank=True)
  meta_description = models.TextField(u'說明(黑字)',max_length=150, null=True, blank=True)
  quantity = models.IntegerField(u'庫存數',null=False, blank=False)
  original_price = models.FloatField(u'原價',null=False, blank=False)
  selling_price = models.FloatField(u'特價',null=False, blank=False)
  status = models.BooleanField(u'顯示/隱藏',default=False,help_text="0=default, 1=Hidden")
  trending = models.BooleanField(u'熱搜商品',default=False,help_text="0=default, 1=Trending")
  tag = models.CharField(u'商品標籤',max_length=150, null=False, blank=False)
  created_at = models.DateTimeField(u'說明(黑字)',auto_now_add=True)

  def __str__(self):
    return self.name

class Cart(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  product_qty = models.IntegerField(null=False,blank=False)
  remark = models.TextField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def getCartSingleItemPrice(self):
    newlist=[]
    try:
      if self.product_qty >= 100:
        return self.product_qty * self.product.selling_price
      else:
        return self.product_qty * self.product.original_price
    except:
      newlist.append(0)


class Wishlist(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  fname = models.CharField(max_length=150,null=False)
  email = models.CharField(max_length=150,null=False)
  phone = models.CharField(max_length=150,null=False)
  uniNumber = models.CharField(max_length=10, null=False)
  address = models.TextField(null=False)
  city = models.CharField(max_length=150,null=False)
  pincode = models.CharField(max_length=150,null=False)
  total_price = models.FloatField(null=False)
  payment_mode = models.CharField(max_length=150,null=False)
  payment_id = models.CharField(max_length=250,null=True)
  orderstatus = (
    ('Pending','Pending'),
    ('Out For Shipping','Out For Shipping'),
    ('Completed','Completed'),
  )
  status = models.CharField(max_length=150,choices=orderstatus,default='Pending')
  message = models.TextField(max_length=150,null=True)
  tracking_no = models.CharField(max_length=150,null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return '{} - {}'.format(self.id,self.tracking_no)
  
class OrderItem(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  product = models.ForeignKey(Product, on_delete=models.CASCADE)
  price = models.FloatField(null=False)
  remark = models.TextField(blank=True, null=True)
  quantity = models.IntegerField(null=False)

  def __str__(self):
    return '{} - {}'.format(self.order.id,self.order.tracking_no)
  
  def getOrderSingleItemPrice(self):
    newlist=[]
    try:
      if self.quantity >= 100:
        return self.quantity * self.product.selling_price
      else:
        return self.quantity * self.product.original_price
    except:
      newlist.append(0)

class Profile(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  uniNumber = models.CharField(max_length=10, null=False)
  phone = models.CharField(max_length=50, null=False)
  address = models.TextField(null=False)
  city = models.CharField(max_length=150,null=False)
  pincode = models.CharField(max_length=150,null=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.user.username

