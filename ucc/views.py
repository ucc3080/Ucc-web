from django.shortcuts import render
from .forms import UserRegistrationForm

# Create your views here.
def home(request):
    return render(request, 'index.html')
    
def register(request):
    if request.method == 'Register':
        user_form = UserRegistrationForm(request.Register)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_email(user_form.cleaned_data['email'])
            new_user.save()
            return render(request,
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})