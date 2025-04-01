from django.shortcuts import render,redirect
from models import Event,Category

# Create your views here.

def create_event(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        priority = request.POST.get('priority')
        description = request.POST.get('description')
        location = request.POST.get('location')
        organizer = request.POST.get('organizer')

        # Retrieve the Category object
        category = Category.objects.get(pk=category_id)
        event = Event.objects.create(
            name=name,
            category=category,
            start_date=start_date,
            end_date=end_date,
            priority=priority,
            description=description,
            location=location,
            organizer=organizer
        )
        return redirect('category_list')
    else:
        categories = Category.objects.all()
        return render(request, 'Event/create_event.html', {'categories': categories})
    

def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == 'POST':
        event.name = request.POST.get('name')
        event.start_date = request.POST.get('start_date')
        event.end_date = request.POST.get('end_date')
        event.priority = request.POST.get('priority')
        event.description = request.POST.get('description')
        event.location = request.POST.get('location')
        event.organizer = request.POST.get('organizer')
        event.save()
        return redirect('category_list')
    else:
        return render(request, 'Event/update_event.html', {'event': event})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'Event/category.html', {'categories': categories})

def create_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('category_list')
    return render(request, 'Event/create_category.html')
