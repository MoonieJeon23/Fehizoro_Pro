from rest_framework import serializers
from .models import Project, Skill, Experience

class ProjectSerializer(serializers.ModelSerializer):
    """
    Transforme les données de tes projets en JSON pour React.
    Inclut automatiquement les URLs des images et des rapports PDF.
    """
    class Meta:
        model = Project
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    """
    Gère la sérialisation de tes compétences par catégories.
    """
    class Meta:
        model = Skill
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    """
    Transforme tes expériences professionnelles et associatives (ING).
    """
    class Meta:
        model = Experience
        fields = '__all__'