from django.db import models

class Project(models.Model):
    """
    Représente tes projets de développement et de design.
    Inclut les visuels et les rapports techniques pour une documentation de A à Z.
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology_stack = models.CharField(max_length=200)

    # Visuels et Documents
    # Les images et PDF seront stockés dans le dossier media/ défini dans settings
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    report_pdf = models.FileField(upload_to='reports/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    """
    Gère tes compétences par catégories pour un affichage filtré dans React.
    """
    CATEGORY_CHOICES = [
        ('tech', 'Technique / Programmation'),
        ('soft', 'Soft Skills / Leadership'),
        ('design', 'Design / 3D'),
        ('lang', 'Langues'),
    ]
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='tech')
    percentage = models.IntegerField(default=70) # Utile pour des barres de progression ou cercles

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"

class Experience(models.Model):
    """
    Détaille ton parcours, notamment tes responsabilités de Présidente ING.
    """
    title = models.CharField(max_length=100) 
    organization = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True) 
    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ['-start_date'] # Les expériences les plus récentes apparaissent en premier

    def __str__(self):
        return f"{self.title} @ {self.organization}"