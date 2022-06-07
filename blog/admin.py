from django.contrib import admin

from blog.models import *

admin.site.register(BlogModel)
admin.site.register(Categorias)
admin.site.register(Autor)