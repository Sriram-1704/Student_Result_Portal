from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    student_class = models.CharField(max_length=10, verbose_name="Class")
    section = models.CharField(max_length=5)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.roll_no})"

class Subject(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()
    max_marks = models.IntegerField(default=100)

    class Meta:
        unique_together = ('student', 'subject')

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.marks_obtained}"