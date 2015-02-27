from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'imdbboxes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^box/(?P<imdb_no>[\w\W]+)/$', 'box.views.BoxPage'),
    url(r'^posterbox/(?P<imdb_no>[\w\W]+)/$', 'box.views.PosterBoxPage'),
    url(r'^actorsfilmbox/(?P<imdb_no>[\w\W]+)/$', 'box.views.ActorOfTheFilmBoxPage'),
    url(r'^$', 'box.views.IndexPage'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)




