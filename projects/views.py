from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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
