"""
URL configuration for practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from app.views import register
from app.views import user_login

urlpatterns = [
    path('admin/', admin.site.urls),

    path('' ,home ,name="home"),

    path('index/' ,home ,name="home"),

    path('service/' ,service ,name="services"),

    path('contact/' ,contact ,name="contact"),

    path('video_get/' ,video_get ,name="video_get"),

    path('about/' ,about ,name="about"),

    path('Login/' ,user_login ,name="Login"),

    path('register/' ,register ,name="register"),

    path('delete-user/<int:user_id>/', delete_user, name='delete_user'),

    path('logout/', user_logout , name="logout_page"),

    path('live_video/', live_video , name="live_video"),

    # path('live_video_2/', livefe, name="live_camera"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

    
urlpatterns += staticfiles_urlpatterns()

