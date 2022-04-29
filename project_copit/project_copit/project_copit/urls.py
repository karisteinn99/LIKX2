"""project_copit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from courseselect.views import homepage, course_selection, big_check, check_ects_requirements
from courseselect.models import Course
from courseselect.checks import count_ects

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courselist/', homepage),
    path('', include('courseselect.urls')),
    path('course-selection', course_selection),
    path('course-selection',Course.get_prerequisite),
    path('course-selection',count_ects),
    path('course-selection', big_check),
]
