from django.shortcuts import render
from django.shortcuts import redirect,render
from .forms import *
from .models import *
from django.http import HttpResponse


# Create your views here.
def home(request):
    if request.method == 'POST':
        print(request.POST)
        questions = Quesmodel.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for q in questions:
            total += 1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score += 1
                correct += 1
            else:
                wrong += 1
        context = {
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'total': total,
        }
        return render(request, 'Result.html', context)
    else:
        questions = Quesmodel.objects.all()
        context = {
            'questions': questions
        }
        return render(request,'home.html', context)


def Addquestion(request):
    if request.user.is_staff:
        form = Addquestionform()
        if (request.method == 'POST'):
            form = Addquestionform(request.POST)
            if (form.is_valid()):
                form.save()
                return redirect('/')
        context = {'form': form}
        return render(request, 'Addquestion.html', context)
    else:
        return redirect('home')