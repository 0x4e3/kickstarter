from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.views import defaults as default_views

urlpatterns = [
    url(settings.ADMIN_URL, admin.site.urls)
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns = [
        url(r'^400/$', default_views.bad_request,
            kwargs={'exception': Exception('Bad Request!')},
            name='bad_request'),
        url(r'^403/$', default_views.permission_denied,
            kwargs={'exception': Exception('Permission Denied')},
            name='permission_denied'),
        url(r'^404/$', default_views.page_not_found,
            kwargs={'exception': Exception('Page not Found')},
            name='not_found'),
        url(r'^500/$', default_views.server_error,
            name='internal_server_error'),
    ] + urlpatterns
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ] + urlpatterns
    # This allows to serve static files during development
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
