
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about-us/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('services/', TemplateView.as_view(template_name='services.html'), name='services'),
    path('packages/', TemplateView.as_view(template_name='packages.html'), name='packages'),
    path('blog/', TemplateView.as_view(template_name='blog.html'), name='blog'),
    path('work-profile/', TemplateView.as_view(template_name='work-profile.html'), name='work-profile'),
    path('our-careers/', TemplateView.as_view(template_name='our-careers.html'), name='our-careers'),
    path('get-in-touch-2/', TemplateView.as_view(template_name='get-in-touch-2.html'), name='get-in-touch-2'),
    path('base/', TemplateView.as_view(template_name='base.html'), name='base'),
]
