from rest_framework import serializers
from club.models import *

class StatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = Status
		fields = '__all__'

class VideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Video
		fields = '__all__'
		depth = 1

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = PDFMaterial
		fields = '__all__'
		depth = 1

class AudioSerializer(serializers.ModelSerializer):
	class Meta:
		model = Audio
		fields = '__all__'
		depth = 1

class MaterialGroupSerializer(serializers.ModelSerializer):
	videos = VideoSerializer(read_only=True, many=True)
	audios = AudioSerializer(read_only=True, many=True)
	pdfmaterial = BookSerializer(read_only=True, many=True)

	class Meta:
		model = MaterialGroup
		fields = '__all__'
		depth = 1

class SimpleMaterialGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = MaterialGroup
		# fields = '__all__'
		exclude =( 'intro_video', )
		depth = 1

