from django.shortcuts import render
# Create your views here.
posts = [
    {
        'author':'CoreyMS',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted': 'Aug 27, 2018'
    
    },
    {
        'author':'EAGee',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted': 'April 8, 2021'
    
    }
]


def home(request):
    context = {'posts':posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})