from django import forms
from .models import Column
from ckeditor.widgets import CKEditorWidget

class ColumnForm(forms.Form):
    title = forms.CharField(label='제목', max_length=100)
    content = forms.CharField(label='', widget = CKEditorWidget())

    class Meta:
        model = Column
        fields = ['title', 'content',]
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['title'].label = "제목"

    #     self.fields['title'].widget.attrs.update({
    #         # 'class': '클래스명',
    #         'placeholder': '제목',
    #     })

    #     self.fields['content'].widget.attrs.update({
    #         # 'class': '클래스명',
    #     })