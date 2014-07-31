from django.conf.urls import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()

from huntertools import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^gearitem/', include('gearitem.urls', namespace="gearitem")),
    url(r'^hunter/', include('hunter.urls', namespace="hunter")),
    url(r'^$', views.Home, name='home'),
    url(r'^changelog/', views.ChangeLog, name='changelog'),
    url(r'^faq/', views.FAQ, name='faq'),
    url(r'^about/', views.About, name='about'),
    url(r'^admin/', include(admin.site.urls)),
)
