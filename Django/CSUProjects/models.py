from django.db import models


class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(
        'Название проекта',
        max_length=80,
        unique=True,
        blank=False
    )
    project_description = models.TextField(
        'Краткое описание',
        blank=False
    )
    project_preview = models.ImageField(
        'Превью проекта',
        upload_to='previews/',
        blank=True,
        help_text='*необязательное поле'
    )
    project_created = models.DateTimeField(
        'Дата создания',
        auto_now=True
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
        verbose_name='Идентификатор проекта',
        on_delete=models.CASCADE,
        help_text='Необходимо указать к какому проекту принадлежит',
    )
    subproject_name = models.CharField(
        'Название подпроекта',
        max_length=80,
        unique=True,
        blank=False,
        help_text='Название подпроекта'
    )
    subproject_description = models.TextField(
        'Описание',
        help_text='Краткое описание проекта'
    )
    subproject_created = models.DateTimeField(
        'Дата создания',
        auto_now=True
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
        verbose_name='Название проекта',
        on_delete=models.CASCADE
    )
    need_description = models.TextField(
        'Требования к работнику',
        max_length=255,
        blank=False,
        help_text='Краткое описание требований'
    )
    need_profiles = models.CharField(
        'Специальность',
        max_length=80,
        help_text='Требуемые профили обучения'
    )

    def __str__(self):
        return self.need_description

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class CompletedProjects(models.Model):
    comp_project_id = models.AutoField(primary_key=True)
    comp_project_name = models.CharField(
        'Название проекта',
        max_length=255,
        blank=False
    )
    comp_project_description = models.TextField(
        'Описание',
        max_length=255,
        help_text='Краткое описание выполненного проекта'
    )
    comp_project_preview = models.ImageField(
        'Превью проекта',
        upload_to='previews/',
        blank=True,
        help_text='*необязательное поле'
    )
    comp_project_created = models.DateTimeField(
        'Дата создания',
        auto_now=True
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
        'Имя',
        max_length=80,
        blank=False
    )
    worker_photo = models.ImageField(
        'Фото',
        upload_to='peoples/',
        blank=False
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
        verbose_name='Название проекта',
        on_delete=models.CASCADE
    )
    models.UniqueConstraint(
        fields=['comp_project_id', 'worker_id'],
        name='worker_in_project'
    )
    worker_post = models.CharField(
        'Должность',
        max_length=80,
        blank=False
    )
    worker_description = models.TextField(
        'Описание',
        max_length=255,
        blank=False,
        help_text='Краткое описание чем занимался в проекте'
    )

    def __str__(self):
        return f'{self.worker_id} {self.comp_project_id}'

    class Meta:
        verbose_name = 'Участник проекта'
        verbose_name_plural = 'Участники проекта'

    def isEven(self):
        return self.w_p_id % 2 == 0 if True else False
