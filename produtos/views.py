from django.views.generic import ListView
from .models import Produto


class ProdutoList(ListView):
    model = Produto

