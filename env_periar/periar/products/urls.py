from django.conf.urls import url
from . import views

app_name = 'products'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<product_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^swipe/$', views.swipe, name='swipe'),
    url(r'^about/$', views.about, name='about'),
    url(r'^(?P<product_id>[0-9]+)/rate_p/$', views.ratep, name='prate'),
    url(r'^(?P<product_id>[0-9]+)/rate_n/$', views.raten, name='nrate'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<product_id>[0-9]+)/add_cart/$', views.addcart, name='addcart'),
    url(r'^cart/$', views.showcart, name='cart'),
    url(r'^(?P<cart_id>[0-9]+)/del/$', views.delete_cart, name='delcart'),
    #url(r'^(?P<user_id>[0-9]+)/checkout/$', views.checkout, name='checkout'),
]
