from django.shortcuts import render

from .forms import ContactForm

def home_view(request):
    template = 'contactform/home.html'
    context = {}

    context['form'] = ContactForm()

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':
        filled_form = ContactForm(request.POST)
        if filled_form.is_valid():
            contactObject = filled_form.save()
            name = contactObject.name
            city = contactObject.city
            #phone = contactObject.phone
            gender = contactObject.gender
            context['name'] = name
            context['city'] = city
            #context['phone'] = phone
            context['gender'] = gender
            return render(request, template, context)
        context['errors'] = filled_form.errors
    return render(request, template, context)
