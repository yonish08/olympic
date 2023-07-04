from core.models import AboutFunOlympic, User

def add_variable_to_context(request):
    orgInfo = AboutFunOlympic.objects.first()

    return {
        'org': orgInfo
    }