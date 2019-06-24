from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),  
     path('blogpost/', views.BlogListView.as_view(), name='blogpost'),  
     path('blogpost/<int:pk>', views.BlogpostDetailView.as_view(), name='blogpost-detail'),
]



