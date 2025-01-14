from django.test import TestCase
from app1.models import *
from django.contrib.auth.models import User
from model_bakery import baker
from pprint import pprint


class TestAppModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        # print('db test')
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

    def test_create_customer_with_random_data(self):
        # Create a Customer instance with random data
        customer = baker.make('app1.ModelTestRandomField', _fill_optional=True)

        # Access the fields and verify the data
        # print(customer.name)  # Randomly generated name
        # print(customer.age)  # Randomly generated age
        # print(customer.email)  # Randomly generated email

        # You can also assert specific conditions
        self.assertTrue(customer.name)
        self.assertIsInstance(customer.age, int)
        self.assertRegex(customer.email, r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

        customer2 = baker.make('app1.ModelTestRandomField', _fill_optional=['age', 'email'])

        # print(customer2.name)  # Randomly generated name
        # print(customer2.age)  # Randomly generated age
        # print(customer2.email)  # Randomly generated email

        self.assertIsNone(customer2.name)
        self.assertIsInstance(customer2.age, int)
        self.assertRegex(customer2.email, r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')


class TestModelwithTupleofTuple(TestCase):
    def test_create_multiple_model(self):
        instance = ModelwithTupleTuple.objects.create(my_field='option2')
        #   pprint(instance.__dict__)
        instance = ModelwithTupleTuple.objects.get(pk=1)  # check it above
        self.assertEqual(str(instance.my_field), "option2")
        self.assertEqual(str(instance.get_my_field_display()), "Option 2")
    # choices = ModelwithTupleTuple.MY_CHOICES


class TestCustomModelField(TestCase):
    def test_custom_model_field(self):
        # Create and save a MyModel instance
        my_instance = MyModel()
        my_instance.my_field = 'hello'
        my_instance.save()  # now it is capitalized by get_prep_value in database Hello

        # # Retrieve the MyModel instance from the database
        retrieved_instance = MyModel.objects.get(
            id=my_instance.id)  # when we got it from database, Hello is passed in and upper by from from_db_value HELLO
        print(retrieved_instance.my_field)  # Output: 'HELLO'
        retrieved_instance = MyModel.objects.get(id=my_instance.id)


class TestRelatedName(TestCase):
    def test_create_without_related_name(self):
        math = Subject(name="Math")
        science = Subject(name="Science")
        engineering = Subject(name="Engineering")
        math.save()
        engineering.save()
        science.save()
        anthony = Student(name="Athony", major=math)
        billy = Student(name="Billy", major=math)
        christina = Student(name="Christina", major=science)
        anthony.save()
        billy.save()
        christina.save()
        print(math.student_set.all())
        print(science.student_set.all())
        print(engineering.student_set.all())
        anthony = Student.objects.get(pk=1)
        print(anthony.major)
        print(anthony.minor)

        science = Subject.objects.get(pk=2)
        anthony.minor = science
        anthony.save()
        print(science.student_set.all())
        print(science.minor_students.all())



