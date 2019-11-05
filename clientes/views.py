from django.views import generic
from .models import Cliente


class ClienteList(generic.ListView):
    model = Cliente


class ClienteDetail(generic.DetailView):
    model = Cliente
    



