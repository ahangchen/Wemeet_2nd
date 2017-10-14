from django.db import models


# Create your models here.
from job.ctrl.defines import SHORT_TEXT_LENGTH, LONGTEXT_MAX_LENGTH


class Job(models.Model):
    contact_mail = models.CharField(max_length=SHORT_TEXT_LENGTH)
    job_key = models.CharField(max_length=SHORT_TEXT_LENGTH)
    job_name = models.CharField(max_length=SHORT_TEXT_LENGTH)
    # 职位类型
    job_type = models.CharField(max_length=SHORT_TEXT_LENGTH)
    # 工作类型
    work_type = models.CharField(max_length=SHORT_TEXT_LENGTH)
    job_file_url = models.CharField(max_length=LONGTEXT_MAX_LENGTH)
    salary = models.CharField(max_length=SHORT_TEXT_LENGTH)
    # 职位描述让团队用畅言写