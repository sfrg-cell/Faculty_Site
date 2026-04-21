from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50)
    head = models.CharField(max_length=50)


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   related_name="teachers")


class Program(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    description = models.TextField()
    coordinator = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    coordinator_email = models.EmailField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE,
                                   related_name="programs")


class Discipline(models.Model):
    name = models.CharField(max_length=50)
    program = models.ForeignKey(Program, on_delete=models.CASCADE,
                                related_name="disciplines")


class HomePageText(models.Model):
    title = models.CharField(max_length=100)
    faculty = models.TextField()
    programs = models.TextField()
    teachers = models.TextField()
    international = models.TextField()
    contacts = models.TextField()
