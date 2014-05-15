from django.conf.urls import patterns, include, url

from django.contrib import admin
from webSite.views import siteList

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^webSite/site/list$', siteList),
)
