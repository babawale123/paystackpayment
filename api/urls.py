from django.urls import path
from .views import (StreamList,StreamDetails,WatchListView,WatchDetails,ReviewList)


urlpatterns = [
    path('streams/', StreamList.as_view()),
    path('streams/<int:pk>/', StreamDetails.as_view()),
    path('watch/', WatchListView.as_view()),
    path('watch/<int:pk>/', WatchDetails.as_view()),
    path('review/', ReviewList.as_view()),

    #path('stream/<int:pk>/review-create', ReviewList.as_view()),
    #path('stream/<int:pk>/review', ReviewList.as_view()),
    
]