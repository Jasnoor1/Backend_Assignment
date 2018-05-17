"""api URL Configuration

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
from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from Company import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/', views.UsersList.as_view(),name="employee_list"),
    #url(r'^users/',views.UsersList.as_view(),name="search"),
    url(r'^user/', views.EmployeeCreateView.as_view(),name="create_employee"),# adding the new user
    #url(r'^users/create/$',views.EmployeeCreateView.as_view(),name="create_employee"),
    #url(r'^posts/(?P<pk>\d+)/detail/$', views.EmployeeDetailView.as_view(), name="employee_details"),
    url(r'^posts/(?P<pk>[0-9]+)/$',views.UsersDetail.as_view(),name="employee_details"),#getting the detail of the user through id
    url(r'^delete/(?P<pk>[0-9]+)/$', views.EmployeeDeleteView.as_view(),name="delete_employee"),
    url(r'^update/(?P<pk>\d+)/$', views.EmployeeUpdateView.as_view(), name="employee_update"),#put
    #url(r'^posts/(?P<pk>\d+)/delete/$', views.EmployeeDeleteView.as_view(), name="delete_employee"),
    #url(r'^delete/', views.UsersDelete.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)