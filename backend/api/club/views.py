from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from datetime import date, timedelta

from .serializers import MaterialGroupSerializer, VideoSerializer, BookSerializer, AudioSerializer, StatusSerializer, SimpleMaterialGroupSerializer
from club.models import *
from account.models import Account

class StatusListView(APIView):
	def get(self, request):
		status_list = Status.objects.all()
		serializer = StatusSerializer(status_list, many=True)
		return Response(serializer.data)

class MaterialGroupView(APIView):
	def get(self, request):
		account = Account.objects.get(user=request.user)
		material_groups = MaterialGroup.objects.filter(status__level__lte=account.status.level)
		serializer = MaterialGroupSerializer(material_groups, many=True)
		return Response(serializer.data)

class SimpleMaterialGroupView(APIView):
	def get(self, request):
		material_groups = MaterialGroup.objects.filter(status__level__lte=0)
		serializer = MaterialGroupSerializer(material_groups, many=True)
		return Response(serializer.data)

class AllMaterialGroupView(APIView):
	def get(self, request):
		material_groups = MaterialGroup.objects.all()
		serializer = SimpleMaterialGroupSerializer(material_groups, many=True)
		return Response(serializer.data)

class MaterialGroupDetailView(APIView):
	permission_classes = [IsAuthenticated]
	def get(self, request, pk):
		try:
			material_group = MaterialGroup.objects.get(pk=pk)
		except:
			return Response({'errors': 'Beýle gruppa tapylmady'}, status=status.HTTP_404_NOT_FOUND)

		serializer = MaterialGroupSerializer(material_group)
		return Response({'success': True, 'status': status.HTTP_200_OK, 'data': serializer.data})

class VideoListView(APIView):
	permission_classes = [IsAuthenticated]
	def get(self, request, pk):
		account = Account.objects.get(user=request.user)
		group = MaterialGroup.objects.get(pk=pk)
		try:
			videos = Video.objects.filter(group__id=pk).order_by('-created_at')
		except:
			return Response({'errors': 'Video tapylmady'}, status=status.HTTP_404_NOT_FOUND)
		if account.status.level >= group.status.level:
			if account.status.level == group.status.level & account.status.level != 4 :
				account_created = account.created_at - timedelta(days=30)
				# print(account_created)
				videos = videos.filter(created_at__gte=account_created )
			serializer = VideoSerializer(videos, many=True)
			return Response(serializer.data)

		else:
			return Response({"error":"У вас нет разрешения для просмотров этого видео"})

class AudioListView(APIView):
	permission_classes = [IsAuthenticated]
	def get(self, request, pk):
		account = Account.objects.get(user=request.user)
		group = MaterialGroup.objects.get(pk=pk)
		try:
			audio = Audio.objects.filter(group__id=pk).order_by('-created_at')
		except:
			return Response({'errors': 'Audio tapylmady'}, status=status.HTTP_404_NOT_FOUND)
		if account.status.level >= group.status.level:
			if account.status.level == group.status.level & account.status.level != 4 :
				account_created = account.created_at - timedelta(days=30)
				print(account_created)
				audio = audio.filter(created_at__gte=account_created )
			serializer = AudioSerializer(audio, many=True)
			return Response(serializer.data)

		else:
			return Response({"error":"У вас нет разрешения для просмотров этого видео"})

class BookListView(APIView):
	permission_classes = [IsAuthenticated]
	def get(self, request, pk):
		account = Account.objects.get(user=request.user)
		group = MaterialGroup.objects.get(pk=pk)
		try:
			book = PDFMaterial.objects.filter(group__id=pk).order_by('-created_at')
		except:
			return Response({'errors': 'Kitap tapylmady'}, status=status.HTTP_404_NOT_FOUND)
		if account.status.level >= group.status.level:
			if account.status.level == group.status.level & account.status.level != 4 :
				account_created = account.created_at - timedelta(days=30)
				print(account_created)
				book = book.filter(created_at__gte=account_created )
			serializer = BookSerializer(book, many=True)
			return Response(serializer.data)

		else:
			return Response({"error":"У вас нет разрешения для просмотров этого видео"})

class FreeVideoListView(APIView):
	def get(self, request, pk):
		group = MaterialGroup.objects.get(pk=pk)
		if group.status.title == 'FREE':
			try:
					videos = Video.objects.filter(group__id=pk).order_by('-created_at')
			except:
				return Response({'errors': 'Video tapylmady'}, status=status.HTTP_404_NOT_FOUND)
		else:
			return Response({"error":"У вас нет разрешения для просмотров этого видео"})

		serializer = VideoSerializer(videos, many=True)
		return Response(serializer.data)

class FreeAudioListView(APIView):
	def get(self, request, pk):
		group = MaterialGroup.objects.get(pk=pk)
		print(group.status.title)
		if group.status.title == 'FREE':
			try:
					audios = Audio.objects.filter(group__id=pk).order_by('-created_at')
			except:
				return Response({'errors': 'Audio tapylmady'}, status=status.HTTP_404_NOT_FOUND)
		else:
			return Response({"error":"У вас нет разрешения для просмотров этого видео"})

		serializer = AudioSerializer(audios, many=True)
		return Response(serializer.data)

class FreeBookListView(APIView):
	def get(self, request, pk):
		group = MaterialGroup.objects.get(pk=pk)
		print(group.status.title)
		if group.status.title == 'FREE':
			try:
					book = PDFMaterial.objects.filter(group__id=pk).order_by('-created_at')
			except:
				return Response({'errors': 'Kitap tapylmady'}, status=status.HTTP_404_NOT_FOUND)
		else:
			return Response({"error":"У вас нет разрешения для просмотров этого видео"})

		serializer = BookSerializer(book, many=True)
		return Response(serializer.data)


class VideoDetailView(APIView):
	def get(self, request, pk):
		try:
			video = Video.objects.get(pk=pk).order_by('-created_at')
		except:
			return Response({'errors': 'Video tapylmady'}, status=status.HTTP_404_NOT_FOUND)
		serializer = VideoSerializer(video)
		return Response({'success': True, 'status': status.HTTP_200_OK, 'data': serializer.data})


class AudioDetailView(APIView):
	def get(self, request, pk):
		try:
			audio = Audio.objects.get(pk=pk)
		except:
			return Response({'errors': 'Audio tapylmady'}, status=status.HTTP_404_NOT_FOUND)
		serializer = AudioSerializer(audio)
		return Response({'success': True, 'status': status.HTTP_200_OK, 'data': serializer.data})

class BookDetailView(APIView):
	def get(self, request, pk):
		try:
			book = PDFMaterial.objects.get(pk=pk)
		except:
			return Response({'errors': 'Audio tapylmady'}, status=status.HTTP_404_NOT_FOUND)
		serializer = BookSerializer(book)
		return Response({'success': True, 'status': status.HTTP_200_OK, 'data': serializer.data})
