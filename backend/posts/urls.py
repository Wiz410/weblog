from django.urls import path
from .views import PostTemplateView

app_name = 'posts'

urlpatterns = [
    path(
        '',
        PostTemplateView.as_view(),
        name='list'
    ),
]
