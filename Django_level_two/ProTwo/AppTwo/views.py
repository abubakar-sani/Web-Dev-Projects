from django.shortcuts import render
from AppTwo.models import WaitingList
from AppTwo.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request, 'appTwo/index.html')

def users(request):

    user_list = WaitingList.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request, 'appTwo/users.html', context = user_dict)

def signUp(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'appTwo/signUp.html', {'form': form})
