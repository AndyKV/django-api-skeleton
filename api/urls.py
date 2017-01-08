from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('user.urls', namespace='user')),
]

if settings.DEBUG is False:   #if DEBUG is True it will be served automatically
    urlpatterns += url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

if settings.DEBUG:
	from rest_framework_swagger.views import get_swagger_view
	schema_view = get_swagger_view(title='API')
	urlpatterns += url(r'^api/docs$', schema_view),
