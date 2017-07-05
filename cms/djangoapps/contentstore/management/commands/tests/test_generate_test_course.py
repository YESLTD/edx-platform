"""
Unittest for generate a test course in an given modulestore
"""
import unittest
import ddt
from django.core.management import CommandError, call_command

from contentstore.management.commands.generate_test_course import Command
from xmodule.modulestore import ModuleStoreEnum
from xmodule.modulestore.tests.django_utils import ModuleStoreTestCase
from xmodule.modulestore.django import modulestore


@ddt.ddt
class TestGenerateTestCourse(ModuleStoreTestCase):
    """
    Unit tests for creating a course in either old mongo or split mongo via command line
    """

    @ddt.data(ModuleStoreEnum.Type.mongo, ModuleStoreEnum.Type.split)
    def test_generate_course_in_stores(self, store):
        call_command(
            "generate_test_course", '{"store":"' + store + '","user":"edx@example.com","name":"test-course","organization":"test-course-generator","number":"1","run":"1"}'
        )
        new_key = modulestore().make_course_key("test-course-generator", "1", "1")
        self.assertTrue(
            modulestore().has_course(new_key),
            "Could not find course in {}".format(store)
        )
        # pylint: disable=protected-access
        self.assertEqual(store, modulestore()._get_modulestore_for_courselike(new_key).get_modulestore_type())
