import datetime
from django.db import models


# 1. Modèle Division
class Division(models.Model):
    div_name = models.CharField(max_length=100, verbose_name='Nom de la division')
    in_scope = models.BooleanField(
        default=False,
        help_text='La division est-elle concernée par la formation ?',
    )

    def __str__(self):
        return self.div_name


# 2. Modèle Employee
class Employee(models.Model):
    PRIORITIES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]

    name = models.CharField(max_length=100, verbose_name='Nom complet')
    priority = models.CharField(
        max_length=1,
        verbose_name="Priorité d'apprentissage",
        choices=PRIORITIES,
        default="M"
    )
    reg_date = models.DateField(
        default=datetime.date.today,
        verbose_name="Date d'enregistrement"
    )

    # Relation Un-à-Plusieurs : Chaque employé appartient à une Division
    division = models.ForeignKey(Division, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} : {self.name}'


# 3. Modèle PersonalInfo
class PersonalInfo(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, primary_key=True)
    tel = models.CharField(max_length=20, verbose_name='Téléphone')
    address = models.CharField(max_length=255, verbose_name='Adresse')

    def __str__(self):
        return f"PersonalInfo of {self.employee.name}"


# 4. Modèle LearningCourse
class LearningCourse(models.Model):
    LEVELS = [
        ('B', 'Basic'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    ]
    title = models.CharField(max_length=200, verbose_name='Titre du cours')
    level = models.CharField(max_length=1, choices=LEVELS, default='B', verbose_name='Niveau')
    employee = models.ManyToManyField(
        Employee,
        related_name='courses',
        verbose_name='Employés inscrits',
    )

    def __str__(self):
        return self.title