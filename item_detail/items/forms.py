from django import forms
from .models import SearchComment
class CommentForm(forms.ModelForm):
    class Meta:
        model = SearchComment
        fields = ['comment_content']
        labels = {
            'comment_content': '댓글내용',
        }

#update, delete form
class UDForm(forms.Form):
    UD = forms.CharField(label='UD', max_length=10)