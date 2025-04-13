from django.shortcuts import render

posts = [
    {
        'author': 'Chinazom',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 13, 2025'
    },
    
    {
        'author': 'Omenife',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 14, 2025'
    }
    
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html')

