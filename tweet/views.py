from django.shortcuts import render
from .models import tweet, contact_me
from .forms import tweetFrom ,UserRgistrationForm, contactFORM
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
# Create your views here.

def index (request):
    return render(request, 'tweet/index.html')

def tweet_list (request):
    Tweetuu = tweet.objects.all().order_by('-created_on')
    return render(request, 'tweet/tweet_list.html', {'tweet':Tweetuu})

@login_required
def tweet_create (request):
    if request.method == 'POST' :
        form = tweetFrom(request.POST, request.FILES)
        if form.is_valid():
            tweet =form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = tweetFrom
    return render(request, 'tweet/tweet_form.html',{'form':form})

def tweet_edit(request, pk_id):
    tweet_instance = get_object_or_404(tweet, pk=pk_id, user=request.user)

    if request.method == 'POST':
        form = tweetFrom(request.POST, request.FILES, instance=tweet_instance)
        if form.is_valid():
            edited_tweet = form.save(commit=False) 
            edited_tweet.user = request.user
            edited_tweet.save()
            return redirect('tweet_list')
    else:
        form = tweetFrom(instance=tweet_instance)

    return render(request, 'tweet/tweet_form.html', {'form': form})

def tweet_delete (request, pk_id):
    tweetuur = get_object_or_404(tweet, pk=pk_id, user = request.user)
    if request.method == 'POST':
        tweetuur.delete()
        return redirect('tweet_list')
    
    return render(request, 'tweet/tweet_confirm_delete.html',{'tweet':tweetuur})

def register (request):
    if request.method == 'POST':
        form = UserRgistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRgistrationForm()
    return render(request, 'registration/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tweet_list') 
        else:
            return render(request, 'login.html', {'form': {}, 'error': 'Invalid credentials'})
    return render(request, 'login.html', {'form': {}})

def userlogout(request):
    logout(request)
    return redirect('tweet_list')

def about(request):
    return render(request, 'tweet/about.html')

def contact(request):
    # contactuu = contact_me.objects.all().order_by('-created_on')
    if request.method == 'POST':
        form = contactFORM(request.POST)
        if form.is_valid():
            form.save(commit=True)
            
            return redirect('index')
    else:
        form = contactFORM()
    return render(request, 'tweet/contact.html',{'form': form} )

# def contact_view(request):
    
#     return render(request, 'tweet/index.html', {'contact_det':contactuu})
