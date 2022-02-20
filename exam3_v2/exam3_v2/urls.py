from django.contrib import admin
from django.urls import path, include

import exam3_v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exam3_v2.notes_app.urls'))
]
