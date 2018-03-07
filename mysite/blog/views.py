from django.shortcuts import render

# need this for the html file, I'm not really sure why
# the . before models means current directory, views and models are in the same
# directory
from .models import Post

from django.utils import timezone

# Create your views here.
# Takes request and returns a render function that will put together
# the template in blog/post_list.html
def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    # the 'posts' : posts
    return render(request, 'blog/post_list.html', {'posts': posts})
