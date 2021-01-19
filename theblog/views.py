from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Ingredient
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    paginate_by = 2
    model = Post
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        ingredients = Ingredient.objects.order_by('blog_post')[:5]
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        context["ingredients"] = ingredients
        return context


def category_view(request, category):
    posts = Post.objects.filter(category=category)
    category_menu = Category.objects.all()
    return render(request, 'category-view.html', context={'category': category, 'posts': posts, 'category_menu': category_menu})


def search_view(request):
    if request.method == 'GET':
        search = request.GET.get('search_text')
        posts_title = Post.objects.filter(title__contains=search)
        posts_author_username = Post.objects.filter(author__username__contains=search)
        posts_title_tag = Post.objects.filter(title_tag__contains=search)
        posts_body = Post.objects.filter(body__contains=search)
        return render(request, 'search-view.html', context={'posts': posts_title, 'posts_author': posts_author_username,
                                                            'posts_title_tag': posts_title_tag, 'posts_body': posts_body})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article-details.html'

    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add-post.html'
    # fields = '__all__'
    # fields=('title', 'body')


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add-category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'update-post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('home')
