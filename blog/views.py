from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.models import BlogPost
from django.urls import reverse_lazy, reverse

class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)

class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'description')
    success_url = reverse_lazy('blog:blog_list')

class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])

    def get_object(self, queryset=None):

        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ('title', 'description')
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blog:blog_list')


class ContactView(TemplateView):
    template_name = 'blog/blog_contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)