from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings  
from django.conf.urls.static import static
from main import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^first_view/(?P<starts_with>\w+)/$', 'main.views.first_view'),
    # url(r'^get_post/', 'main.views.get_post'),
    # url(r'^template_view/', 'main.views.template_view', name='temaplate_view.name'),
    # url(r'^detail_view/(?P<pk>\d+)/$', 'main.views.detail_view'),
    # url(r'^list_view/$', 'main.views.list_view'),

    url(r'state_list/$', 'main.views.state_list'),
    url(r'state_detail/(?P<pk>.+)/$', 'main.views.state_detail'),
    url(r'state_cbv_list/$', views.StateListView.as_view()),
    url(r'^city_search/$', 'main.views.city_search'),
    url(r'^city_create/$', 'main.views.city_create'),
    url(r'^city_edit/(?P<pk>[0-9]+)/$', 'main.views.city_edit'),
    url(r'^city_delete/(?P<pk>[0-9]+)/$', 'main.views.city_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
