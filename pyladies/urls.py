from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    
    url(r'^$', 'pyladies.homepage.views.home_page', name='home_page'),
    url(r'^blog/', include('pyladies.blog.urls')),
    url(r'^calendar/', include('pyladies.calendar.urls')),
    url(r'^chapters/', include('pyladies.chapters.urls')),
    url(r'^jobs/', include('pyladies.jobs.urls')),
    url(r'^sponsors/', include('pyladies.sponsors.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),

)
