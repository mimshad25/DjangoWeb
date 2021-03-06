from django.shortcuts import render
from django.http import HttpResponse
from webpages.models import Contact

# Create your views here.
def home(request):
    return render(request, 'index.html', {'title':'Home Page Title'})
def contact(request):
    if (request.GET.get('method') == 'delete' and request.GET.get('id')):
     rec = Contact.objects.filter(id=request.GET.get('id'))
     rec.delete()

    if (request.GET.get('method') == 'edit' and request.GET.get('id')):
     cnt = Contact.objects.filter(id=request.GET.get('id')).get()
     return render(request,'edit.html', {'title':'Contact Page Title', 'row' : cnt})

    if(request.method == 'POST'):
        if(request.GET.get('method') == 'edit'):
            rec = Contact.objects.filter(id= request.GET.get('id'))
            rec.update(
                name = request.POST['name'],
                email = request.POST['email'],
                address = request.POST['address'],
                city = request.POST['city'],
                zipcode = request.POST['zipcode']
            )
        else:
         data = Contact(
         name = request.POST['name'],
         email = request.POST['email'],
         address = request.POST['address'],
         city = request.POST['city'],
         zipcode = request.POST['zipcode']
        )
        data.save()

    cnt = Contact.objects.all()
    return render(request, 'contact.html', {'title':'Contact Page Title', 'rows' : cnt})
def about(request):
    return render(request, 'about.html', {'title':'About Page Title'})

def member(request, id):
    return HttpResponse("<h1> Group Member ID: {}" .format(id))
def group(request):
    return HttpResponse("<h1> Group Members List </h1>")