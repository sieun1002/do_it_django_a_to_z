from django.urls import path 
from . import views 

urlpatterns = [
  #CBV 형식
  path('', views.PostList.as_view()),
  path('<int:pk>/', views.PostDetail.as_view()),
  path('category/<str:slug>/', views.category_page),

  #FBV 형식
  # path('<int:pk>/', views.single_post_page),
  # path('', views.index),
]