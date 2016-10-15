from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, Http404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib import quote_plus
from django.db.models import Q
from django.utils import timezone
# just replaced id with slug everywhere
# Create your views here.

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
        
    if not request.user.is_authenticated:
        raise Http404
        
    form=PostForm(request.POST or None, request.FILES or None)# we added None so that it doesn't display "The field is required" every time we visit the page
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user # it will assume the user is logged in
        print form.cleaned_data.get("title")#will print it in terminal ..and not needed.. just for knowledge 
        instance.save()
        #message success
        messages.success(request, "Successfully Created", extra_tags='some-tag')
        # message is not working properly because of cloud9 i guess.. we can also add links to these messages... review video #23 
        #we can have multiple messages in the same manner
        return HttpResponseRedirect(instance.get_absolute_url()) 
    else:
        messages.error(request, "Not Successfully Created")
        
                  #  <!--<a href="{% url 'posts:detail' obj.id %}">{{ obj.title }}</a></br>-->
    
    """for capturing the data add the following code
    if request.method=='POST':
        print request.POST.get("content")
        print request.POST.get("title")"""
    context={
        'form':form
    }
    return render(request, "post_form.html", context)

def post_detail(request, slug):
    #instance=Post.objects.get(id=3)
    instance =get_object_or_404(Post, slug=slug)
    if instance.publish> timezone.now().date() or instance.draft:
        if not request.user.is_staff or not request.user.is_superuser:
            raise Http404
    
    share_string=quote_plus(instance.content)
    context={
        "title":instance.title ,
        "instance":instance,
        "share_string":share_string,
    }
    return render(request, "post_detail.html", context)
    
def post_list(request):
    today=timezone.now().date()
    queryset_list=Post.objects.active()#.order_by('-timestamp')# order_by recreates the order of posts according to timestamp.. another way of doing it is demonstrated in models.py
    if request.user.is_staff or request.user.is_superuser:
        queryset_list=Post.objects.all()
    #queryset_list=Post.objects.filter(draft=False).filter(publish__lte=timezone.now())
    #pagination copied from django documentation
    
    query=request.GET.get("query")
    if query:
        queryset_list=queryset_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(user__first_name__icontains=query)|
            Q(user__last_name__icontains=query)
            ).distinct() # what is distinct?
    paginator = Paginator(queryset_list, 10) # Show 10 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context={
        "object_list":queryset,
        "title":"Psycho",
        #"page_request_var": page_request_var,
        "today":today,
    }
    return render(request, "post_list.html", context)
    
def post_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance=get_object_or_404(Post, slug=slug)
    form=PostForm(request.POST or None, request.FILES or None, instance=instance )#instance =instance so that we can see the original post and then edit it
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        #message success
        messages.success(request, "Successfully Updated")
        #we can have multiple messages in the same manner
        return HttpResponseRedirect(instance.get_absolute_url())  
    else:
        messages.error(request, "Not Successfully Updated")
        
    context={
        "title":instance.title,
        "instance":instance,
        "form":form,
        }
    return render(request, "post_form.html", context)
    
def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance=get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("posts:home")
    #return HttpResponse("<h3>Delete is working</h3>")
    
    
    

