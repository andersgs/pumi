from django.conf.urls import url, include
from django.contrib import admin

from pumi.views import IndexView

from rest_framework_nested import routers

from epidata.views import LoginView, AccountViewSet, EpidataViewSet

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'epidata', EpidataViewSet)

urlpatterns = [
    #url(r'^/', include('epidata.urls')),
    url(r'^api/v1', include(router.urls)),
    url(r'^api/v1/login/$',LoginView.as_view(), name='login'),
    #url(r'^admin/', admin.site.urls),
    url('^.*$', IndexView.as_view(),name='index')
]
