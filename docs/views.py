from django.shortcuts import render, get_object_or_404
from .models import Document, Category

# Create your views here.
def doc_detail(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    categories = Category.objects.prefetch_related('document_set')
    return render(request, 'home.html', {
        'doc': doc,
        'categories': categories,
    })

def home(request):
    doc = Document.objects.first()
    categories = Category.objects.prefetch_related('document_set')

    return render(request, 'home.html', {
        'doc': doc,
        'categories': categories,
    })