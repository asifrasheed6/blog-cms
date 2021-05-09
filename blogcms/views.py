from django.views import generic
from blogcms.models import Post

# Create your views here.
class Index(generic.ListView):
    template_name = 'blogcms/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.all().order_by('menu_item', '-published_on')

class PostView(generic.DetailView):
    template_name = 'blogcms/post.html'
    model = Post
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context.update(
            {
                'post_list': Post.objects.all().filter(menu_item__gte=0).order_by('menu_item'),
                'post': kwargs['object'],
            }
        )
        return context