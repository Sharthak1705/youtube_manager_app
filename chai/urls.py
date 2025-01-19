from . import views
from django.urls import path

urlpatterns = [
    path('', views.chai_list, name='chai_list'),
    path('create/', views.chai_create,name= 'chai_create'),
    path('<int:chai_id>/edit/', views.chai_edit,name= 'chai_edit'),
    path('<int:chai_id>/delete/', views.chai_remove,name='chai_remove'),
    path('register/', views.register, name= 'register'),
    
      
] 