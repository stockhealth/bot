# faqbot/management/commands/load_faqs.py
import json
from django.core.management.base import BaseCommand
from faqbot.models import FAQ

class Command(BaseCommand):
    help = 'Load FAQs from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='The JSON file containing the FAQs')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        with open(json_file, 'r') as file:
            faqs = json.load(file)
            for faq in faqs:
                FAQ.objects.create(question=faq['question'], answer=faq['answer'])
        self.stdout.write(self.style.SUCCESS('Successfully loaded FAQs'))
