from re import template
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm
urlpatterns = [
    # path('', views.home),
    path('',views.ProductView.as_view(),name="home"),
    
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),

    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),

    path('light/', views.light, name='light'),
    path('light/<slug:data>', views.light, name='lightdata'),

    path('horror/', views.horror, name='horror'),
    path('horror/<slug:data>', views.horror, name='horrordata'),

    path('motivation/', views.motivation, name='motivation'),
    path('motivation/<slug:data>', views.motivation, name='motivationdata'),

    path('login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name="app/passwordchangedone.html"),name="passwordchangedone"),
    # path('registration/', views.customerregistration, name='customerregistration'),


    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name='password_reset_done'),

    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'),name='passwordchange'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name='password_reset_complete'),

    path('registraion/',views.CustomerRegistrationView.as_view(),name="customerregistration"),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
