from django.urls import path
from .views import (
    create_event, update_event, category_list, create_category,
    delete_category, category_events, event_chart
)

urlpatterns = [
    path('events/create/', create_event, name='create_event'),
    path('events/update/<int:pk>/', update_event, name='update_event'),
    path('categories/', category_list, name='category_list'),
    path('categories/create/', create_category, name='create_category'),
    path('categories/delete/<int:category_id>/', delete_category, name='delete_category'),
    path('categories/<int:category_id>/events/', category_events, name='category_events'),
    path('events/chart/', event_chart, name='event_chart'),
]