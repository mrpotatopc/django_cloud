from django.shortcuts import render
from .models import UserPartition,Folder,File,Cfolder
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView,DetailView,ListView,View
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy,reverse

# Create your views here.

class RedirectToPreviousMixin:

    default_redirect = '/'

    def get(self, request, *args, **kwargs):
        request.session['previous_page'] = request.META.get('HTTP_REFERER', self.default_redirect)
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return self.request.session['previous_page']


class HomepageView(LoginRequiredMixin,ListView):
    template_name='home/home.html'
    context_object_name ='partitions'
    model = UserPartition

    def get_queryset(self):
        return UserPartition.objects.filter(user=self.request.user)


@login_required
def PartitionView(request,id):
    P = UserPartition.objects.get(id=id)
    folder = P.folder_set.order_by('-id')
    context={
        'partition': P ,
        'Folders':folder
    }
    return render(request, 'home/partition.html',context)

@login_required
def FolderView(request,id1,id2):
    P = UserPartition.objects.get(id=id1)
    F = Folder.objects.get(id=id2)
    file = F.file_set.order_by('-id')
    chfolder = F.cfolder_set.order_by('-id')
    context={
        'folder':F,
        'files':file,
        'cfolders':chfolder
    }

    return render(request, 'home/folder.html',context)

@login_required
def CfolderView(request,id):
    F = Cfolder.objects.get(id=id)
    file = F.file_set.order_by('-id')
    chfolder = F.cfolder_set.order_by('-id')
    context={
        'folder':F,
        'files':file,
        'cfolders':chfolder
    }

    return render(request, 'home/cfolder.html',context)

class UserPartitionCreateView(LoginRequiredMixin,RedirectToPreviousMixin,CreateView):
    model = UserPartition
    action = 'create section'
    fields = ['name']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserPartitionCreateView, self).form_valid(form)

class FolderCreateView(LoginRequiredMixin,RedirectToPreviousMixin,CreateView) :
    model = Folder
    action = 'create Folder'
    fields = ['name']

    def form_valid(self, form):
        P = get_object_or_404(UserPartition, id=self.kwargs['id'])
        form.instance.partition = P
        return super(FolderCreateView, self).form_valid(form)

class CFolderCreateView1(LoginRequiredMixin,RedirectToPreviousMixin,CreateView) :
    model = Cfolder
    action = 'create Folder'
    fields = ['name']

    def form_valid(self, form):
        P = get_object_or_404(Folder, id=self.kwargs['id'])
        form.instance.pfolder1 = P
        return super(CFolderCreateView1, self).form_valid(form)

class CFolderCreateView2(LoginRequiredMixin,RedirectToPreviousMixin,CreateView) :
    model = Cfolder
    action = 'create Folder'
    fields = ['name']

    def form_valid(self, form):
        P = get_object_or_404(Cfolder, id=self.kwargs['id'])
        form.instance.pfolder2 = P
        return super(CFolderCreateView2, self).form_valid(form)



class CfolderFileCreateView(LoginRequiredMixin,RedirectToPreviousMixin,CreateView) :
    model = File
    action = 'add file'
    fields = ['file']

    def form_valid(self, form):
        F = get_object_or_404(Cfolder, id=self.kwargs['id'])
        form.instance.folder2 = F
        return super(CfolderFileCreateView, self).form_valid(form)

class FileCreateView(LoginRequiredMixin,RedirectToPreviousMixin,CreateView) :
    model = File
    action = 'add File'
    fields = ['file']

    def form_valid(self, form):
        F = get_object_or_404(Folder, id=self.kwargs['id2'])
        form.instance.folder = F
        return super(FileCreateView, self).form_valid(form)

class UserPartitionDeleteView(LoginRequiredMixin,RedirectToPreviousMixin,DeleteView):
    model = UserPartition
    action = 'delete section'

class FolderDeleteView(LoginRequiredMixin,RedirectToPreviousMixin,DeleteView):
    model = Folder
    action = 'delete folder'

class CfolderDeleteView(LoginRequiredMixin,RedirectToPreviousMixin,DeleteView):
    model = Cfolder
    action = 'delete folder'

class FileDeleteView(LoginRequiredMixin,RedirectToPreviousMixin,DeleteView):
    model = File
    action = 'delete file'

class UserPartitionUpdateView(LoginRequiredMixin,RedirectToPreviousMixin,UpdateView):
    model = UserPartition
    action = "rename section"
    fields = ['name']

class FolderUpdateView(LoginRequiredMixin,RedirectToPreviousMixin,UpdateView):
    model = Folder
    action = "rename folder"
    fields = ['name']
