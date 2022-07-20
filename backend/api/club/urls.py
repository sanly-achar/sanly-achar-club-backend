from django.urls import path

from .views import (
	MaterialGroupView,
	MaterialGroupDetailView,
	VideoDetailView,
	AudioDetailView,
	BookDetailView,
	StatusListView,
	SimpleMaterialGroupView,
	AllMaterialGroupView,
	VideoListView,
	AudioListView,
	BookListView,
	FreeVideoListView,
	FreeAudioListView,
	FreeBookListView
	)

urlpatterns = [
	path('status/list/', StatusListView.as_view(), name='status_list'),
	path('group/allgroups/', AllMaterialGroupView.as_view(), name='allgroups'),
	path('group/free/video/<int:pk>/', FreeVideoListView.as_view(), name='free-videos-list'),
	path('group/free/audio/<int:pk>/', FreeAudioListView.as_view(), name='free-audio-list'),
	path('group/free/book/<int:pk>/', FreeBookListView.as_view(), name='free-book-list'),
	path('group/list/', MaterialGroupView.as_view(), name='group-list'),
	path('group/<int:pk>/', MaterialGroupDetailView.as_view(), name='group-detail'),
	path('video/list/<int:pk>/', VideoListView.as_view(), name='video-list'),
	path('audio/list/<int:pk>/', AudioListView.as_view(), name='audio-list'),
	path('book/list/<int:pk>/', BookListView.as_view(), name='book-list'),
	path('video/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
	path('audio/<int:pk>/', AudioDetailView.as_view(), name='audio-detail'),
	path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]