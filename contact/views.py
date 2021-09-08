from django.shortcuts import render, redirect
from .forms import FormContact
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    form_contact = FormContact()

    if request.method=='POST':
        form_contact = FormContact(data=request.POST)
        if form_contact.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            content = request.POST.get("content")

            msg = EmailMessage(
                'Messaje from app',
                'The user {} with email {} write:\n\n {}'.format(name, email, content),
                '', 
                ['<put recipient email>'] # Change for the recipient email
            )

            try:
                msg.send()
                return redirect("/contact/?valid")          
            except:
                return redirect("/contact/?invalid")     

    return render(request, "contact/contact.html", {'form_contact': form_contact})  