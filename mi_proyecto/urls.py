from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from tasks import views

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # 🏠 Home
    path("", views.home, name="home"),

    # 📚 Secciones
    path("cursos/", views.cursos, name="cursos"),
    path("experiencia/", views.experiencia, name="experiencia"),
    path("reconocimientos/", views.reconocimientos, name="reconocimientos"),
    path("garage/", views.garage, name="garage"),
    path("productos-laborales/", views.productos_laborales, name="productos_laborales"),
    path("productos-academicos/", views.productos_academicos, name="productos_academicos"),
    
    # 📄 Exportar CV
    path("exportar-cv/", views.exportar_cv, name="exportar_cv"),
]

# Configuración para ver imágenes en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)