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
        help_text='Ведите состояние (статус) проекта. По умолчанию статус - В процессе'
    )
    creation_date = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    updation_date = models.DateTimeField(
        'Дата изменения',
        auto_now=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
    
    def display_year(self):
        return self.creation_date.year
    display_year.short_description = 'Год создания'


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
        blank=False
    )

    def str(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'