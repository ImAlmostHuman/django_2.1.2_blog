from django.shortcuts import render

posts = [
	{
	'author': 'Uschi',
	'title': 'I love Bones',
	'content': 'Content about bones',
	'date_posted': 'October 29, 2018'
	},
	{
	'author': 'Uschi',
	'title': 'More on Bones',
	'content': 'Some more content about bones',
	'date_posted': 'October 30, 2018'
	},
]

# Create your views here.
def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})