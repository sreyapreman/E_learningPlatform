from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,View,DeleteView,TemplateView
from django.utils.decorators import method_decorator

from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.views.decorators.cache import never_cache



from app.models import Course,Demo_video
from .forms import CourseForm,DemoVideoForm

from .models import Demo_video
from .forms import DemoVideoForm

from myaccount.decorators import signin_required,instructor_required


sadecks = [instructor_required, signin_required, never_cache]
decks =  [signin_required, never_cache]

@method_decorator(decks, name='dispatch')
class CourseListView(ListView):
    model=Course
    template_name="courses-list.html"
    context_object_name="courses"

@method_decorator(decks, name='dispatch')
class CourseDetailView(DetailView):
    model=Course
    template_name="course-details.html"
    context_object_name="course"

@method_decorator(sadecks, name='dispatch')
class CourseAddView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course-add.html'
    success_url = reverse_lazy('course-list')


    def dispatch(self, request, *args, **kwargs):
        # Check if the user is a staff member, if not, deny access
        if not self.request.user.is_staff:
            return HttpResponseForbidden("You don't have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)
    

@method_decorator(sadecks, name='dispatch')
class CourseUpdateView(UpdateView):
    form_class = CourseForm
    model = Course
    template_name = 'course-update.html'
    success_url = reverse_lazy('course-list')

@method_decorator(sadecks, name='dispatch')
class CourseDeleteView(View):
    def get(self,request,*args, **kwargs):
        id=kwargs.get('pk')
        Course.objects.get(id=id).delete()
        return redirect('course-list')


@method_decorator(decks, name='dispatch')
class DemoVideoListView(ListView):
    model = Demo_video
    template_name = 'demovideo-list.html'
    context_object_name = 'demovideos'


@method_decorator(sadecks, name='dispatch')
class DemoVideoAddView(CreateView):
    model = Demo_video
    form_class = DemoVideoForm
    template_name = 'demovideo-add.html'
    success_url = reverse_lazy('course-list')

@method_decorator(decks, name='dispatch')
class DemoVideoDetailView(DetailView):
    model = Demo_video
    template_name = 'demovideo-detail.html'
    context_object_name = 'demovideo'

@method_decorator(sadecks, name='dispatch')
class DemoVideoUpdateView(UpdateView):
    model = Demo_video
    form_class = DemoVideoForm
    template_name = 'demovideo-edit.html'
    success_url = reverse_lazy('demovideo-detail')


@method_decorator(sadecks, name='dispatch')
class DemoVideoDeleteView(DeleteView):
    model = Demo_video
    template_name = 'demovideo.html'
    success_url = reverse_lazy('demo_video_list')


class IndexView(TemplateView):
    template_name="index.html"

class QuizView(TemplateView):
    template_name="quizz.html"

