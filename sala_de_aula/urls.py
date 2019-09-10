
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from professor.views import ProfessorViewSet
from sala.views import AlunoViewSet, AlunoList, AlunoDetails
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'aluno',AlunoViewSet)
router.register(r'professor', ProfessorViewSet)

urlpatterns = [
    path('alunos', AlunoList.as_view()),
    path('aluno/<int:id>', AlunoDetails.as_view()),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth-api/', obtain_auth_token),
]
