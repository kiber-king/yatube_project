from django.urls import path


from . import views
app_name = 'Posts'


urlpatterns = [
    path('', views.index, name='index'),
    path('group/', views.group_posts, name='group_posts'),
]
