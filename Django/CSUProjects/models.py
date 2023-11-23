from tabnanny import verbose
from typing import Self
from django.db import models


class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(
        max_length=80,
        unique=True,
        blank=False,
        verbose_name='Название проекта'
    )
    project_description = models.TextField(
        blank=False,
        verbose_name='Краткое описание'
    )
    project_preview = models.ImageField(
        upload_to='previews/',
        blank=True,
        help_text='*необязательное поле',
        verbose_name='Превью проекта'
    )
    project_created = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата создания'
    )

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def mediaExists(self):
        try:
            result = self.project_preview.url
        except:
            return False
        return True


class SubProjects(models.Model):
    subproject_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(
        Projects,
        on_delete=models.CASCADE,
        help_text='Необходимо указать к какому проекту принадлежит',
        verbose_name='Идентификатор проекта'
    )
    subproject_name = models.CharField(
        max_length=80,
        unique=True,
        blank=False,
        help_text='Название подпроекта',
        verbose_name='Название подпроекта'
    )
    subproject_description = models.TextField(
        help_text='Краткое описание проекта',
        verbose_name='Описание'
    )
    subproject_created = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата создания'
    )

    def __str__(self):
        return self.subproject_name

    class Meta:
        verbose_name = 'Подпроект'
        verbose_name_plural = 'Подпроекты'


class SubProjectNeeds(models.Model):
    need_id = models.AutoField(primary_key=True)
    subproject_id = models.ForeignKey(
        SubProjects,
        on_delete=models.CASCADE,
        verbose_name='Название проекта'
    )
    need_description = models.TextField(
        max_length=255,
        blank=False,
        help_text='Краткое описание требований',
        verbose_name='Требования к работнику'
    )
    need_profiles = models.CharField(
        max_length=80,
        help_text='Требуемые профили обучения',
        verbose_name='Специальность'
    )

    def __str__(self):
        return self.need_description

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class CompletedProjects(models.Model):
    comp_project_id = models.AutoField(primary_key=True)
    comp_project_name = models.CharField(
        max_length=255,
        blank=False,
        verbose_name='Название проекта'
    )
    comp_project_description = models.TextField(
        max_length=255,
        help_text='Краткое описание выполненного проекта',
        verbose_name='Описание'
    )
    comp_project_preview = models.ImageField(
        upload_to='previews/',
        blank=True,
        help_text='*необязательное поле',
        verbose_name='Превью проекта'
    )
    comp_project_created = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата создания'
    )

    def __str__(self):
        return self.comp_project_name

    class Meta:
        verbose_name = 'Выполенный проект'
        verbose_name_plural = 'Выполненные проекты'

    def mediaExists(self):
        try:
            result = self.project_preview.url
        except:
            return False
        return True


class Workers(models.Model):
    worker_id = models.AutoField(primary_key=True)
    worker_full_name = models.CharField(
        max_length=80,
        blank=False,
        verbose_name='Имя'
    )
    worker_photo = models.ImageField(
        upload_to='peoples/',
        blank=False,
        verbose_name='Фото'
    )

    def __str__(self):
        return self.worker_full_name

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'


class WorkersInProject(models.Model):

    w_p_id = models.AutoField(primary_key=True)
    worker_id = models.ForeignKey(
        Workers, on_delete=models.CASCADE, verbose_name='ФИО')
    comp_project_id = models.ForeignKey(
        CompletedProjects,
        on_delete=models.CASCADE,
        verbose_name='Название проекта'
    )
    models.UniqueConstraint(
        fields=['comp_project_id', 'worker_id'],
        name='worker_in_project'
    )
    worker_post = models.CharField(
        max_length=80,
        blank=False,
        verbose_name='Должность'
    )
    worker_description = models.TextField(
        max_length=255,
        blank=False,
        help_text='Краткое описание чем занимался в проекте',
        verbose_name='Описание'
    )

    def __str__(self):
        return f'{self.worker_id} {self.comp_project_id}'

    class Meta:
        verbose_name = 'Участник проекта'
        verbose_name_plural = 'Участники проекта'

    def isEven(self):
        return self.w_p_id % 2 == 0 if True else False
