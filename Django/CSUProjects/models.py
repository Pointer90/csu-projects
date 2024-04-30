from django.db import models

ProjectStatusesEnum = (
    ('completed', 'Выполнен'),
    ('quickly', 'Срочно'),
    ('full', 'Набор окончен'),
    ('process', 'В процессе'),
    ('frozen', 'Заморожен'),
)

class Projects(models.Model):
    pid = models.AutoField(primary_key=True)
    title = models.CharField(
        'Название проекта',
        max_length=80,
        unique=True,
        blank=False
    )
    description = models.TextField(
        'Описание проекта',
        blank=False
    )
    photo = models.ImageField(
        upload_to='previews/',
        blank=True,
        help_text='*необязательное поле',
        verbose_name='Превью проекта'
    )
    status = models.CharField(
        'Статус',
        max_length=14,
        choices=ProjectStatusesEnum,
        default='process',
        help_text='Выберите состояние (статус) проекта'
    )
    creation_date = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    updation_date = models.DateTimeField(
        'Дата изменения',
        auto_now=True
    )
    phone = models.CharField(
        'Номер телефона руководителя',
        blank=False,
        max_length=14
    )
    link = models.URLField(
        'Ссылка на сайт проекта',
        blank=True,
        help_text='*необязательное поле'
    )


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def display_year(self):
        return self.creation_date.year
    display_year.short_description = 'Год создания'

    def mediaExists(self):
        try:
            result = self.photo.url
        except:
            return False
        return True

class Workers(models.Model):
    wid = models.AutoField(primary_key=True)
    name = models.CharField(
        'ФИО',
        max_length=80,
        blank=False
    )
    photo = models.ImageField(
        'Фото',
        upload_to='peoples/',
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def mediaExists(self):
        try:
            result = self.photo.url
        except:
            return False
        return True

class Subprojects(models.Model):
    sid = models.AutoField(primary_key=True)
    pid = models.ForeignKey(
        Projects,
        on_delete=models.CASCADE,
        help_text='Необходимо указать к какому проекту принадлежит',
        verbose_name='Идентификатор проекта'
    )
    title = models.CharField(
        'Название подпроекта',
        max_length=80,
        unique=True,
        blank=False,
        help_text='Название подпроекта'
    )
    description = models.TextField(
        'Описание',
        max_length=255,
        help_text='Краткое описание подпроекта'
    )
    photo = models.ImageField(
        upload_to='previews/',
        blank=True,
        help_text='*необязательное поле',
        verbose_name='Превью проекта'
    )
    creation_date = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    updation_date = models.DateTimeField(
        'Дата изменения',
        auto_now=True
    )
    status = models.CharField(
        'Статус', 
        max_length=14, 
        choices=ProjectStatusesEnum, 
        default='process',
        help_text='Выберите состояние (статус) подпроекта'
    )

    class Meta:
        verbose_name = 'Подпроект'
        verbose_name_plural = 'Подпроекты'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/admin/CSUProjects/subprojects/{self.sid}'
    
class Vacancies(models.Model):
    vid = models.AutoField(primary_key=True)
    sid =models.ForeignKey(
        Subprojects,
        on_delete=models.CASCADE,
        verbose_name='Название подпроекта'
    )
    post = models.CharField(
        'Специальность',
        max_length=80,
        help_text='Требуемые профили обучения'
    )
    description = models.TextField(
        'Требование к работнику',
        max_length=255,
        blank=False,
        help_text='Краткое описание требований'
    )

    def str(self):
        return self.description

    class Meta:
        verbose_name = 'Вакансия',
        verbose_name_plural = 'Вакансии'

class WorkersInSubprojects(models.Model):
    wsid = models.AutoField(primary_key=True)
    sid = models.ForeignKey(
        Subprojects,
        verbose_name = 'Название подпроекта',
        on_delete = models.CASCADE,
        help_text='Необходимо указать к какому подпроекту принадлежит'
    )
    wid = models.ForeignKey(
        Workers,
        verbose_name = 'Имя участника',
        on_delete = models.CASCADE,
        help_text='Необходимо указать кто участвует в проекте'
    )

    post = models.CharField(
        'Должность',
        max_length = 80,
        blank = False
    )

    description = models.TextField(
        'Описание',
        max_length = 255,
        blank=False
    )

    def str(self):
        return f'{self.wid} {self.sid}'
    
    def get_absolute_url(self):
        return f'/admin/CSUProjects/workers/{self.wsid}'

    class Meta:
        verbose_name = 'Исполнитель в подпроекте'
        verbose_name_plural = 'Исполнители в подпроектах'