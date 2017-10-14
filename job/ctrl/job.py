import time

from job.ctrl.defines import LOCAL_HEADER
from job.models import Job
from job.utils.file_helper import save
from job.utils.smtp_mail import send_163_mail_attach


def publish(contact_mail, job_key, job_name, job_type, work_type, job_file_url, salary):
    Job.objects.update_or_create(contact_mail=contact_mail, job_key=job_key, job_name=job_name,
                                 job_type=job_type, work_type=work_type,
                                 job_file_url=job_file_url, salary=salary)
    return


def job_list(job_type, work_type, job_name, page_num):
    page_job_cnt = 20
    jobs = Job.objects.all().order_by('-id')[page_num * page_job_cnt: (page_num + 1) * page_job_cnt]

    return [{
        'id': job.id,
        'job_name': job.job_name,
        'job_type': job.job_type,
        'work_type': job.work_type,
        'job_file_url': job.job_file_url,
        'contact_mail': job.contact_mail,
        'salary': job.salary
    } for job in jobs]


def name2path(name):
    return LOCAL_HEADER + name


def save_attach(name, attach):
    name = str(time.time()).replace('.', '').replace(' ', '') + name
    name = name.replace(' ', '')
    path = name2path(name)
    save(attach, path)
    return path


def detail(id):
    job = Job.objects.filter(id=id).first()
    return {
        'id': job.id,
        'job_name': job.job_name,
        'job_type': job.job_type,
        'work_type': job.work_type,
        'job_file_url': job.job_file_url,
        'salary': job.salary,
        'contact_mail': job.contact_mail
    }


def upload_resume(job_id, resume_name, resume_attach):
    path = save_attach(resume_name, resume_attach)
    contact_mail = job = Job.objects.filter(id=job_id).first().contact_mail
    send_163_mail_attach('13660106752', 'xuegongban118',
                         contact_mail, '13660106752@163.com', 'WeMeet职位邮件', path)
    return True
