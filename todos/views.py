from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse


from .models import TodoItem


def item_list(request):
    todos = TodoItem.objects.all()
    context = {
        'todos':todos
    }
    return render(request, 'index.html', context)


def details(request, pk):
    todo = TodoItem.objects.get(pk=pk)
    context = {
        'todo':todo
    }
    return render(request, 'details.html', context)


def imp(request):
    return render(request, 'imp.html')


def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        description = request.POST['description']
        progress = request.POST['progress']

        todo = TodoItem(title=title, description=description, progress=progress)
        todo.save()

        return redirect('../..')

    else:
        return render(request, 'add.html')



def edit(request, pk):
    todo = TodoItem.objects.get(pk=pk)
    context = {
        'todo':todo
    }

    if(request.method == 'POST'):
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        todo.progress = request.POST['progress']

        todo.save()

        return redirect('../../..')
    else:
        return render(request, 'edit.html', context)

def delete(request, pk):
    todo = TodoItem.objects.get(pk=pk)
    context = {
        'todo':todo
    }

    if(request.method == 'POST'):
        todo.delete()

        return redirect('../../..')
    else:
        return render(request, 'delete.html', context)


'''
class TodoItemCreateView(LoginRequiredMixin, CreateView):
	fields = ('title', 'description', 'progress',)
	model = TodoItem

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def get_success_url(self):
		return self.object.get_absolute_url()

class TodoItemDetailView(LoginRequiredMixin, DetailView):
	model = TodoItem

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(owner=self.request.user)

class TodoItemUpdateView(LoginRequiredMixin, UpdateView):
	fields = ('title', 'description', 'progress',)
	model = TodoItem

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(owner=self.request.user)

	def get_success_url(self):
		return self.object.get_absolute_url()


class TodoItemDeleteView(DeleteView):
	model = TodoItem
	success_url = reverse_lazy('todo:list')

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(owner=self.request.user)

class TodoItemListView(LoginRequiredMixin, ListView):
	model = TodoItem

	def get_queryset(self):
		queryset = super().get_queryset()
		return queryset.filter(owner=self.request.user)
'''
