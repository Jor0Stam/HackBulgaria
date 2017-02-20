from django import forms


class CreateCourseForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())
    start_date = forms.DateField(widget=forms.SelectDateWidget())
    end_date = forms.DateField(widget=forms.SelectDateWidget())


class EditCourseForm(forms.Form):
    old_name = forms.CharField()
    name = forms.CharField(required=False)
    description = forms.CharField(required=False, widget=forms.Textarea())
    start_date = forms.DateField(required=False, widget=forms.SelectDateWidget())
    end_date = forms.DateField(required=False, widget=forms.SelectDateWidget())
