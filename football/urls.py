from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^news/', include('blog.urls')),
    url(r'^matches/', include('matches.urls')),
    url(r'^team/', include('team.urls')),
    url(r'^club/', include('the_club.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^', include('club.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)