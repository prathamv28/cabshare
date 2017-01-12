from django.conf.urls import include, url
from django.contrib import admin
from user_auth import views as user_auth_views
from chats import views as chats_views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/get-token/' , auth_views.obtain_auth_token ),

]
