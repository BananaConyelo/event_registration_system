from django.shortcuts import render, redirect
from .forms import EventRegistrationForm
from django.contrib import messages

def event_register(request):
    if request.method == "POST":
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration saved successfully!")
            return redirect('home')
    else:
        form = EventRegistrationForm()
    
    return render(request, 'registration_form.html', {'form' : form})