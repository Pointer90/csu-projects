from django.db import models

StatusProjectEnum = (
    ('notComplete', 'Не выполнен'),
    ('partial', 'В процессе'),
    ('complete', 'Выполнен')
)

class Projects(models.Model):
    prj_id = models.AutoField(primary_key=True)
    prj_name = models.CharField(
        max_length=80,
        unique=True,
        blank=False,
        verbose_name='Название проекта'
    )
    prj_description = models.TextField(
        blank=False,
        verbose_name='Краткое описание'
    )
    prj_preview = models.ImageField(
        upload_to='previews/',
        blank=True,
        help_text='*необязательное поле',
        verbose_name='Превью проекта'
    )
    prj_created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    prj_updated = models.DateTimeField(
        'Дата изменения',
        auto_now=True
    )

    status = models.CharField(
        'Статус', 
        max_length= 11, 
        choices=StatusProjectEnum, 
        default='notComplete',
        help_text=' Введите статус готовности (по умолчанию статус не готов)'
    )

    def __str__(self):
        return self.prj_name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def mediaExists(self):
        try:
            result = self.prj_preview.url
        except:
            return False
        return True
    
    def display_year(self):
        return self.prj_created.year
    display_year.short_description = 'Год создания'


class SubProjects(models.Model):
    subprj_id = models.AutoField(primary_key=True)
    prj_id = models.ForeignKey(
        Projects,
        on_delete=models.CASCADE,
        help_text='Необходимо указать к какому проекту принадлежит',
        verbose_name='Идентификатор проекта'
    )
    subprj_name = models.CharField(
        'Название подпроекта',
        max_length=80,
        unique=True,
        blank=False,
        help_text='Название подпроекта'
    )
    subprj_description = models.TextField(
        'Описание',
        help_text='Краткое описание проекта'
    )
    subprj_preview = models.ImageField(
        upload_to='previews/',
        blank=True,
        help_text='*необязательное поле',
        verbose_name='Превью проекта'
    )
    subprj_created = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    subprj_updated = models.DateTimeField(
        'Дата изменения',
        auto_now=True
    )
    status = models.CharField(
        'Статус', 
        max_length= 11, 
        choices=StatusProjectEnum, 
        default='notComplete',
        help_text=' Введите статус готовности (по умолчанию статус не готов)'
    )

    class Meta:
        verbose_name = 'Подпроект'
        verbose_name_plural = 'Подпроекты'

    def __str__(self):
        return self.subprj_name


class SubProjectNeeds(models.Model):
    need_id = models.AutoField(primary_key=True)
    subprj_id = models.ForeignKey(
        SubProjects,
        on_delete=models.CASCADE,
        verbose_name='Название проекта'
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
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class WorkersInProject(models.Model):

    w_p_id = models.AutoField(primary_key=True)
    worker_id = models.ForeignKey(
        Workers, on_delete=models.CASCADE, verbose_name='ФИО')
    prj_id = models.ForeignKey(
        Projects,
        on_delete=models.CASCADE,
        verbose_name='Название проекта'
    )
    models.UniqueConstraint(
        fields=['prj_id', 'worker_id'],
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

    class Meta:
        verbose_name = 'Участник проекта'
        verbose_name_plural = 'Участники проекта'

    def __str__(self):
        return f'{self.worker_id} {self.prj_id}'


    def isEven(self):
        return self.w_p_id % 2 == 0 if True else False
