from typing import List
from django.shortcuts import render
from django.urls.base import reverse_lazy
from . import models
from django.views.generic import (View, TemplateView, ListView, 
								DetailView, CreateView, DeleteView, 
								UpdateView)

# Create your views here.


class IndexView(TemplateView):
	template_name = "basic_app/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["injectme"] = "EVO MENE OVDE"
		return context
	


class SchoolListView(ListView):
	context_object_name = "schools"	# default is school_list
	model = models.School



class SchoolDetailView(DetailView):
	context_object_name = "school_detail"	# default is school
	model = models.School
	template_name = "basic_app/school_detail.html"


class SchoolCreateView(CreateView):
	fields = ("name", "principal", "location")
	model = models.School



class SchoolUpdateView(UpdateView):
	fields = ("name", "principal")
	model = models.School



class SchoolDeleteView(DeleteView):
	model = models.School
	success_url = reverse_lazy("basic_app:list")