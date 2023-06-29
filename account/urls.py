from django.urls import path, include
from . import views

from rest_framework.routers import SimpleRouter
from account.views import UserViewSet

from django.views.decorators.cache import cache_page

router = SimpleRouter()
router.register('', UserViewSet)


urlpatterns = [
    path('login/', cache_page(60)(views.LoginView.as_view())),
    path('refresh/', views.RefreshView.as_view()),
    path('', include(router.urls)),
]