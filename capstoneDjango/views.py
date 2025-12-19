from django.http import HttpResponse


def home(request):

    return HttpResponse("Welcomee to the API")
