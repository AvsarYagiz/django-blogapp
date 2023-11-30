from django.contrib import admin

from .models import Post, Author, Tag, Comment

# Register your models here.

# Customizing the admin interface for the Post model
class PostAdmin(admin.ModelAdmin):
    # Add filters for easy navigation in the admin interface
    list_filter = ("author", "tags", "date",)
    
    # Displayed fields in the list view of the admin interface
    list_display = ("title", "date", "author",)
    
    # Automatically populate the slug field based on the title
    prepopulated_fields = {"slug": ("title",)}

# Customizing the admin interface for the Comment model
class CommentAdmin(admin.ModelAdmin):
    # Displayed fields in the list view of the admin interface
    list_display = ("user_name", "post")

# Register the models and their respective admin classes
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
