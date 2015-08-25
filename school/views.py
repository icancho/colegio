from django.shortcuts import render
from school.models import *


def school_first(request):
	template = 'school_view.html'

	school_data = School.objects.all()
	return render(request, template, {
		'school_data': school_data,
	})

		
# Create your views here.
