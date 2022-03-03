from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        label = {'id_group': 'Группа', 'id_text': 'Текст поста'}
        help_texts = {'group': 'Выберите группу', 'text': 'Введите ссообщение'}
        fields = ('text', 'group')
