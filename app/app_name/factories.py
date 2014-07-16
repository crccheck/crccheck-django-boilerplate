"""
Factory-boy Cheatsheet:

class FooFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = models.Foo
    updated_at = factory.LazyAttribute(lambda __: now())
"""
import factory

from . import models
