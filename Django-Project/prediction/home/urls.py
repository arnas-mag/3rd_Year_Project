from django.urls import path
from home import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
   path('', views.user_login, name="login"),
   path('dashboard', views.dashboard, name="dashboard"),
   path('login', views.user_login, name="login"),
   path('prediction', views.prediction, name="prediction"),
   path('graph', views.graph, name="graph"),
   path('create_account', views.create_account, name="create_account")
]

urlpatterns += staticfiles_urlpatterns()
