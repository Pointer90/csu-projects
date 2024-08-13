from django import forms
from .models import Subprojects

class ShareProjectForm(forms.Form):
    style_fields = {
        'project':{
            'class': 'form-control border-0 border-bottom rounded-0 shadow-none',
            'name': 'title_project',
            'type': 'text',
            'id': 'floatingTitle',
            'placeholder': 'Название проекта'
        },
        'organization':{
            'class': 'form-control border-0 border-bottom rounded-0 shadow-none',
            'name': 'title_organization',
            'type': 'text',
            'id': 'floatingOrganization',
            'placeholder': 'Название организации'
        },
        'email':{
            'class': 'form-control border-0 border-bottom rounded-0 shadow-none',
            'name': 'email',
            'type': 'email',
            'id': 'floatingEmail',
            'placeholder': 'Email'
        },
        'vacancy':{
            'class': 'form-control border-0 border-bottom rounded-0 shadow-none',
            'name': 'vacancy',
            'type': 'text',
            'id': 'floatingVacancy',
            'placeholder': 'Кто необходим',
            'aria-describedby':'vacancyHelp'
        },
        'description':{
            'class': 'form-control border-0 border-bottom rounded-0 shadow-none',
            'name': 'description',
            'id': 'floatingDescription',
            'placeholder': 'Описание проекта',
            'aria-describedby':'descriptionHelp'
        }
}
    
    title_project = forms.CharField(
        label='Название проекта',
        widget=forms.TextInput(attrs=style_fields['project'])
    )

    title_organization = forms.CharField(
        label='Название организации', 
        widget=forms.TextInput(attrs=style_fields['organization'])
    )

    email = forms.EmailField(
        label='Email', 
        widget=forms.TextInput(attrs=style_fields['email'])
    )

    vacancy = forms.CharField(
        label='Кто необходим',
        help_text = 'Перечислите должности участников.', 
        widget=forms.TextInput(attrs=style_fields['vacancy'])
    )

    description = forms.CharField(
        label='Описание проекта',
        help_text = 'Кратко опишите идею своего проекта.',
        widget=forms.Textarea(attrs=style_fields['description'])
    )


class SubprojectForm(forms.Form):
    def __init__(self, pid, *args, **kwargs):
        super(SubprojectForm, self).__init__(*args, **kwargs)
        self.fields['title'] = forms.ModelChoiceField(
            queryset=Subprojects.objects.filter(pid=pid),
            label= 'Название подпроекта',
            empty_label= 'Выберите подпроект',
            widget= forms.Select(attrs={'class': 'form-select'})
        )

    style_fields = {
        'name':{
            'class': 'form-control border-0 border-bottom rounded-0 shadow-none',
            'name': 'name',
            'type': 'text',
            'id': 'floatingName',
            'placeholder': 'Имя'
        },
        'second_name':{
            'class': 'form-control border-0 border-bottom rounded-0 shadow-none',
            'name': 'second_name',
            'type': 'text',
            'id': 'floatingSecondName',
            'placeholder': 'Фамилия'
        },
        'group':{
            'class': 'form-control border-0 border-bottom rounded-0 shadow-none',
            'name': 'group',
            'type': 'text',
            'id': 'floatingGroup',
            'placeholder': 'Группа'
        },
        'email':{
            'class': 'form-control border-0 border-bottom rounded-0 shadow-none',
            'name': 'email',
            'type': 'text',
            'id': 'floatingEmail',
            'placeholder': 'Email'
        },
        'vacancy':{
            'class': 'form-control border-0 border-bottom rounded-0 shadow-none',
            'name': 'vacancy',
            'type': 'text',
            'id': 'floatingVacancy',
            'placeholder': 'Вакансия'
        },
        'description':{
            'class': 'form-control border-0 border-bottom rounded-0 shadow-none',
            'name': 'description',
            'type': 'text',
            'id': 'floatingDescription',
            'placeholder': 'О себе'
        }
    }
    
    name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(attrs=style_fields['name'])
    )
    second_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(attrs=style_fields['second_name'])
    )
    group = forms.CharField(
        label='Группа',
        widget=forms.TextInput(attrs=style_fields['group'])
    )
    email = forms.EmailField(
        label='Email', 
        widget=forms.TextInput(attrs=style_fields['email'])
    )
    vacancy = forms.CharField(
        label='Введите интересующую вас вакансию',
        widget=forms.TextInput(attrs=style_fields['vacancy'])
    )
    description = forms.CharField(
        label='О себе',
        help_text = 'Расскажите нам немного о себе',
        widget=forms.Textarea(attrs=style_fields['description'])
    )