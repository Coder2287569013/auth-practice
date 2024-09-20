from django.urls import path
from review_system import views

urlpatterns = [
    path('', views.review_list, name='review-list'),
    path('review-form/', views.create_review, name='create-review')
]
