"""imdbportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from imdbfeatures.views import root_view, search_by_name_view, search_by_imdb_id, test_table_view

urlpatterns = [
    
    path('', root_view),
    path('table/', test_table_view),
    path('admin/', admin.site.urls),
    path('byname/', search_by_name_view),
    path('imdb-id/<str:imdb_id>', search_by_imdb_id, name='details-imdb-id'),
]
