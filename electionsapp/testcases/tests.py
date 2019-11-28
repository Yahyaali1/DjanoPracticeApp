import datetime
from django.utils import timezone
from django.test import TestCase
from django.urls import reverse
from django.http import Http404

from ..models import Question


class QuestionModelTest(TestCase):

    def test_was_recently_published(self):
        question = Question(pub_date=timezone.now()+datetime.timedelta(days=30))
        self.assertIs(question.was_recent_pub(), False)


class IndexViewTest(TestCase):

    def test_no_questions(self):
        response = self.client.get(reverse('elect:welcome'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['index_list'], [])


class DetailViewTest(TestCase):

    def test_invalid_question_id(self):
        response = self.client.get(reverse('elect:detail', args=(1000,)))
        self.assertEqual(response.status_code, 404)
