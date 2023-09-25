from decimal import *
from django import template

register=template.Library()

# 用法 {% singlePrice qty originalPrice sellingPrice %}
@register.simple_tag(name='singlePrice')
def singlePrice(qty, originalPrice, sellingPrice):
  newlist=[]
  singlePrice = 0
  try:
    if qty >= 100:
      singlePrice = int(sellingPrice) * int(qty)
    else:
      singlePrice = int(originalPrice) * int(qty)
    return singlePrice
  except:
    newlist.append(0)