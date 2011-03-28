from django.core.management.base import BaseCommand
from optparse import make_option
from projects import tasks
from projects.models import Project
from builds.models import Version

class Command(BaseCommand):
    """Custom management command to rebuild documentation for all projects on
    the site. Invoked via ``./manage.py update_repos``.
    """
    option_list = BaseCommand.option_list + (
        make_option('-p',
            action='store_true',
            dest='pdf',
            default=False,
            help='Make a pdf'
            ),
        make_option('-r',
            action='store_true',
            dest='record',
            default=False,
            help='Make a Build'
            ),
        make_option('-t',
            action='store_true',
            dest='touch',
            default=False,
            help='Touch the files'
            ),
        make_option('-V',
            dest='version',
            default=None,
            help='Build a version, or all versions'
            )
        )

    def handle(self, *args, **options):
        make_pdf = options['pdf']
        record = options['record']
        touch = options['touch']
        version = options['version']
        if len(args):
            for slug in args:
                if version and version != "all":
                    print "Updating version %s for %s" % (version, slug)
                    for version in Version.objects.filter(project__slug=slug,
                                                          slug=version):
                        tasks.update_docs(version.project_id,
                                          pdf=make_pdf,
                                          record=False,
                                          version_pk=version.pk)
                elif version == "all":
                    print "Updating all versions for %s" % slug
                    for version in Version.objects.filter(project__slug=slug,
                                                          active=True,
                                                          uploaded=False):
                        tasks.update_docs(pk=version.project_id,
                                          pdf=make_pdf,
                                          record=False,
                                          version_pk=version.pk)
                else:
                    p = Project.objects.get(slug=slug)
                    print "Building %s" % p
                    tasks.update_docs(pk=p.pk, pdf=make_pdf, touch=touch)
        else:
            if version == "all":
                print "Updating all versions"
                for version in Version.objects.filter(active=True,
                                                      uploaded=False):
                    tasks.update_docs(pk=version.project_id,
                                      pdf=make_pdf,
                                      record=record,
                                      touch=touch,
                                      version_pk=version.pk)
            else:
                print "Updating all docs"
                tasks.update_docs_pull(pdf=make_pdf,
                                       record=record,
                                       touch=touch)
