from django.urls import path
from category import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60*15)(views.CategoryCreateListView.as_view())),
    path('<int:pk>/', cache_page(60*15)(views.CategoryDetailView.as_view())),
]