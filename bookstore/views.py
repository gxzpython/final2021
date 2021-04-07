from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.urls import reverse



def index(request):
    template = loader.get_template('bookstore/homepage.html')

    return HttpResponse(template.render({},request))
def signin(request):
    template = loader.get_template('bookstore/signin.html')

    return HttpResponse(template.render({},request))

def register(request):
    template = loader.get_template('bookstore/register.html')
    return HttpResponse(template.render({},request))
# http://127.0.0.1:8000/book-store/register/
  
# def register(request):
#     # if request.method =='POST':
#     #     register_form=RegisterForm(request.POST,request.FILES)
#     #     if register_form.is_valid():
#     #         register_form.save()
#     #     context={
#     #         "form": register_form,
#     #         "img_obj":register_form.instance
#     #     }
#         return render(request,'bookstore/register.html',context)
#     else:
#         register_form=RegisterForm()
#         return render(request,'bookstore/register.html',{'form':register_form})
