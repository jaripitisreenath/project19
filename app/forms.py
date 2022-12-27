from django import forms
l=[(1,1),(2,2,),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)]

class StudentForm(forms.Form):
    s_id=forms.IntegerField()
    s_name=forms.CharField(max_length=100)
    s_class=forms.ChoiceField(choices=l)
    s_fa=forms.CharField(max_length=100)
    s_marks=forms.IntegerField()
    