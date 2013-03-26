from django.conf import settings
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('{{ app_name }}.urls',
        namespace='{{ app_name }}', app_name='{{ app_name }}')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


# extra urlpatterns for development used for serving media and for serving a
# dummy favicon.
if settings.DEBUG:
    from django.http import HttpResponse

    def favicon(request):
        image_data = open("example_project/static_root/favicon.ico", "rb").read()
        return HttpResponse(image_data, mimetype="image/x-icon")

    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^favicon.ico$', favicon),
    )
