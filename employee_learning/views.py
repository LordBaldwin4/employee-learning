import datetime
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import LearningCourse

# 1. Page d'accueil du site
class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.date.today()
        return context

# 2. Liste des cours (triée par titre)
class CourseList(LoginRequiredMixin, ListView):
    queryset = LearningCourse.objects.order_by('title')  # Trie par ordre alphabétique
    template_name = 'employee_learning/course_list.html'
    context_object_name = 'course_object_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = datetime.date.today()  # Ajoute la date du jour au contexte
        return context

# 3. Détail d'un cours spécifique
class CourseDetail(LoginRequiredMixin, DetailView):
    model = LearningCourse
    template_name = 'employee_learning/course_detail.html'
    context_object_name = 'course_object'

# 4. Formulaire de création de cours
class CourseCreate(LoginRequiredMixin, CreateView):
    model = LearningCourse
    template_name = 'employee_learning/course_create.html'
    fields = ('title', 'level', 'employee')  # Champs affichés dans le formulaire
    success_url = reverse_lazy('course_list')  # Redirection après validation

# 5. Formulaire de modification
class CourseUpdate(LoginRequiredMixin, UpdateView):
    model = LearningCourse
    template_name = 'employee_learning/course_update.html'
    fields = ('title', 'level', 'employee')
    success_url = reverse_lazy('course_list')

# 6. Page de confirmation de suppression
class CourseDelete(LoginRequiredMixin, DeleteView):
    model = LearningCourse
    template_name = 'employee_learning/course_delete.html'
    success_url = reverse_lazy('course_list')