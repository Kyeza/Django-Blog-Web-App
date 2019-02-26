from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# Create your views here.
def home(request):
	return render(request, 'blog/home.html')

class PostListView(ListView):
	"""docstring for PostListView"""
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	odering = ['-date_posted']

class PostDetailView(DetailView):
	"""docstring for PostDetailView"""
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	"""docstring for PostCreateView"""
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	"""docstring for PostUpdateView"""
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	"""docstring for PostDeleteView"""
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
