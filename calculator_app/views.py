from django.shortcuts import render
from .models import Calculator_histoty

def index(request):
    return render(request, 'index.html')

def submit_answer(request):
    display = request.GET['display']
    try:
        answer = eval(display)
        calculations_history = Calculator_histoty(equation=display, result=answer)
        calculations_history.save()
    except (SyntaxError, ZeroDivisionError):
        answer = "Syntax Error"

    context = {
        'answer' : answer,
        'equation' :display
    }
    return render(request, 'index.html', context)

def history(request):
    calculations = Calculator_histoty.objects.all().order_by('-date_added')
    return render(request, 'history.html', {'calculations':calculations})

def clear_history(request):
    Calculator_histoty.objects.all().delete()
    return render(request, 'history.html')
