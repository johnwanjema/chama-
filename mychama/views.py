from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm,CreateChamaForm
from .models import Profile,Individual,Group,Membership
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils import timezone

# Create your views here.
def index(request):    
    return render(request, 'index.html')

def loan(request):    
    return render(request, 'loan.html')

@login_required(login_url='/accounts/login')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user=current_user)
    print(profile)
    my_profile = Profile.objects.get(user=current_user)
    return render(request, 'profile.html', locals())


@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = current_user
            prof.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm()
    return render(request, 'update_profile.html', {'form': form})

class ChamaCreate(CreateView):
    model = Group
    form_class = CreateChamaForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        chama = form.save()
        m1 = Membership.objects.create(
            member=self.request.user, chama=chama, date_joined=timezone.now())
        return super().form_valid(form)

@login_required(login_url='/accounts/login/')
def chama(request):
    form = CreateChamaForm
    chamas = Group.objects.all()
    print(chamas)
    current_user = request.user
    if request.method == "POST":
        form = CreateChamaForm(request.POST, request.FILES)
        if form.is_valid():
            chama = form.save(commit=False)
            chama.created_by = current_user
            chama.save()
            return redirect('index')
        else:
            form = CreateChamaForm(request.POST, request.FILES)
    return render(request, 'chama_form.html', {"form": form,"chamas": chamas})
