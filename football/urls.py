from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('blog.urls')),
    path('matches/', include('matches.urls')),
    path('team/', include('team.urls')),
    path('club/', include('the_club.urls')),
    path('chaining/', include('smart_selects.urls')),
    path('', include('club.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)