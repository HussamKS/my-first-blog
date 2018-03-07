from django.shortcuts import render

# Create your views here.
# Takes request and returns a render function that will put together
# the template in blog/post_list.html
def post_list(request):
    return render(request, 'blog/post_list.html', {})
