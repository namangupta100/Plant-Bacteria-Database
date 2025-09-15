from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.db.models import Count, Q
from .models import PlantProbioticBacteria
from .serializers import PlantProbioticBacteriaSerializer

class PlantProbioticBacteriaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Plant Probiotic Bacteria to be viewed or edited.
    Supports: list, create, retrieve, update, and delete operations.
    """
    queryset = PlantProbioticBacteria.objects.all().order_by('-created_at')
    serializer_class = PlantProbioticBacteriaSerializer

class AboutView(TemplateView):
    template_name = 'pbd/about.html'

class BacteriaListView(ListView):
    model = PlantProbioticBacteria
    template_name = 'pbd/bacteria_list.html'
    context_object_name = 'bacteria_list'
    ordering = ['-created_at']

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(genus__icontains=query) |
                Q(species__icontains=query) |
                Q(strain__icontains=query) |
                Q(plant_host__icontains=query) |
                Q(function__icontains=query) |
                Q(mode_of_action__icontains=query) |
                Q(reference__icontains=query)
            ).distinct()
        return queryset

class BacteriaDetailView(DetailView):
    model = PlantProbioticBacteria
    template_name = 'pbd/bacteria_detail.html'
    context_object_name = 'bacteria'

class BacteriaCreateView(CreateView):
    model = PlantProbioticBacteria
    template_name = 'pbd/bacteria_form.html'
    fields = ['genus', 'species', 'strain', 'plant_host', 'function', 'mode_of_action', 'reference']
    success_url = reverse_lazy('bacteria_list')

class BacteriaUpdateView(UpdateView):
    model = PlantProbioticBacteria
    template_name = 'pbd/bacteria_form.html'
    fields = ['genus', 'species', 'strain', 'plant_host', 'function', 'mode_of_action', 'reference']
    success_url = reverse_lazy('bacteria_list')

class BacteriaDeleteView(DeleteView):
    model = PlantProbioticBacteria
    template_name = 'pbd/bacteria_confirm_delete.html'
    success_url = reverse_lazy('bacteria_list')

    def post(self, request, *args, **kwargs):
        import logging
        logger = logging.getLogger(__name__)
        logger.warning(f"Attempting to delete object with pk={self.kwargs.get('pk')}")
        response = super().post(request, *args, **kwargs)
        logger.warning(f"Delete response status: {response.status_code}")
        return response

class HomeView(TemplateView):
    template_name = 'pbd/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get total number of strains
        context['total_strains'] = PlantProbioticBacteria.objects.count()
        
        # Get unique plant hosts count
        context['total_hosts'] = PlantProbioticBacteria.objects.values('plant_host').distinct().count()
        
        # Get unique genera count
        context['total_genera'] = PlantProbioticBacteria.objects.values('genus').distinct().count()
        
        # Get unique species count
        context['total_species'] = PlantProbioticBacteria.objects.values('species').distinct().count()
        
        return context

class CustomAPIRootView(APIView):
    """
    Plant Probiotic Bacteria Database API Root
    
    This is the root endpoint for the Plant Probiotic Bacteria Database API.
    The API provides access to manage and retrieve information about plant probiotic bacteria.
    """
    
    def get(self, request, *args, **kwargs):
        data = {
            'bacteria': {
                'list': reverse('plantprobioticbacteria-list', request=request),
                'description': 'Endpoints for managing plant probiotic bacteria records',
                'actions': {
                    'GET': 'List all bacteria records',
                    'POST': 'Create a new bacteria record'
                }
            },
            'statistics': {
                'total_strains': PlantProbioticBacteria.objects.count(),
                'unique_genera': PlantProbioticBacteria.objects.values('genus').distinct().count(),
                'unique_species': PlantProbioticBacteria.objects.values('species').distinct().count(),
                'unique_hosts': PlantProbioticBacteria.objects.values('plant_host').distinct().count()
            },
            'documentation': reverse('schema-docs', request=request),
            'schema': reverse('schema', request=request),
        }
        return Response(data)
