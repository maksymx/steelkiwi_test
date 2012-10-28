from django.conf.urls import patterns, include, url
from student.views import studentlist, edit_student
from group.views import grouplist, edit_group
from logger.views import delete_instance
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'steelkiwi_test.views.home', name='home'),
    # url(r'^steelkiwi_test/', include('steelkiwi_test.foo.urls')),
    url(r'^$', grouplist, name='index'),
    url(r'^group/(\d+)/$', studentlist, name='show_group'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/login/'}, name='logout'),
    url(r'^accounts/profile/', 'django.views.generic.simple.redirect_to', {'url': '/'}),
    url(r'^student/add/$', edit_student, name='add_student'),
    url(r'^student/add/(?P<group_id>\d+)/$', edit_student, name='add_student_to_group'),
    url(r'^student/edit/(\d+)/$', edit_student, name='edit_student'),

    url(r'^group/add/$', edit_group, name='add_group'),
    url(r'^group/edit/(\d+)/$', edit_group, name='edit_group'),

    url(r'^student/delete/(?P<instance_id>\d+)/',
        delete_instance,
        name='delete_student',
        kwargs={'instance_type': 1}),

    url(r'^group/delete/(?P<instance_id>\d+)/',
        delete_instance,
        name='delete_group',
        kwargs={'instance_type': 2}),
)
