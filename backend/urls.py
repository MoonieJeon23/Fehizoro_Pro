from django.contrib import admin
from django.urls import path, include, re_path # Ajout de re_path ici
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.static import serve # Ajout de serve ici
from core.views import ProjectViewSet, SkillViewSet, ExperienceViewSet, ContactMessageView

# 1. Configuration du Router
router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'experience', ExperienceViewSet)

# 2. Liste unique urlpatterns
# 2. Liste unique urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),

    # SOLUTION POUR LE CV
    re_path(r'^public/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # ON UTILISE UNE STRUCTURE PLUS CLAIRE :
    # On met d'abord tout ce qui est dans le router sous /api/
    path('api/', include(router.urls)),

    # ET ON CHANGE LÉGÈREMENT LE CHEMIN DU CONTACT POUR ÉVITER LE CONFLIT AVEC LE ROUTER
   path('api/contact/', ContactMessageView.as_view(), name='contact'),

    # Front-end
    path('', TemplateView.as_view(template_name='index.html')),
]

# 3. Service des fichiers médias et statiques
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)