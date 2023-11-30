from django.urls import path
from .import views

app_name = 'starrail'

urlpatterns = [
    path('', views.StrategyList.as_view(), name='index'),
    path('destiny', views.Destiny_View.as_view(), name='destiny'),
    path('universe-3', views.Universe_3View.as_view(), name='universe_3'),
    path('universe-4', views.Universe_4View.as_view(), name='universe_4'),
    path('universe-5', views.Universe_5View.as_view(), name='universe_5'),
    path('universe-6', views.Universe_6View.as_view(), name='universe_6'),
    path('universe-7', views.Universe_7View.as_view(), name='universe_7'),
    path('universe-8', views.Universe_8View.as_view(), name='universe_8'),
    path('mypage', views.mypage_view, name='mypage'),
]
