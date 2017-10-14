from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from job.ctrl.job import detail
from job.utils import json_helper
from job.ctrl import job


# Create your views here.

@csrf_exempt
def publish_job(request):
    job_type = request.POST['job_type']
    job_name = request.POST['job_name']
    work_type = request.POST['work_type']
    salary = request.POST['salary']
    job_key = request.POST['job_key']
    job_file_url = request.POST['job_file_url']
    # insert to db
    job.publish(job_key, job_name, job_type, work_type, job_file_url, salary)
    return HttpResponse(json_helper.dump_err_msg(0, 'published'))


@csrf_exempt
def add_job_attach(request):
    attach = request.FILES['job_attach']
    name = request.POST['att_name']
    ret, path = job.save_attach(name, attach)
    return HttpResponse(json_helper.dump_err_msg(0, path))


@csrf_exempt
def job_list(request):
    job_type = request.GET['job_type']
    job_name = request.GET['job_name']
    work_type = request.GET['work_type']
    page_num = request.GET['page_num']
    return HttpResponse(json_helper.dumps_err(0, job.job_list(job_type, work_type, job_name, page_num)))


@csrf_exempt
def job_detail(request):
    job_id = request.GET['id']
    job_obj = detail(job_id)
    return HttpResponse(json_helper.dumps_err(0, job_obj))


@csrf_exempt
def upload_resume(request):
    job_id = request.GET['job_id']
    resume_name = request.GET['resume_name']
    resume_attach = request.FILES['resume_attach']
    upload_resume(job_id, resume_name, resume_attach)
    return HttpResponse(json_helper.dump_err_msg(0, 'upload success'))