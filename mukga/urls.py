from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'muklib.views.action', name='action'),

    url(r'^intro$', 'muklib.views.intro', name='intro'),

    url(r'^result$', 'muklib.views.result', name='result'),

    url(r'^admin/', include(admin.site.urls)),
)
