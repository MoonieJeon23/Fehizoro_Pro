from django.db import models
from django.core.mail import send_mail
from django.conf import settings

class Project(models.Model):
    # Les bases
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology_stack = models.CharField(max_length=200) 
    
    # Le visuel et les documents 
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    report_pdf = models.FileField(upload_to='reports/', blank=True, null=True)
    
    # Pour trier les projets par date
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Technique / Programmation'),
        ('soft', 'Soft Skills / Leadership'),
        ('design', 'Design / 3D'),
        ('lang', 'Langues'),
    ]
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='tech')
    percentage = models.IntegerField(default=70) # Pour afficher une barre de progression

    def __str__(self):
        return f"{self.name} ({self.category})"

class Experience(models.Model):
    title = models.CharField(max_length=100) # ex: Présidente ING
    organization = models.CharField(max_length=100) # ex: ISFPS
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True) # Vide si c'est "En cours"
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False) # Petit bonus pour ton Admin

    def save(self, *args, **kwargs):
        # On vérifie si c'est un nouveau message
        is_new = self.pk is None
        super().save(*args, **kwargs)
        
        if is_new:
            # On prépare le contenu pour toi
            sujet_pour_fehizoro = f"[Portfolio] Nouveau contact : {self.subject}"
            corps_pour_fehizoro = (
                f"Tu as reçu un nouveau message de ton portfolio !\n\n"
                f"Nom : {self.name}\n"
                f"Email : {self.email}\n"
                f"Sujet : {self.subject}\n\n"
                f"Message :\n{self.message}"
            )
            
            try:
                send_mail(
                    sujet_pour_fehizoro,
                    corps_pour_fehizoro,
                    settings.EMAIL_HOST_USER, # Expéditeur
                    [settings.EMAIL_HOST_USER], # Destinataire (Toi !)
                    fail_silently=False,
                )
            except Exception as e:
                # Si le mail échoue, on l'affiche dans le terminal pour débugger
                print(f"Erreur d'envoi d'email : {e}")

    def __str__(self):
        return f"Message de {self.name} - {self.subject}"