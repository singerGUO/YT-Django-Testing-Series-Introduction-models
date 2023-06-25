from django.test import TestCase
from app1.models import *
from django.contrib.auth.models import User
from model_bakery import baker
from pprint import pprint


class TestAppModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        print('db test')
        # Set up data for the whole TestCase
        testuser = User.objects.create_user(
            username='testuser', password='12345')
        testuser2 = User.objects.create_user(
            username='testuser2', password='12345')
        cls.new = Post.objects.create(
            title="django", content="New content", slug="django")
        cls.new.likes.set([testuser.pk, testuser2.pk])

    def test_model_str1(self):
        self.assertEqual(str(self.new), "django")

    def test_post_has_an_author(self):
        self.assertEqual(self.new.likes.count(), 2)

    def test_get_absolute_url(self):
        self.new.slug = Post.objects.get(id=1)
        self.assertEqual("/django/", self.new.slug.get_absolute_url())


class TestModelBakery(TestCase):

    def setUp(self):
        self.post = baker.make('app1.Post', title='Django Testing', _quantity=5)

    def test_create_multiple_model(self):
        for model in self.post:
            model.title = 'Updated Name'
            model.save()
        Posts = Post.objects.all()  # 5
        self.assertEqual(len(Posts), 5)
        content = Post.objects.create(title="new_content", content="This is some content")
        self.assertEqual(len(self.post), 5)
        Posts = Post.objects.all()
        self.assertEqual(len(Posts), 6)
        self.assertEqual(str(content), "new_content")


class TestModelwithTupleofTuple(TestCase):
    def test_create_multiple_model(self):
        instance = MyModel.objects.create(my_field='option2')
        pprint(instance.__dict__)
        instance = MyModel.objects.get(pk=1)# check it above
        self.assertEqual(str(instance.my_field), "option2")
        self.assertEqual(str(instance.get_my_field_display()), "Option 2")
        choices = MyModel.MY_CHOICES
        print(choices)


