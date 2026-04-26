from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

# Importation de toutes tes vues depuis l'app 'core'
from core.views import (
    ProjectViewSet, 
    SkillViewSet, 
    ExperienceViewSet, 
    ContactMessageView
)

# Création du router pour les ViewSets (API automatique)
router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'experience', ExperienceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Toutes les routes du router (projects, skills, experience)
    path('api/', include(router.urls)), 
    
    # Ta route spécifique pour le formulaire de contact
    path('api/contact/', ContactMessageView.as_view(), name='contact'),
]

# Service des fichiers MEDIA (tes photos de projets) en mode DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)