from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        ins = Contact(name=name, email=email, subject=subject, message=message)

        ins.save()

        return render(request, 'store/contact.html', {'name': name})
    else:
        form = ContactForm(request.POST)
        return render(request, 'store/contact.html', {'form': form})


from django.shortcuts import render

# Create your views here.
