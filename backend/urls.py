from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from core.views import ProjectViewSet, SkillViewSet, ExperienceViewSet

# 1. Configuration du Router pour l'API
router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'experience', ExperienceViewSet)

urlpatterns = [
    # Administration Django
    path('admin/', admin.site.urls),

    # API Routes
    path('api/', include(router.urls)),
]

# 2. Service des fichiers médias et statiques
# On les place ICI pour qu'ils soient prioritaires sur le routage du Frontend
if settings.DEBUG or not settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# 3. Catch-all pour le Front-end (React)
# TOUJOURS en dernière position
urlpatterns += [
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]