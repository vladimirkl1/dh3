from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name='homepage.html'),name="homepage"),
#    url(r'^about/', include('dhru.about.urls',namespace="about")),
#    url(r'^items/', include('dhru.items.urls',namespace="items")),
#    url(r'^stores/',include('dhru.stores.urls',namespace="stores")),
#    url(r'^online/',include('dhru.online.urls',namespace="online")),
#    url(r'^social/',include('dhru.social.urls',namespace="social")),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('dhru.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
