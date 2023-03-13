from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Department
from .controllers.student import *
# Create your views here.
def home(request):
	return render(request, 'management/index.html')

def student_list(request):
	context = {}
	context['student_list'] = Student.objects.all().order_by('id')
	return render(request, 'management/student_list.html', context)

def student_add(request):
	context = {}
	errors = {}
	if request.method =='POST':
		errors = validate_form(request)
		if not errors:
			new_student = Student(
				id=request.POST['id'],
				name=request.POST['name'],
				email=request.POST['email'],
				mobile_number=request.POST['phone_number'],
				date_of_birth=request.POST['date_of_birth'],
				gpa=request.POST['gpa'],
				gender=request.POST['gender'],
				level=request.POST['level'],
				status=request.POST['status'],
			)
			new_student.save()
	if errors:
		context['errors'] = errors
	
	return render(request, 'management/student_add.html', context)

def student_edit(request, id):
	errors = {}
	context = {}

	try:
		student = Student.objects.get(id = id)
		context['student'] = student
	except Exception as e:
		errors['student_error'] = "Student ID doesn't exist"
		context["errors"] = errors
	if not errors and request.method == 'POST':
		errors = validate_edit_form(request, id)
		print(errors)
		if errors:
			context['errors'] = errors
		else:
			student.id = request.POST['id']
			student.name = request.POST['name']
			student.email = request.POST['email']
			student.mobile_number = request.POST['phone_number']
			student.date_of_birth = request.POST['date_of_birth']
			student.gpa = request.POST['gpa']
			student.gender = request.POST['gender']
			student.level = request.POST['level']
			student.status = request.POST['status']
			student.save()
	return render(request, 'management/student_edit.html', context)

def search(request):
	context = {}
	if request.method == 'GET' and 'search' in request.GET:
		student_results = None
		if request.GET['search'].isnumeric():
			student_results = Student.objects.filter(id=request.GET['search'])
		else:
			student_results = Student.objects.filter(name__contains = request.GET['search'])
		context['student_results'] = student_results
		print(context['student_results'])
	return render(request, 'management/search.html',  context)

def departments(request):
	context = {'departments' : Department.objects.all()}
	return render(request, 'management/departments.html', context)

def about(request):
	return render(request, 'management/about.html')
