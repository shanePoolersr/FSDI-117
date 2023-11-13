from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string


# Create your views here.
def home(request):
    return render(request,'pages/about_me.html')

def contact(request):
    
    if request.method == "POST":
        form = ContactForm(request.Post)
        
        if form .is_valid():
            #send email
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email_from = form.cleaned_data['email']
            
            html = render_to_string("pages/email.html", request.POST)
            
            send_mail("Message from " + name, message,  email_from, ['me@mail.com'], html_message=html)
            
            return redirect('home')
    
    else:
        # send the html
        
        form = ContactForm() # Create an instance of the form
        
        return render(request, 'pages/contact.html',{
            'form': form
            
                           
        })
        
def edu_work(request):
    return render(request, 'pages/experience.html')        