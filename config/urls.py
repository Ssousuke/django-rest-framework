from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('cursos.urls')),
    path('login/admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
