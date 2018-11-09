import random
from rest_framework import viewsets, response, decorators, views, status, generics

from contactlist import models, serializers


class ContactViewSet(viewsets.ModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer


@decorators.api_view(['GET'])
def custom_list(request):
    return response.Response({
        'magic_number': random.randint(0, 10),
    })


class ClassBasedMagicNumber(views.APIView):
    def get(self, request):
        return response.Response('ok')

    def post(self, request):
        return response.Response('post response')


class ContactsView(views.APIView):
    def get(self, request):
        contacts = models.Contact.objects.all()
        serializer = serializers.ContactSerializer(contacts, many=True)
        return response.Response(serializer.data)

    def post(self, request):
        serializer = serializers.ContactSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)


class ContactDetailView(generics.RetrieveAPIView, views.APIView):
    serializer_class = serializers.ContactSerializer
    queryset = models.Contact.objects.all()

    def patch(self, request, **kwargs):
        instance = self.get_object()
        serializer = serializers.ContactSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class AddressView(views.APIView):
    def post(self, request):
        serializer = serializers.AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
