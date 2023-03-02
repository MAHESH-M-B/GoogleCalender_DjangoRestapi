from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('rest/', include('DjangoGoogleCalenderApp.urls')),
    path('admin/', admin.site.urls),
]
