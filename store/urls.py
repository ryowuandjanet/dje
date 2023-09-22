from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from store.controller import authview, cart, wishlist,checkout,order

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name='about'),
    path('collections',views.collections,name="collections"),
    path('collections/<str:slug>',views.collectionsview,name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>',views.productview,name="productview"),

    path('register/',authview.register,name='register'),
    path('login/',authview.loginpage,name='loginpage'),
    path('logout/',authview.logoutpage,name='logout'),
    path('password-reset/', authview.ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='store/auth/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='store/auth/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password-change/', authview.ChangePasswordView.as_view(), name='password_change'),
    # 等別注意，add-to-cart的後面不可再加/，會出錯
    # 如果在localhost:3000沒有作動，就把port改成3001
    path('add-to-cart', cart.addtocart, name='addtocart'),
    path('cart', cart.viewcart, name="cart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('delete-cart-item', cart.deletecartitem, name="deletecartitem"),

    path('wishlist', wishlist.index, name="wishlist"),
    path('add-to-wishlist', wishlist.addtowishlist, name="addtowishlist"),
    path('delete-wishlist-item', wishlist.deletewishlistitem, name="deletewishlistitem"),
    
    path('checkout', checkout.index, name="checkout"),
    path('place-order', checkout.placeorder, name="placeorder"),
    path('proceed-to-pay', checkout.razorpaycheck),
    path('my-orders', order.index,name="myorders"),
    path('view-order/<str:t_no>', order.vieworder,name="orderview"),
]
