from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Event, Category
from .serializers import EventSerializer, CategorySerializer
from django.utils import timezone

# Create Event
@api_view(['POST'])
def create_event(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Update Event
@api_view(['PUT'])
def update_event(request, pk):
    event = Event.objects.get(pk=pk)
    serializer = EventSerializer(event, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Category List
@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

# Create Category
@api_view(['POST'])
def create_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete Category
@api_view(['DELETE'])
def delete_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    if category.event_set.exists():
        return Response({"error": "Category contains events"}, status=status.HTTP_400_BAD_REQUEST)
    category.delete()
    return Response({"message": "Category deleted"}, status=status.HTTP_204_NO_CONTENT)

# Category Events
@api_view(['GET'])
def category_events(request, category_id):
    events = Event.objects.filter(category_id=category_id)
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)

# Event Chart Data
@api_view(['GET'])
def event_chart(request):
    categories = Category.objects.all()
    pending_counts = {
        category.name: Event.objects.filter(
            category=category, start_date__gt=timezone.now()
        ).count() for category in categories
    }
    return Response(pending_counts)