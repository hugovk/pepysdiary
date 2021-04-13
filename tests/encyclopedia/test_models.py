from django.test import TestCase

from pepysdiary.encyclopedia.factories import (
    PersonTopicFactory,
    PlaceTopicFactory,
    TopicFactory,
)


# Only testing a handful of things at the moment.


class TopicTestCase(TestCase):
    def test_is_family_tree_true(self):
        topic = TopicFactory(id=7390)
        self.assertTrue(topic.is_family_tree)

    def test_is_family_tree_false(self):
        topic = TopicFactory(id=123)
        self.assertFalse(topic.is_family_tree)

    def test_is_person_true(self):
        topic = PersonTopicFactory()
        self.assertTrue(topic.is_person)

    def test_is_person_false(self):
        topic = TopicFactory()
        self.assertFalse(topic.is_person)

    def test_is_place_true(self):
        topic = PlaceTopicFactory()
        self.assertTrue(topic.is_place)

    def test_is_place_false(self):
        topic = TopicFactory()
        self.assertFalse(topic.is_person)
