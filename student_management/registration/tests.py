from django.test import TestCase
from django.urls import reverse

from .models import Student


class StudentRegistrationTests(TestCase):
    def test_registration_page_loads(self):
        response = self.client.get(reverse('student_registration'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/student_registration.html')

    def test_post_creates_student_and_redirects(self):
        response = self.client.post(
            reverse('student_registration'),
            {
                'student_id': 'S001',
                'first_name': 'John',
                'last_name': 'Doe',
                'gender': 'MALE',
                'date_of_birth': '2000-01-01',
                'contact_number': '1234567890',
            },
        )

        self.assertRedirects(response, reverse('registration_success'))
        self.assertTrue(Student.objects.filter(student_id='S001').exists())

    def test_registration_success_page_loads(self):
        response = self.client.get(reverse('registration_success'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/registration_success.html')
