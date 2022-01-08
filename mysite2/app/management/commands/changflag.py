from django.core.management.base import BaseCommand, CommandError
from app.models import Person

# python manage.py changflag 1 4 5

class Command(BaseCommand):

    help = '提供人的id，变换其flag'

    def add_arguments(self, parser):
        parser.add_argument('person_ids', nargs='+', type=int)
        # pip install argparser

        parser.add_argument('--delete', action='store_true', help='删除指定的人')

    def handle(self, *args, **options):

        for person_id in options['person_ids']:

            try:
                person = Person.objects.get(pk=person_id)
            except Person.DoesNotExist:
                raise CommandError('你指定的id为%s的人不存在！'% person_id)
            if options['delete']:
                person.delete()
                self.stdout.write(self.style.SUCCESS('成功删除了id为%s的人' % person_id))
                continue

            person.flag = not person.flag
            person.save()
            self.stdout.write(self.style.SUCCESS('成功修改了id为%s的人的状态' % person_id))

