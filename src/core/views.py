from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from core.models import Defect
from core.serializers import DefectSerializer, DefectCreateSerializer


class ListDefectAPI(ListAPIView):
    queryset = Defect.objects.all()
    serializer_class = DefectSerializer
    

class RetrieveDefectAPI(RetrieveAPIView):
    queryset = Defect.objects.all()
    serializer_class = DefectSerializer
    lookup_field = "id"


class CreateDefectAPI(CreateAPIView):
    queryset = Defect.objects.all()
    serializer_class = DefectCreateSerializer


class UpdateDefectAPI(UpdateAPIView):
    queryset = Defect.objects.all()
    serializer_class = DefectSerializer
    lookup_field = "id"


class DestroyDefectAPI(DestroyAPIView):
    queryset = Defect.objects.all()
    serializer_class = DefectSerializer
    lookup_field = "id"
    