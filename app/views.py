from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def naga(request):
    forms=StudentForm()
    d={'forms':forms}
    if request.method=='POST':
        forms_data=StudentForm(request.POST)
        if forms_data.is_valid():
            a=forms_data.cleaned_data['s_id']
            b=forms_data.cleaned_data['s_name']
            c=forms_data.cleaned_data['s_class']
            d=forms_data.cleaned_data['s_fa']
            g=forms_data.cleaned_data['s_marks']
            
            T=Student.objects.get_or_create(s_id=a,s_name=b,s_class=c,s_fa=d,s_marks=g)[0]
            T.save()
            H=Student.objects.all()
            d1={'H':H}
            return render(request,'brock.html',d1)
    
    return render(request,'naga.html',d)