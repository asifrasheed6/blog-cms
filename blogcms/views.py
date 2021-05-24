from django.views import generic
from blogcms.models import Post, Comment, Category, View
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
import json

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

        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')

        view = View(ipaddress = ip, post = kwargs['object'], timestamp = datetime.date(datetime.now()))
        view.save()

        context.update(
            {
                'post_list': Post.objects.all().filter(menu_item__gte=0).order_by('menu_item'),
                'post': kwargs['object'],
            }
        )
        return context

class Profile(generic.DetailView):
    template_name = 'blogcms/profile.html'
    model = User
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context.update(
            {
                'post_list': Post.objects.all().filter(menu_item__gte=0).order_by('menu_item'),
                'user': kwargs['object'],
            }
        )
        return context

class Categories(generic.DetailView):
    template_name = 'blogcms/category.html'
    model = Category
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(Categories, self).get_context_data(**kwargs)
        context.update(
            {
                'post_list': Post.objects.all().filter(menu_item__gte=0).order_by('menu_item'),
                'category': kwargs['object'],
            }
        )
        return context

class SignUp(generic.ListView):
    template_name = 'blogcms/signup.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.all().filter(menu_item__gte=0).order_by('menu_item')

class Stats(generic.ListView):
    template_name = 'blogcms/stats.html'
    context_object_name = 'post_stats'

    def get_queryset(self):
        return Post.objects.all().filter(page__exact = False).annotate(num_views = Count('view'))

def addComment(request):
    if request.user.is_authenticated and request.POST:
        if request.POST['comment_content'] != '':
            comment = Comment(post=Post.objects.all().filter(pk=int(request.POST['post_id'])).first(),
                          author=request.user, comment_date=datetime.now(),
                          comment_content=request.POST['comment_content'])
            comment.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER']+"#comments")
    return HttpResponseRedirect(reverse('cms:index'))

def addUser(request):
    if not request.user.is_authenticated and request.POST:
        form = request.POST
        user = User.objects.create_user(form['username'], form['email'], form['password'])
        user.first_name = form['first_name']
        user.last_name = form['last_name']
        user.is_staff = True
        user.save()
        print(user.is_staff)
        return HttpResponseRedirect('/accounts/login/?next=/')
    return HttpResponseRedirect(reverse('cms:index'))

