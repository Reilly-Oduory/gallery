from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search/', views.search_results, name='search_results'),
    path('category/<category_name>/', views.category, name='category_results'),
    path('image/<image_id>', views.individual_image, name='image'),
    path('image/<image_id>/comment', views.comment, name='new_comment')

]
