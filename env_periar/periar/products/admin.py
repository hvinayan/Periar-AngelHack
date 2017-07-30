from django.contrib import admin
from .models import Product, Category, Cart

from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy

class MyAdminSite(AdminSite):
    # Text to put at the end of each page's <title>.
    site_title = ugettext_lazy('Periar')

    # Text to put in each page's <h1> (and above login form).
    site_header = ugettext_lazy('Periar:Dash')

    # Text to put at the top of the admin index page.
    index_title = ugettext_lazy('Periar:Dash')

admin_site = MyAdminSite()

# Register your models here.


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
