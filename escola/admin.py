from django.contrib import admin
from .models import *
class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nome', 'Email', 'CPF', 'Data_Nascimento', 'Celular')
    list_display_links = ('id', 'Nome')
    list_per_page = 20
    search_fields = ('Nome','CPF')
    ordering = ('Nome',)
admin.site.register(Estudantes, EstudanteAdmin)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_curso', 'Descricao')
    list_display_links = ('id', 'id_curso')
    search_fields = ('id_curso',)
admin.site.register(Curso, CursoAdmin)

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('id','id_estudante','id_curs','periodo')
    list_display_links = ('id','id_estudante','id_curs')
    search_fields = ('id',)
admin.site.register(Matricula, MatriculaAdmin)
