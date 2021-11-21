from django.shortcuts import render
import json

# Create your views here.

def people(request):
    with open('data.json') as f:
        data = json.load(f)
        newdata = sorted(data, key=lambda d: d['age'])
    return render(request, 'people.html', context={'people': newdata})

def single_person(request, person_id):
    with open('data.json') as f:
        data = json.load(f)
    selected_person = None
    for person in data:
        if person['id'] == person_id:
            selected_person = person
    return render(request, 'person.html', {'person': selected_person})
