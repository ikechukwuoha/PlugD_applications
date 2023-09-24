from django.contrib import admin
from django.urls import path, include
#from django.views.generic import TemplateView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),

    path('user/', include('users.urls')),
    path('admin/', admin.site.urls),


    #path('auth/', include('djoser.urls')),
    #path('auth/', include('djoser.urls.jwt')),

]

#urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
