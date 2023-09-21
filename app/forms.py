from django import forms
from .models import Course, Demo_video

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'picture']


        widgets = {
    'title': forms.TextInput(attrs={'class': 'form-control '}),
    'description': forms.Textarea(attrs={'class': 'form-control'}),
    'picture': forms.FileInput(attrs={'class': 'form-control'}),     
     
    
} 

class DemoVideoForm(forms.ModelForm):
    class Meta:
        model = Demo_video
        fields = ['course', 'title', 'content', 'video_file']

        widgets = {
    'course': forms.Select(attrs={'class': 'form-control '}),
    'title': forms.TextInput(attrs={'class': 'form-control'}),
    'content': forms.Textarea(attrs={'class': 'form-control'}),
    'video_file': forms.FileInput(attrs={'class': 'form-control'}),     
     
    
} 