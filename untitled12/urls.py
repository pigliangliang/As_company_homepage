from django.conf.urls import include, url
from django.contrib import admin

from . import view
from blogs import views as blog_views
from django.views.generic import RedirectView
urlpatterns = [
    # Examples:
    url(r'^$',view.hello,name='hello_index'),

    url(r'^calc_result',view.hello),
    #url(r'polls/', include('polls.url')),
    url(r'^admin/', admin.site.urls),
    url(r'polls/',include('polls.url',namespace='polls')),
    url(r"^blogs/",include('blogs.urls',namespace='blogs')),
    url(r'^auths/', include('auths.urls', namespace='auths')),
    url(r'^systems/',include('systems.urls',namespace='systems')),


]
'''

from django.conf.urls import url,include

from . import view

urlpatterns = [
    url(r'^$', view.hello),
    url(r'polls/',include('polls.url')),
]'''