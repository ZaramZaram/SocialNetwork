from django.urls import path
from .views import HomePage, PostDetailView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
                path('home/', HomePage.as_view(), name='homepage'),
                path('detail/', PostDetailView.as_view(), name='post_detail')
               ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
