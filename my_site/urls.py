from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# Main URL patterns for the Django project
urlpatterns = [
    # Admin site URLs
    path('admin/', admin.site.urls),
    
    # Include URLs from the 'blog' app
    path('', include('blog.urls'))
]

# Serve media files during development (for user-uploaded content)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files during development (CSS, JavaScript, images, etc.)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
