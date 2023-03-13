from django.db import models

class Department(models.Model):
	name = models.CharField(max_length=200)
	short = models.CharField(max_length=10)
	def __str__(self) -> str:
		return self.name
# Create your models here.
class Student(models.Model):
	GENDER_CHOICES = (
		('M', 'Male'),
		('F', 'Female'),
	)
	STATUS_CHOICES = (
		("active", "active"),
		("inactive", "inactive")
	)
	LEVEL_CHOICES = (
		("1", "First Level"),
		("2", "Second Level"),
		("3", "Third Level"),
		("4", "Fourth Level"),
	)
	id = models.PositiveIntegerField(primary_key=True)
	name = models.CharField(max_length=200, null=False)
	email = models.EmailField(max_length = 254, null=True)
	date_of_birth = models.DateField(max_length=12, null=False)
	gpa = models.DecimalField(decimal_places=6, max_digits=7)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False)
	level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='1', null=False)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=False)
	department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, default=5)
	mobile_number = models.CharField(max_length=12, null=True)
	def __str__(self) -> str:
		return self.name + ', ' + str(self.id)

