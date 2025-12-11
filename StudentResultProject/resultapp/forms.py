from django import forms
from .models import Student, Result

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'})
        }

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['subject', 'marks_obtained', 'max_marks']