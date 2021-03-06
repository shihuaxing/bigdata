#from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *

from graphmodels.accounts.views import profile, register
from graphmodels.views import index, test
from graphmodels.dataset.views import *
from graphmodels.program.views import *
from graphmodels.task.views import *
from graphmodels.vis.views import *
from graphmodels.docs.views import *

#from graphmodels.accounts.views import *
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import settings
import re

urlpatterns = patterns('',
    url(r'^medias/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^result/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.USR_RESULT_ROOT}),
    url(r'^vresult/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.USR_VIS_ROOT}),
    url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.IMAGE_ROOT}),
    # Examples:
    # url(r'^$', 'graphmodels.views.home', name='home'),
    # url(r'^graphmodels/', include('graphmodels.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),

    url(r'^$', index),
    #url(r'^accounts/index/$', index),
    #url(r'^accounts/register/$', register),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', logout, {'next_page': '/'}),
    url(r'^accounts/profile/$', profile),
    url(r'^accounts/register/$', register),
    url(r'^index/$', index),
    url(r'^test/$', test),
    url(r'^dataset/upload/$', dataset_upload),
    url(r'^datasets/$', dataset_view),
    url(r'^datasets/(\d+)/$', dataset_info),
    url(r'^model/upload/$', program_upload),
    url(r'^models/$', program_view),
    url(r'^task/submit/$', task_submit),
    url(r'^tasks/$', task_view),
    url(r'^tasks/(\d+)/$', task_info),
    url(r'^task/new/$', task_new),
    url(r'^viss/$', vis_view),
    url(r'^viss/(\d+)/$', vis_info),
    url(r'^vis/upload/$', vis_upload),
    url(r'^docs/intro/$', docs_intro),
    url(r'^docs/feature/$', docs_feature),
    url(r'^docs/dataset/$', docs_dataset),
    url(r'^docs/model/$', docs_api),
    url(r'^about/$', docs_about),
    url(r'^contact/$', docs_contact),
)
