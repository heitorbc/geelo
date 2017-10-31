import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: "user_%03d" % n)
    email = factory.Sequence(lambda n: "user_%03d@email.com" % n)
    password = factory.PostGenerationMethodCall('set_password', factory.Sequence(lambda n: "user_%03d123" % n))

    is_superuser = True
    is_staff = True
    is_active = True