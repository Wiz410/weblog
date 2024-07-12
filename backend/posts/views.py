from django.views.generic import ListView
from django.contrib.auth import get_user_model

from core import constants

User = get_user_model()


class PostListView(ListView):
    """Страница заглушка."""
    model = User
    template_name = 'posts/post_list.html'
    paginate_by = constants.OBJECTS_PER_PAGE
