import cgi
from django.shortcuts import render
from .models import Category
# Create your views here.
def post(request):
    if request.method == "GET" :
        my_category = Category.objects.all()
        return render(request, 'category.html', {'category':my_category})
    elif request.method == 'POST':
        title = request.POST.get('my-title','')
        content = request.POST.get('my-content','')

        cg = Category()
        cg.title = title
        cg.content = content
        cg.save()

        return render(request, 'category.html')
