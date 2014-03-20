from django.conf import settings
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # apps.lib
    url(r'^$', 'apps.lib.views.base'),
)


if 'django.contrib.admin' in settings.INSTALLED_APPS:
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns += patterns('',
        url(r'^admin/', include(admin.site.urls)),
    )
