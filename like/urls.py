from django.urls import path
from like import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(views.LikeCreateView.as_view())),
    path('<int:pk>/', views.LikeDeleteView.as_view()),
]