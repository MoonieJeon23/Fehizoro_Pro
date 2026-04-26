
from rest_framework import viewsets
from .models import Project, Skill, Experience, ContactMessage  # Vérifie que Skill et Experience sont bien ici
from .serializers import ProjectSerializer, SkillSerializer, ExperienceSerializer, ContactMessageSerializer # Et ici aussi
from rest_framework import generics



class ContactMessageView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    
class ProjectViewSet(viewsets.ModelViewSet):
    # Recupération dans BDD
    queryset = Project.objects.all()
    # Utiliser le traducteur qui vient d'etre créer
    serializer_class = ProjectSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

