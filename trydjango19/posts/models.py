from django.db import models # 
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone

# Create your models here.
# Post.objects.all() -- it's a type of model manager that works with the queryset
# Post.objects.create() -- another type of model manager that creates an instance
class PostManager(models.Manager): #Model managers is essentially a way to control how the models work
    def active(self, *args, **kwargs):
        #Post.objects.all()= super(PostManager, self).all() same thing
        return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())



# when using ImageField we will have to install pillow by -- pip install pillow
def upload_location(instance, filename): # this upload_location will change how it is uploaded inside the mdeia_cdn
    #filebase, extension= filename.split(".")
    #return "%s/%s/%s" %(instance.id, filename, extension)# we will have the instance.id in the name of the file instead of the original image file..but not a good idea
    return "%s/%s" %(instance.id, filename) # if we had a user folder we cud have done-- instance.user

class Post(models.Model):# title, image, content, updated, timestamp are all attributes of our class Post
    user=models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title=models.CharField(max_length=200)
    slug=models.SlugField(unique=True)
    #image=models.FileField(null=True, blank=True) # blank=True , as a Post can also exist without an image # heightfield and widthfield don't exist in filefield that's why we have used imagefield here
    #image=models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field") # adding additional attributes to the image field
    image=models.ImageField(upload_to=upload_location,null=True, blank=True, width_field="width_field", height_field="height_field") # upload_to calls the function upload_location(created above)  ..we can also do this -- upload_to="images/"
    height_field=models.IntegerField(default=0) # gives the height of the image...chk the admin 
    width_field=models.IntegerField(default=0) # gives the width of the image.. chk the admin
    draft=models.BooleanField(default=False)
    publish=models.DateField(auto_now=False, auto_now_add=False)
    
    content=models.TextField()
    updated=models.DateTimeField(auto_now=True, auto_now_add=False)
    #auto_now=True # whenever it was last updated, it will change accordingly when it was last updated
    timestamp=models.DateTimeField(auto_now=False, auto_now_add=True)
    #auto_now_add=True # whenever it was added into the database , it is set only one time
    
    objects=PostManager() # if we remove this statement ..it will show us the drafts and the posts published in the future
    # we can call objects anything(ex. views) ..it is just a variable but in views then we will have to change Post.objects.all -> Post.views.all
    def __unicode__(self): # we declare this so that we can see the title in place of <album object> when we type Post.objects.all()
        return self.title
        
    def get_absolute_url(self):
        #return "/posts/%s/"%(self.id)
        return reverse("posts:detail", kwargs={"slug":self.slug})
        
    class Meta:#orders the posts according to the arguments passed
        ordering =["-timestamp","-updated"]
        
def create_slug(instance, new_slug=None):
    slug=slugify(instance.title)
    if new_slug is not None:
        slug=new_slug
    qs=Post.objects.filter(slug=slug).order_by("-id")
    exists=qs.exists()
    if exists:
        new_slug="%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug
        
        
        
def pre_save_post_receiver(sender, instance, *args, **kwargs):     #for receiving signals refer django documentation
    if not instance.slug:
        instance.slug=create_slug(instance)
    
    
    
    
    
    
    """slug=slugify(instance.title)
    # tesla item 1-> tesla-item-1
    exists=Post.objects.filter(slug=slug).exists
    if exists:
        slug= "%s-%s" %(slug, instance.id)
    instance.slug=slug"""
    
        
pre_save.connect(pre_save_post_receiver, sender=Post) # here sender is Post and receiver is pre_save_post_receiver
# the sender is always the model class


# Each model is a Python class that subclasses django.db.models.Model.
# x=Post() , a regular python object
# x.title="xyz"
# x.content="sdgssaf"
# x.save(), for saving

# another method:
# x=Post(title="xyz", content="asdasd")

# for referencing purposes:
# x.title
# x.content
# x.id


# filtering purposes:
# Post.objects.filter(id=1) will return whatever the __unicode__ is returning corresponding to that id=1..in this case title ..
# 
# Post.objects.filter(title__startswith='xyz') will return the title starting with xyz i.e. whatever unicode is returning

#Post.objects.create(user=user, title="title_anything", )

#Post.objects.all.filter()


