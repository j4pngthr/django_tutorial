"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# アプリで対応付けしたURLをURLconfに反映
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
  # URLから探す文字列 # 探す関数
  path('polls/', include('polls.urls')), # URLconfにpolls.urlsを反映
  path('admin/', admin.site.urls),
]
