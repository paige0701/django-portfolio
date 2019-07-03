from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CreateForm

# Create your views here.
from projects.models import Project


@login_required
def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


@login_required
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)


def create_project(request):
    if request.method == "GET":
        create_form = CreateForm()
        return render(request, 'create_project.html', {'form': create_form})
    else:
        project = Project()
        data = request.POST.copy()

        project.title = data.get('title')
        project.description = data.get('description')
        project.technology = data.get('technology')
        project.image = data.get('image')
        project.author = request.user

        project.save()
        return redirect('project_index')


