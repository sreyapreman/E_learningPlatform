"""
URL configuration for ElearningSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/',views.CourseListView.as_view(),name="course-list"),
    path('<int:pk>/',views.CourseDetailView.as_view(),name='course-details'),
    path('add/',views.CourseAddView.as_view(),name='course-add'),
    path('update/<int:pk>/',views.CourseUpdateView.as_view(),name='course-update'),
    path('delete/<int:pk>/',views.CourseDeleteView.as_view(),name='course-delete'),


    path('index/',views.IndexView.as_view(),name='index'),
    path('quizz/',views.QuizView.as_view(),name='quizz'),

    path('demo/<int:pk>/',views.DemoVideoDetailView.as_view(),name='demovideo-detail'),
    path('demo/',views.DemoVideoAddView.as_view(),name='demovideo-add'),
    path('demo/update/<int:pk>/',views.DemoVideoUpdateView.as_view(),name='demovideo-edit'),
    path('demo/<int:pk>/remove/',views.DemoVideoDeleteView.as_view(),name='demovideo-delete'),
    path('demo/list/',views.DemoVideoListView.as_view(),name='demovideo-list'),






] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

