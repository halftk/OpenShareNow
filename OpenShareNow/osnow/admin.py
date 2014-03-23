from django.contrib import admin

from osnow.models import Item
from osnow.models import Seccio
from osnow.models import Categoria
from osnow.models import Usuari
from osnow.models import Comentari
from osnow.models import Idioma
from osnow.models import Tag
from osnow.models import Valoracio

admin.site.register(Item)
admin.site.register(Seccio)
admin.site.register(Categoria)
admin.site.register(Usuari)
admin.site.register(Comentari)
admin.site.register(Idioma)
admin.site.register(Tag)
admin.site.register(Valoracio)


