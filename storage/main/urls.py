from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^regist$', views.regist, name='regist'),
    url(r'^log_in$', views.log_in, name='log_in'),
    url(r'^log_out$', views.log_out, name='log_out$'),
    url(r'^Home', views.Home, name='Home'),


]