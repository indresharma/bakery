
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as authentication_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('register/', user_views.register, name="register"),
    path('login/', authentication_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', authentication_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('profile/', user_views.profile, name="profile")
]


urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
