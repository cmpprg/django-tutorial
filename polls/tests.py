import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    """
    Tests for the Question Model
    """
    #METHOD TESTS
    def test_was_published_recently_with_future_question(self):
        """
        Test that checks was_published_recently() returns false if question's
        publication date is in the future 
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    
    def test_was_published_recently_with_old_question(self):
        """
        Test that checks was_published_recently() returns false if question's
        publication date is older than 1 day
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    
    def test_was_published_recently_with_recent_question(self):
        """
        Test that checks was_published_recently() returns true if question's
        publication date is within the last day
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

