from django import forms
from . import models as boards_models


class BoardCreateForm(forms.ModelForm):
    class Meta:
        model = boards_models.Board
        fields = [
           "title",
            "content",
            "tag",
        ]
    tag = forms.ModelMultipleChoiceField(queryset=boards_models.Tag.objects.all(), widget=forms.CheckboxSelectMultiple,label="태그")
    def save(self):
        board = super().save(commit=False)
        return board


class TagSearchForm(forms.ModelForm):
    class Meta:
        model = boards_models.Tag
        fields = [
            "name"
        ]
    name = forms.ModelMultipleChoiceField(queryset=boards_models.Tag.objects.all(), widget=forms.CheckboxSelectMultiple,label="태그목록")