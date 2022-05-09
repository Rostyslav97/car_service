from rest_framework.generics import ListAPIView
from core.models import Defect
from core.serializers import DefectSerializer


class ListDefectAPI(ListAPIView):
    queryset = Defect.objects.all()
    serializer_class = DefectSerializer
    