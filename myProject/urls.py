from django.contrib import admin
from django.urls import path,include
from app import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('studentapi',views.CRUDStudentView,basename='student')
router.register('teacherapi',views.CRUDTeacherView,basename='teacher')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
