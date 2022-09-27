
from django.contrib import admin
from django.urls import path

from myapp.views import index, delete_consume

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index , name='index'),
    path('delete/<int:id>/',delete_consume, name='delete' ),
]
