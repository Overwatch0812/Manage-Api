from .views import ProjectView,AllProjectView,DeleteApiView,UpdateApiView,CreateProjectView
from django.urls import path,include

urlpatterns = [
    path('',AllProjectView.as_view() ),
    path('create/',CreateProjectView.as_view() ),
    path('<int:pk>/',ProjectView.as_view()),
    path('<int:pk>/update/',UpdateApiView.as_view()),
    path('<int:pk>/delete/',DeleteApiView.as_view())
]