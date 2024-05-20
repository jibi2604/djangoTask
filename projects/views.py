from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

# Create your views here.


def project_list(request):

    projects = Project.objects.all()
    return render(request, 'project/project_list.html', {'projects': projects})


def project_detail(request, pk):

    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project/project_detail.html', {'project': project})


@login_required
def project_create(request):

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('project:project_list')
    else:
        form = ProjectForm()
    return render(request, 'project/project_form.html', {'form': form})


@login_required
def project_update(request, pk):

    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project:project_detail', pk=pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project/project_form.html', {'form': form})


@login_required
def project_delete(request, pk):

    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project:project_list')
    return render(request, 'project/project_confirm_delete.html', {'project': project})
