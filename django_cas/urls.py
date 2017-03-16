__author__ = 'sannies'

try:
    from django.conf.urls.defaults import url
except ImportError:
    from django.conf.urls import url

from .views import login, logout, proxy_callback

urlpatterns = [
    url(r'^login$', login, name="cas_login"),
    url(r'^logout$', logout, name="cas_logout"),
    url(r'^proxycallback$', proxy_callback, name="cas_proxy_callback"),
]
