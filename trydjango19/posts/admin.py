from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin): # ModelAdmin is used for customizing the admin
     list_display=['title','updated', 'timestamp'] # list_display -displays the arrays in the admin page
     list_display_links=['updated'] # list_display_links -it will make the text in the updated array to be functionable
     list_filter=['updated', 'timestamp'] # list_filter - it adds the filtering options on the right side of the admin page
     list_editable=['title'] # list_editable - let's the user edit the title without actually entering the link
     search_fields=['title', 'content'] # search_fields - will look thru the title and content for the string entered by the user
     class Meta:
         models=Post

admin.site.register(Post, PostAdmin)



#admin follows crud -create, retrieve, update, delete
