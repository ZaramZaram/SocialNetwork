from django.urls import path
from .views import HomePage, PostDetailView


urlpatterns = [
                path('', HomePage.as_view(), name='homepage'),
                path('detail/', PostDetailView.as_view(), name='post_detail')
               ]
