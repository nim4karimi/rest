from django.contrib import admin
from django.urls import path , re_path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Use regex with re_path
    re_path(r'^api/', include('rest_framework.urls')),
]
