from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView,DetailView,ListView,View
# Create your views here.
class HomepageView(TemplateView):
    template_name='home/home.html'
