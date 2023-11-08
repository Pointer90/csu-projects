from django.db import models


class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.TextField(unique=True, blank=False, help_text="Название проекта")
    project_description = models.TextField(blank=False, help_text="Описание проекта")
    project_preview = models.ImageField(upload_to="previews/", blank=True, help_text="Изображение проекта (необязательно)")

    def __str__(self):
        return self.project_name

    def mediaExists(self):
        try:
            result = self.project_preview.url
        except:
            return False
        return True
    

class SubProjects(models.Model):
    subproject_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    subproject_name = models.CharField(max_length=100, unique=True, blank=False, help_text="Название подпроекта")
    subproject_description = models.TextField(help_text="Описание подпроекта")

    def __str__(self):
        return self.subproject_name
    

class SubProjectNeeds(models.Model):
    need_id = models.AutoField(primary_key=True)
    subproject_id = models.ForeignKey(SubProjects, on_delete=models.CASCADE)
    need_description = models.CharField(max_length=255, blank=False, help_text="Описание требований к студентам")
    need_profiles = models.CharField(max_length=255, help_text="Требуемые профили обучения")

    def __str__(self):
        return self.need_description
    
class CompletedProjects(models.Model):
    comp_project_id = models.AutoField(primary_key=True)
    comp_project_name = models.CharField(max_length=255, blank=False, help_text="Название выполненного проекта")
    comp_project_description = models.CharField(max_length=255, help_text="Описание выполненного проекта")
    comp_project_preview = models.ImageField(upload_to="previews/", blank=True, help_text="Изображение проекта (необязательно)")

    def __str__(self):
        return self.comp_project_name
    
    def mediaExists(self):
        try:
            result = self.project_preview.url
        except:
            return False
        return True

class Workers(models.Model):
    worker_id = models.AutoField(primary_key=True)
    worker_full_name = models.CharField(max_length=100, blank=False)
    worker_photo = models.ImageField(upload_to="peoples/", blank=False)

    def __str__(self):
        return self.worker_full_name

class WorkersInProject(models.Model):

    w_p_id = models.AutoField(primary_key=True)
    worker_id = models.ForeignKey(Workers, on_delete=models.CASCADE)
    comp_project_id = models.ForeignKey(CompletedProjects, on_delete=models.CASCADE)
    models.UniqueConstraint(fields=['comp_project_id', 'worker_id'], name='worker_in_project')
    worker_post = models.CharField(max_length= 80, blank= False)
    worker_description = models.CharField(max_length= 255, blank= False)

    def __str__(self):
        return f'{self.worker_id} {self.comp_project_id}'

    def isEven(self):
        return self.w_p_id % 2 == 0 if True else False