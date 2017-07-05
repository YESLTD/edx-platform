"""
Django management command to generate a test course in a specific modulestore
"""
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from contentstore.management.commands.utils import user_from_str
from contentstore.views.course import create_new_course_in_store
from xmodule.modulestore import ModuleStoreEnum

import json


class Command(BaseCommand):
    """ Generate a basic course """
    help = 'Generate a course with settings on studio'

    def add_arguments(self, parser):
        parser.add_argument('json', help='A json object with the following fields: store, user, name, organization, number, fields')

    def handle(self, *args, **options):
        settings = json.loads(options["json"])
        store = settings["store"]
        user = user_from_str(settings["user"])
        org = settings["organization"]
        num = settings["number"]
        run = settings["run"]
        fields = settings["fields"]

        # Create the course
        new_course = create_new_course_in_store(store, user, org, num, run, fields)
        self.stdout.write(u"Created {}".format(unicode(new_course.id)))
