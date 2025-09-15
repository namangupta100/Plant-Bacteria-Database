from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from .views import (
    PlantProbioticBacteriaViewSet,
    BacteriaListView,
    BacteriaDetailView,
    BacteriaCreateView,
    BacteriaUpdateView,
    BacteriaDeleteView,
    HomeView,
    CustomAPIRootView,
    AboutView
)

router = DefaultRouter()
router.register(r'api/bacteria', PlantProbioticBacteriaViewSet)

# API Documentation schemas
schema_view = get_schema_view(title='Plant Probiotic Bacteria API')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('api/schema/', schema_view, name='schema'),
    path('api/docs/', include_docs_urls(title='Plant Probiotic Bacteria API'), name='schema-docs'),
    path('bacteria/', BacteriaListView.as_view(), name='bacteria_list'),
    path('bacteria/<int:pk>/', BacteriaDetailView.as_view(), name='bacteria_detail'),
    path('bacteria/create/', BacteriaCreateView.as_view(), name='bacteria_create'),
    path('bacteria/<int:pk>/update/', BacteriaUpdateView.as_view(), name='bacteria_update'),
    path('bacteria/<int:pk>/delete/', BacteriaDeleteView.as_view(), name='bacteria_delete'),
]
