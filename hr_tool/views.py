from django.shortcuts import render

# Create your views here.
def employee_list(request):
    return render(request, 'list.html')


def detail(request, pk):
    return render(request, 'detail.html')
