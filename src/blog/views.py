from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from blog.models import BlogPost


class BlogHome(ListView):
    """ ListView cherche automatiquement pour nomdumodele_list.html"""

    model = BlogPost
    context_object_name = "blog"

    def get_queryset(self):

        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset

        return queryset.filter(published=True)


class BlogPostCreate(LoginRequiredMixin, CreateView):

    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = BlogPost
    template_name = 'blog/blogpost_create.html'
    # template_name définit le path du template, par défault "modelname_form.html"
    fields = ['title', 'content', ]


class BlogPostEdit(LoginRequiredMixin, UpdateView):
    """ default file name : modelname_edit.html"""
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = BlogPost
    template_name = 'blog/blogpost_edit.html'
    fields = ['title', 'content', 'published', ]


class BlogPostDetail(DetailView):
    """ default file name : modelname_detail.html"""
    model = BlogPost
    context_object_name = "post"


class BlogPostDelete(LoginRequiredMixin, DeleteView):
    """ default file name : nomdumodele_confirm_delete.html"""
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    model = BlogPost
    success_url = reverse_lazy("posts:blog")
