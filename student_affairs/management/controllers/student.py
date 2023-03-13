from django.http import HttpResponse
from django.core.validators import validate_email
from ..models import Student
import re

phone_number_pattern = "^\\+?[0-9]{7,14}$"

def validate_form(request):
	errors = {}
	#id
	if not('id' in request.POST and request.POST['id'] != ''):
		errors['id_error'] = "empty id field"
	elif Student.objects.filter(id=request.POST['id']).exists():
			errors['id_error'] = "id already exists"
	#name
	if not('id' in request.POST and request.POST['name'] != ''):
		errors['name_error'] = "empty name field"
	#email
	try:
		validate_email(request.POST['email'])
	except Exception as e:
		errors['email_error'] = str(e)
	#phone number
	if not re.match(phone_number_pattern, request.POST['phone_number']):
		errors['phone_number_error'] = "invalid phone number"
	#GPA
	try:
		gpa = request.POST['gpa']
		gpa = float(gpa)
		if gpa > 4 or gpa < 0:
			raise
	except:
		errors['gpa_error'] = 'invalid GPA'
	return errors	

def validate_edit_form(request, id):
	errors = {}
	#id
	if not('id' in request.POST and request.POST['id'] != ''):
		errors['id_error'] = "empty id field"
	try:
		post_id = Student.objects.get(id=request.POST['id'])
		if post_id.id != id:
			errors['id_error'] = "id already exists"
	except:
		pass
	#name
	if not('id' in request.POST and request.POST['name'] != ''):
		errors['name_error'] = "empty name field"
	#email
	try:
		validate_email(request.POST['email'])
	except Exception as e:
		errors['email_error'] = str(e)
	#phone number
	if not re.match(phone_number_pattern, request.POST['phone_number']):
		errors['phone_number_error'] = "invalid phone number"
	#GPA
	try:
		gpa = request.POST['gpa']
		gpa = float(gpa)
		if gpa > 4 or gpa < 0:
			raise
	except:
		errors['gpa_error'] = 'invalid GPA'
	return errors	