from django.conf.urls import url
from job import views

urlpatterns = [
    url(r'^publish_job/$', views.publish_job),
    url(r'^add_job_attach/$', views.add_job_attach),
    url(r'^job_list/$', views.job_list),
    url(r'^job_detail/$', views.job_detail),
    url(r'^upload_resume/$', views.upload_resume),
]