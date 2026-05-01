from rest_framework import viewsets
from .models import Project, Skill, Experience
from .serializers import ProjectSerializer, SkillSerializer, ExperienceSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    Vue pour gérer les projets.
    Permet de lister et de voir les détails de tes réalisations.
    """
    queryset = Project.objects.all().order_by('-created_at')
    serializer_class = ProjectSerializer

class SkillViewSet(viewsets.ModelViewSet):
    """
    Vue pour les compétences.
    Indispensable pour l'affichage filtré par catégories dans React.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    """
    Vue pour ton parcours professionnel et associatif.
    """
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer