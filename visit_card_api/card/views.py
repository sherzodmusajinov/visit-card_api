from django.conf import settings
from PIL import Image, ImageDraw, ImageFont
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers


class VisitCardDataSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    pochta = serializers.CharField(max_length=255)
    manzil = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    name_company = serializers.CharField(max_length=255)


class VisitCardView(APIView):
    def post(self, request):

        serializer = VisitCardDataSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data


            img = Image.open('media/1.jpg')
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("media/font.ttf", 28)


            draw.text((500, 260), f"Phone: {data['phone']}", fill="red", font=font)
            draw.text((500, 316), f"Pochta: {data['pochta']}", fill="red", font=font)
            draw.text((500, 368), f"Manzil: {data['manzil']}", fill="red", font=font)
            draw.text((500, 417), f"Email: {data['email']}", fill="red", font=font)
            draw.text((500, 469), f"Company: {data['name_company']}", fill="red", font=font)

            file_name = f"vizit_card_{data['name_company']}.jpg"
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            img.save(file_path)

            return Response({"file_url": settings.MEDIA_URL + file_name}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
