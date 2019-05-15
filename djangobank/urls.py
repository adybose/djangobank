
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from accounts.views import MyView

from core.views import home, about

urlpatterns = [
    url('admin', admin.site.urls),
    url('login', MyView.login_view, name='login'),
    url('register', MyView.register_view, name='register'),
    url('logout', MyView.logout_view, name='logout'),

    url(r'^$', home, name='home'),


    url(r'^', include('transactions.urls', namespace='transactions')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
        )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
        )
