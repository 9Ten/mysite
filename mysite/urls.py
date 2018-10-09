"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

# account
from account.views import register

# dashboard
from dashboard.views import dashboard_view, dashboard_edit, dashboard_status, dashboard_abstract,dashboard_payment

from django.contrib.auth import views as auth_views
from mysite import views as static_content

admin.site.site_header = 'Web-Conferrence Admin'
admin.site.site_title = 'Web-Conferrence Admin'
# admin.site.site_url = 'http://127.0.0.1:8000/'
admin.site.index_title = 'Web-Conferrence Administration'


urlpatterns = [
    # Section Dynamic content
    path('', static_content.index),
    path('index/', static_content.index, name='index'),
    path('news/', static_content.news, name='news'),
    path('dashboard/view/', dashboard_view, name='dashboard_view'),
    path('dashboard/edit/', dashboard_edit, name='dashboard_edit'),
    path('dashboard/status/', dashboard_status, name='dashboard_status'),
    path('dashboard/abstract/', dashboard_abstract, name='dashboard_abstract'),
    path('dashboard/payment/', dashboard_payment, name='dashboard_payment'),

    # Section Static content
    path('about_us/', static_content.about_us, name='about_us'),
    path('abstract/', static_content.abstract, name='abstract'),
    path('accommodation/', static_content.accommodation, name='accommodation'),
    path('committee/', static_content.committee, name='committee'),
    path('contact/', static_content.contact, name='contact'),
    path('convention_venue/', static_content.convention_venue,
         name='convention_venue'),
    path('excursion/', static_content.excursion, name='excursion'),
    path('general_information/', static_content.general_information,
         name='general_information'),
    path('programs/', static_content.programs, name='programs'),
    path('registration/', static_content.registration, name='registration'),
    path('schedule/', static_content.schedule, name='schedule'),
    path('speakers/', static_content.speakers, name='speakers'),
    path('visa/', static_content.visa, name='visa'),

    # Section Authentication
    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    path('register/', register, name='register'),

    # password_reset with email
    path('password_reset/', auth_views.password_reset, {'template_name': 'password_reset_form.html'}, name='password_reset'),
    path('password_reset/done/', auth_views.password_reset_done, {'template_name': 'password_reset_done.html'}, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.password_reset_confirm, {'template_name': 'password_reset_confirm.html'}, name='password_reset_confirm'),
    path('reset/done/', auth_views.password_reset_complete, {'template_name': 'password_reset_complete.html'}, name='password_reset_complete'),

    # Section Admin
    path('myadmin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),   # CKEditor
]


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
