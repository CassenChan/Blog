from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

@require_GET
def main_page(request):
  return render(request, "main_page.html")


@require_GET
def school_page(request):
  return render(request, "school_page.html")


@require_GET
def project_page(request):
  return render(request, "project_page.html")


@require_GET
def skills_page(request):
  return render(request, "skills_page.html")


@require_GET
def work_page(request):
  return render(request, "work_page.html")
