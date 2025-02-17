from django.contrib import admin
from django.urls import path
from card.views import VisitCardView





urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/generate-visit-card/', VisitCardView.as_view(), name='generate-visit-card'),
]