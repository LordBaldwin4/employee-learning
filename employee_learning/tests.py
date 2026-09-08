from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Division, Employee, LearningCourse


class LearningCourseViewsTests(TestCase):
	def setUp(self):
		self.division = Division.objects.create(div_name='Technologie', in_scope=True)
		self.employee = Employee.objects.create(name='Awa Diop', division=self.division)
		self.course = LearningCourse.objects.create(title='Python', level='B')
		self.course.employee.add(self.employee)
		self.user = get_user_model().objects.create_user(
			username='learner',
			password='strong-test-password',
		)

	def test_course_list_requires_authentication(self):
		response = self.client.get(reverse('course_list'))

		self.assertRedirects(
			response,
			f'{reverse("account_login")}?next={reverse("course_list")}',
		)

	def test_authenticated_course_list_is_sorted_by_title(self):
		LearningCourse.objects.create(title='Analyse de données', level='I')
		self.client.force_login(self.user)

		response = self.client.get(reverse('course_list'))

		self.assertEqual(response.status_code, 200)
		self.assertEqual(
			list(response.context['course_object_list'].values_list('title', flat=True)),
			['Analyse de données', 'Python'],
		)

	def test_course_detail_exposes_registered_employee(self):
		self.client.force_login(self.user)

		response = self.client.get(reverse('course_detail', args=[self.course.pk]))

		self.assertContains(response, 'Awa Diop')
		self.assertContains(response, 'Technologie')
