from django import forms
from myApp.models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        
        fields = [
            'name',
            'content',
        ]