from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'index',views.Index.as_view()),
    url(r'task',views.Task.as_view()),
    url(r'school_delete_search', views.School_delete_search.as_view()),
    url(r'school', views.School.as_view()),
    url(r'province',views.province),
    url(r'city',views.city),
    url(r'education', views.Edu.as_view()),
    url(r'edu',views.edu),


]