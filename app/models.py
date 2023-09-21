from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    picture=models.ImageField(upload_to="images",blank=True,null=True)

    def __str__(self):
        return self.title

class Demo_video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    video_file = models.FileField(upload_to='videos', blank=True, null=True)  # Define the upload_to directory
    # Add more fields for quizzes, assignments, etc.

    def __str__(self):
        return self.title
    


