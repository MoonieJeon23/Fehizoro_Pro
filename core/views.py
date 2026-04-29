from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Importe tes vues ici (ex: ProjectViewSet, SkillViewSet)
# de la manière dont tu les as nommées dans core/views.py

router = DefaultRouter()
# router.register(r'projects', ProjectViewSet)
# router.register(r'skills', SkillViewSet)

urlpatterns = [
    path('', include(router.urls)),
]