# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('submission.views',
    url(r'^list/$', 'list', name='list'),
)
