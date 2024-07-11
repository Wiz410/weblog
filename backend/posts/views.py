from django.views.generic import TemplateView


class PostTemplateView(TemplateView):
    """Страница заглушка."""
    template_name = 'posts/post_list.html'
