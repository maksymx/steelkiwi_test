from django.conf.urls import patterns, include, url
from student.views import studentlist
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'steelkiwi_test.views.home', name='home'),
    # url(r'^steelkiwi_test/', include('steelkiwi_test.foo.urls')),
    url(r'^$', studentlist),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
