# -*- coding: utf-8 -*-

from django.conf.urls import patterns
from views import welcome

urlpatterns = patterns('',
  ('^welcome$', welcome)
)
