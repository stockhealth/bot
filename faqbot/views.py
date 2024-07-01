# faqbot/views.py
from django.shortcuts import render
from .models import FAQ

def home(request):
    return render(request, 'faqbot/home.html')

def get_answer(request):
    query = request.GET.get('query')
    answer = FAQ.objects.filter(question__icontains=query).first()
    context = {'query': query, 'answer': answer}
    return render(request, 'faqbot/answer.html', context)
