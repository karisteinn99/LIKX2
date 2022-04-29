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
<<<<<<< HEAD
from courseselect.views import homepage, course_selection, courses_by_semester
=======
from courseselect.views import homepage
from courseselect.views import course_selection
from courseselect.views import courses_by_semester
from courseselect.views import get_prerequisite
>>>>>>> bfcbccd13607c1329100e9fcf7bee61f00aad129

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courselist/', homepage),
    path('', include('Student.urls')),
    path('course-selection', course_selection),
    path('course-selection',get_prerequisite),
    path('semester-test',courses_by_semester),
]
