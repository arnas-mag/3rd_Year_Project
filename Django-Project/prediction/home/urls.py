from django.urls import path
from home import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
   path('', views.home, name="home"),
   path('dashboard', views.dashboard, name="dashboard"),
   path('login', views.login, name="login"),
   path('prediction', views.prediction, name="prediction"),
   path('graph', views.graph, name="graph"),
   path('create_account', views.create_account, name="create_account")
]

urlpatterns += staticfiles_urlpatterns()
