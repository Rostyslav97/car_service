from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from core.models import Defect
from core.serializers import DefectSerializer, DefectCreateSerializer
from core.permissions import IsOwner
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class ListDefectAPI(ListAPIView):
    queryset = Defect.objects.all()
    serializer_class = DefectSerializer
    permission_classes = (IsAdminUser, )
    

class RetrieveDefectAPI(RetrieveAPIView):
    queryset = Defect.objects.all()
    serializer_class = DefectSerializer
    lookup_field = "id"
    permission_classes = (IsAdminUser, )


class CreateDefectAPI(CreateAPIView):
    queryset = Defect.objects.all()
    serializer_class = DefectCreateSerializer
    permission_classes = (IsAuthenticated, )


class UpdateDefectAPI(UpdateAPIView):
    queryset = Defect.objects.all()
    serializer_class = DefectSerializer
    lookup_field = "id"
    permission_classes = (IsOwner, )


class DestroyDefectAPI(DestroyAPIView):
    queryset = Defect.objects.all()
    serializer_class = DefectSerializer
    lookup_field = "id"
    permission_classes = (IsOwner, )
