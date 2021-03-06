"""filmratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import RedirectView

from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
    password_change,
    password_change_done,
)

from films import views
from films.backends import MyRegistrationView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),

    url(r'^films/$',
        RedirectView.as_view(pattern_name='browse', permanent=True)),
    url(r'^films/(?P<slug>[-\w]+)/$', views.film_detail, name='film_detail'),
    url(r'^films/(?P<slug>[-\w]+)/edit/$', views.edit_film, name='edit_film'),

    url(r'^browse/$',
        RedirectView.as_view(pattern_name='browse', permanent=True)),
    url(r'^browse/name/$', views.browse_by_name, name='browse'),
    url(r'^browse/name/(?P<initial>[-\w]+)/$', views.browse_by_name,
        name='browse_by_name'),

    url(r'^accounts/password/reset/$', password_reset, {
        'template_name': 'registration/password_reset_form.html'
    }, name='password_reset'),
    url(r'^accounts/password/reset/done/$', password_reset_done, {
        'template_name': 'registration/password_reset_done.html'
    }, name='password_reset_done'),
    url(r'^accounts/password/reset(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+/$)',
        password_reset_confirm, {
            'template_name': 'registration/password_reset_confirm.html'
        }),
    url(r'^/accounts/password/done/$', password_reset_complete, {
        'template_name': 'registration/password_reset_complete.html'
    }, name='password_reset_complete'),
    url(r'^accounts/password/change/$', password_change, {
        'template_name': 'registration/password_change_form.html'
    }, name='password_change'),
    url(r'^/accounts/password/change/done$', password_change_done, {
        'template_name': 'registration/password_change_done.html'
    }, name='password_change_done'),
    url(r'^accounts/register/$', MyRegistrationView.as_view(),
        name='registration_register'),
    url(r'^accounts/create_film/$', views.create_film,
        name='registration_create_film'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
