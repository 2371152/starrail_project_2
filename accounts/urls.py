# p377
from django.urls import path, include
from . import views
from .views import contact_view
# p395
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signup_success/', views.SignUpSuccessView.as_view(), name='signup_success'),
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),
    path('accounts/index/', views.IndexView.as_view(), name='index'),
    path('mypage/', views.MypageView.as_view(), name='mypage'),
    path('post/', views.CreateStrategyView.as_view(), name='post'),
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),
    path('strategys/<int:category>',
         views.CategoryView.as_view(), name='strategys_cat'),
    path('strategy-detail/<int:pk>',
         views.DetailView.as_view(), name='strategy_detail'),
    path('photo/<int:pk>/delete/',
         views.PhotoDeleteView.as_view(), name='photo_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact/', contact_view, name='contact_view'),
]
