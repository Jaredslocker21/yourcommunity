from .models import Member, Comment
from django_summernote.widgets import SummernoteInplaceWidget
from django import forms


class MemberForm(forms.ModelForm):
    """
    Member Input Form
    """
    class Meta:
        """
        Meta class
        """
        model = Member
        fields = [
            'role',
            'author',
            'user_email',
            'featured_image',
            'description',
                        
        ]
        widgets = {
            'Member': SummernoteInplaceWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
