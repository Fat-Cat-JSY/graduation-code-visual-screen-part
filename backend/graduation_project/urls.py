"""dj2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""
import os
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from django.views.static import serve
from django.views.generic import TemplateView

from . import views
from backend.graduation_project.settings import dbName as schemaName

urlpatterns = [
    path('xadmin/', admin.site.urls),
    path(r'index/', views.index),
    path('{}/'.format(schemaName), include('backend.apps.core.urls')),  # 导入schemaName
    re_path(r'admin/lib/(?P<p1>.*)/(?P<p2>.*)$', views.admin_lib2),
    re_path(r'admin/lib/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)$', views.admin_lib3),
    re_path(r'admin/lib/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)/(?P<p4>.*)$', views.admin_lib4),
    re_path(r'admin/page/(?P<p1>.*)$', views.admin_page),
    re_path(r'admin/page/(?P<p1>.*)/(?P<p2>.*)$', views.admin_page2),
    re_path(r'admin/pages/(?P<p1>.*)$', views.admin_pages),
    re_path(r'admin/pages/(?P<p1>.*)/(?P<p2>.*)$', views.admin_pages2),

    re_path(r'front/(?P<p1>.*)$', views.schema_front1),
    re_path(r'front/(?P<p1>.*)/(?P<p2>.*)$', views.schema_front2),
    re_path(r'front/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)$', views.schema_front3),
    re_path(r'front/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)/(?P<p4>.*)$', views.schema_front4),
    re_path(r'front-pc/(?P<p1>.*)$', views.schema_frontpc1),
    re_path(r'front-pc/(?P<p1>.*)/(?P<p2>.*)$', views.schema_frontpc2),
    re_path(r'front-pc/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)$', views.schema_frontpc3),
    re_path(r'front-pc/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)/(?P<p4>.*)$', views.schema_frontpc4),

    re_path(r'{}/front/(?P<p1>.*)$'.format(schemaName), views.schema_front1),
    re_path(r'{}/front/(?P<p1>.*)/(?P<p2>.*)$'.format(schemaName), views.schema_front2),
    re_path(r'{}/front/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)$'.format(schemaName), views.schema_front3),
    re_path(r'{}/front/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)/(?P<p4>.*)$'.format(schemaName), views.schema_front4),
    re_path(r'{}/front-pc/(?P<p1>.*)$'.format(schemaName), views.schema_frontpc1),
    re_path(r'{}/front-pc/(?P<p1>.*)/(?P<p2>.*)$'.format(schemaName), views.schema_frontpc2),
    re_path(r'{}/front-pc/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)$'.format(schemaName), views.schema_frontpc3),
    re_path(r'{}/front-pc/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)/(?P<p4>.*)$'.format(schemaName), views.schema_frontpc4),

    re_path(r'admin/(?P<p1>.*)/(?P<p2>.*)$', views.admin_file2),
    re_path(r'admin/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)$', views.admin_file3),
    re_path(r'admin/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)/(?P<p4>.*)$', views.admin_file4),
    re_path(r'layui/(?P<p1>.*)$', views.layui1),
    re_path(r'layui/(?P<p1>.*)/(?P<p2>.*)$', views.layui2),
    re_path(r'layui/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)$', views.layui3),
    re_path(r'layui/(?P<p1>.*)/(?P<p2>.*)/(?P<p3>.*)/(?P<p4>.*)$', views.layui4),
    re_path(r'pages/(?P<p1>.*)$', views.front_pages),
    re_path(r'pages/(?P<p1>.*)/(?P<p2>.*)$', views.front_pages2),
    re_path(r'modules/(?P<p1>.*)$', views.front_modules),
    re_path(r'css/(?P<p1>.*)$', views.css1),
    re_path(r'js/(?P<p1>.*)$', views.js1),
    re_path(r'img/(?P<p1>.*)$', views.img1),
    path(r'test/<str:p1>/', views.test),
    path(r'null', views.null),
]

# 判断admin使用vue还是jquery
if os.path.isdir(os.path.join(os.getcwd(), "frontend/vue-admin/admin/dist/")):
    urlpatterns.extend([
        path(r'{}/admin/dist/index.html'.format(schemaName),
             TemplateView.as_view(template_name='vue-admin/admin/dist/index.html')),
        path(r'{}/admin/'.format(schemaName), TemplateView.as_view(template_name='vue-admin/admin/dist/index.html')),
        path(r'admin/dist/index.html'.format(schemaName),
             TemplateView.as_view(template_name='vue-admin/admin/dist/index.html')),
        path(r'admin/', TemplateView.as_view(template_name='vue-admin/admin/dist/index.html')),
    ])
else:
    urlpatterns.extend([
        path(r'{}/admin/index.html'.format(schemaName),
             TemplateView.as_view(template_name='vue-admin/admin/public/index.html')),
        path(r'{}/admin/'.format(schemaName), TemplateView.as_view(template_name='vue-admin/admin/public/index.html')),
        path(r'admin/index.html'.format(schemaName),
             TemplateView.as_view(template_name='vue-admin/admin/public/index.html')),
        path(r'admin/', TemplateView.as_view(template_name='vue-admin/admin/public/index.html')),
    ])


if os.path.isfile(os.path.join(os.getcwd(), "frontend/vue-admin/public/index.html")):
    urlpatterns.extend([
        path(r'index.html', TemplateView.as_view(template_name='vue-admin/public/index.html')),
        path(r'{}/index.html'.format(schemaName), TemplateView.as_view(template_name='vue-admin/public/index.html')),
        path(r'{}/front/index.html'.format(schemaName), TemplateView.as_view(template_name='vue-admin/public/index.html')),
        path(r'', TemplateView.as_view(template_name='vue-admin/public/index.html')),
    ])