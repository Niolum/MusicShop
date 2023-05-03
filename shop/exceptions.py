from django.shortcuts import render

def handler404(request, exception=None):
    title='Ошибочка 404'
    data = {'title': title}
    return render(request, 'product/error404.html', status=404, context=data)

def handler500(request):
    title='Ошибочка 500'
    data = {'title': title}
    return render(request, 'product/error500.html', status=500, context=data)