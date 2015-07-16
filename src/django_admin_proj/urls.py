from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'admin_dashboard.views.home', name='home'),
	url(r'^users/$', 'admin_dashboard.views.users', name='users'),
	url(r'^pre_reg/$', 'admin_dashboard.views.pre_reg', name='pre_reg'),
	url(r'^analystics/$', 'admin_dashboard.views.analytics', name='analytics'),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)