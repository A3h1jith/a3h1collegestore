from .models import Department, Course


def dep_links(request):
    links = Department.objects.all()
    return dict(links=links)

def course_links(request):
    link_c = Course.objects.all()
    return dict(link_c=link_c)