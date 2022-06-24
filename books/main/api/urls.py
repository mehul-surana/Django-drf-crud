
from django.urls import path,include
from .views import BookViewSets

from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'books',BookViewSets)

urlpatterns = [
    path('',include(router.urls))
]