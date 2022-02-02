from django.urls import path, include
from streamapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path(r'^edit_favorites/$', views.edit_favorites, name='edit_favorites'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('grey_scale', views.grey_scale, name='grey_scale'),
    path('binary_scale', views.binary_scale, name='binary_scale'),
    path('grey_scale_page', views.grey_scale_page, name='grey_scale_page'),
    path('binary_scale_page', views.binary_scale_page, name='binary_scale_page'),
]
