# forms.py
from django import forms
from .models import Comment,Newsletter,ContactMessage, CommentMotorpasion, CommentCarscoops, CommentInsideevs, CommentCarmagazine, CommentAutocar, CommentAutonews, CommentBuscarNoticias,CommentIMDB

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'website', 'message', 'image']  # Incluye el campo `image`
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your website (optional)',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your message',
                'rows': 5,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }

class CommentMotorpasionForm(forms.ModelForm):
    class Meta:
        model = CommentMotorpasion
        fields = ['name', 'email', 'website', 'message', 'image']  # Incluye el campo `image`
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your website (optional)',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your message',
                'rows': 5,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }

class CommentCarscoopsForm(forms.ModelForm):
    class Meta:
        model = CommentCarscoops
        fields = ['name', 'email', 'website', 'message', 'image']  # Incluye el campo `image`
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your website (optional)',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your message',
                'rows': 5,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }


class CommentInsideevsForm(forms.ModelForm):
    class Meta:
        model = CommentInsideevs
        fields = ['name', 'email', 'website', 'message', 'image']  # Incluye el campo `image`
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your website (optional)',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your message',
                'rows': 5,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }


class CommentCarmagazineForm(forms.ModelForm):
    class Meta:
        model = CommentCarmagazine
        fields = ['name', 'email', 'website', 'message', 'image']  # Incluye el campo `image`
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your website (optional)',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your message',
                'rows': 5,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }


class CommentAutocarForm(forms.ModelForm):
    class Meta:
        model = CommentAutocar
        fields = ['name', 'email', 'website', 'message', 'image']  # Incluye el campo `image`
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your website (optional)',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your message',
                'rows': 5,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }


class CommentAutonewsForm(forms.ModelForm):
    class Meta:
        model = CommentAutonews
        fields = ['name', 'email', 'website', 'message', 'image']  # Incluye el campo `image`
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your website (optional)',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your message',
                'rows': 5,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }


#CommentBuscarNoticias
class CommentBuscarNoticiasForm(forms.ModelForm):
    class Meta:
        model = CommentBuscarNoticias
        fields = ['name', 'email', 'website', 'message', 'image']  # Incluye el campo `image`
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your website (optional)',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your message',
                'rows': 5,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }

#CommentIMDB
class CommentIMDBForm(forms.ModelForm):
    class Meta:
        model = CommentBuscarNoticias
        fields = ['name', 'email', 'website', 'message', 'image']  # Incluye el campo `image`
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your website (optional)',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your message',
                'rows': 5,
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']  # Solo necesitamos el correo electrónico
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control border-white p-3',
                'placeholder': 'Your Email',
                'style': 'height: 55px;'
            }),
        }
        labels = {
            'email': ''
        }
        

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Your Name',
                'style': 'height: 55px;',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Your Email',
                'style': 'height: 55px;',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Subject',
                'style': 'height: 55px;',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control border-1 bg-light px-4',
                'placeholder': 'Your Message',
                'style': 'height: 200px;',
            }),
        }