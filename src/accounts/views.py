from django.shortcuts import render
from django.http import HttpResponse
from excel_data.tool import OpenExcel
from django.views import generic
from .forms import (
    UserCreationForm, 
)

# Create your views here.

def home(request):
    root='C:\\Dropbox\\Dropbox\\PTK Nepal\\Operation\\Finance\\DebtsCredits_Book'
    df=OpenExcel().from_folder(root,'VatBills_Sales')
    context={}
    return render(request,'base.html',context)

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse("login")

