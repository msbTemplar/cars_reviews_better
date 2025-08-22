# models.py
from django.db import models
from django.core.exceptions import ValidationError

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField()
    image = models.ImageField(upload_to='comments_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.created_at}'

class CommentMotorpasion(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField()
    image = models.ImageField(upload_to='comments_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.created_at}'
    

class CommentCarscoops(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField()
    image = models.ImageField(upload_to='comments_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.created_at}'

#insideevs
class CommentInsideevs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField()
    image = models.ImageField(upload_to='comments_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.created_at}'
    

#carmagazine
class CommentCarmagazine(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField()
    image = models.ImageField(upload_to='comments_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.created_at}'


#autocar
class CommentAutocar(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField()
    image = models.ImageField(upload_to='comments_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.created_at}'

#autonews
class CommentAutonews(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField()
    image = models.ImageField(upload_to='comments_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.created_at}'


class CommentBuscarNoticias(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField()
    image = models.ImageField(upload_to='comments_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.created_at}'
    

class CommentIMDB(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField()
    image = models.ImageField(upload_to='comments_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.created_at}'



class Newsletter(models.Model):
    email = models.EmailField(unique=True)  # Almacenará el correo electrónico
    date_subscribed = models.DateTimeField(auto_now_add=True)  # Fecha de suscripción
    is_active = models.BooleanField(default=True)  # Permitir activar o desactivar la suscripción
    
    def __str__(self):
        return self.email
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Message from {self.name} - {self.subject}'
    

class Noticia1(models.Model):
    titulo = models.CharField(max_length=255)
    link = models.URLField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo
    

class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    link = models.URLField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['fecha_creacion']),  # Si deseas un índice en la fecha de creación
        ]
    
    def __str__(self):
        return self.titulo


class NoticiaDiferente(models.Model):
    titulo = models.CharField(max_length=2255)
    link = models.URLField(max_length=500)
    img_url = models.ImageField(upload_to='other_images/', max_length=500, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['fecha_creacion']),  # Si deseas un índice en la fecha de creación
        ]
    # def save(self, *args, **kwargs):
    #     # Truncar el título si excede los 100 caracteres
    #     if len(self.titulo) > 100:
    #         self.titulo = self.titulo[:90]
    #     super().save(*args, **kwargs)
        
    def __str__(self):
        return self.titulo
    

class FeaturedNews(models.Model):
    CATEGORY_CHOICES = [
        ("Technology", "Technology"),
        ("Sports", "Sports"),
        ("Entertainment", "Entertainment"),
        ("Other", "Other"),
    ]

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="Other")
    date = models.DateField()
    image = models.ImageField(upload_to="featured_news/")
    link = models.URLField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # Permitir activar o desactivar la suscripción
    

    def __str__(self):
        return self.title