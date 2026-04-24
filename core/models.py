from django.db import models

class Project(models.Model):
    # Les bases
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology_stack = models.CharField(max_length=200) # ex: "C++, SFML"
    
    # Le visuel et les documents (Très important pour tes rapports A à Z)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    report_pdf = models.FileField(upload_to='reports/', blank=True, null=True)
    
    # Pour trier tes projets par date
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title