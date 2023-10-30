from django.db import models


class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.TextField(unique=True, blank=False, help_text="Название проекта")
    project_description = models.TextField(blank=False, help_text="Описание проекта")
    project_preview = models.ImageField(upload_to="CSUProjects/static/src/img/projects/", blank=True, help_text="Изображение проекта (необязательно)")

    def __str__(self):
        return self.project_name
    

class Subprojects(models.Model):
    subproject_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    subproject_name = models.CharField(max_length=100, unique=True, blank=False, help_text="Название подпроекта")
    subproject_description = models.TextField(help_text="Описание подпроекта")

    def __str__(self):
        return self.subproject_name
    

class Subproject_needs(models.Model):
    need_id = models.AutoField(primary_key=True)
    subproject_id = models.ForeignKey(Subprojects, on_delete=models.CASCADE)
    need_description = models.CharField(max_length=255, blank=False, help_text="Описание требований к студентам")
    need_profiles = models.CharField(max_length=255, help_text="Требуемые профили обучения")

    def __str__(self):
        return self.need_description
    
class Completed_projects(models.Model):
    comp_project_id = models.AutoField(primary_key=True)
    comp_project_name = models.CharField(max_length=255, blank=False, help_text="Название выполненного проекта")
    comp_project_description = models.CharField(max_length=255, help_text="Описание выполненного проекта")
    comp_project_preview = models.ImageField(upload_to="CSUProjects/static/src/img/compProjects/", blank=True, help_text="Изображение проекта (необязательно)")

    def __str__(self):
        return self.comp_project_name


class Workers(models.Model):
    worker_id = models.AutoField(primary_key=True)
    comp_project_id = models.ForeignKey(Completed_projects, on_delete=models.CASCADE)
    worker_full_name = models.CharField(max_length=127, blank=False)
    worker_post = models.CharField(max_length=127, blank=False)
    worker_description = models.TextField(blank=False)
    worker_photo = models.ImageField(upload_to="CSUProjects/static/src/img/compProjects/workers/", blank=False)

    def __str__(self):
        return self.worker_full_name