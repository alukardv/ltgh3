from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('users/', views.UsersView.as_view(), name='users'),
    path('question/', views.QuestionListView.as_view(), name='question'),
    path('about/', views.about, name='about'),
    #path('app1/', views.get_objects_on_map, name='get_objects_on_map'),
]
