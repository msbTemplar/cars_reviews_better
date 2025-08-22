from django.contrib import admin
from .models import Comment, Newsletter, ContactMessage,Noticia,NoticiaDiferente,CommentMotorpasion, CommentAutocar, CommentAutonews, CommentCarmagazine,CommentCarscoops,CommentInsideevs


# Register your models here.

admin.site.register(Comment)
admin.site.register(CommentMotorpasion)
admin.site.register(CommentAutocar)
admin.site.register(CommentAutonews)
admin.site.register(CommentCarmagazine)
admin.site.register(CommentCarscoops)
admin.site.register(ContactMessage)
admin.site.register(Newsletter)
admin.site.register(CommentInsideevs)
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'link')

@admin.register(NoticiaDiferente)
class NoticiaDiferenteAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'link', 'img_url')