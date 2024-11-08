from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Mission, Target
from .serializers import MissionSerializer, TargetSerializer
from cats.models import Cat

class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def create(self, request, *args, **kwargs):
        targets_data = request.data.pop('targets', [])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mission = serializer.save()

        for target_data in targets_data:
            target_serializer = TargetSerializer(data=target_data)
            target_serializer.is_valid(raise_exception=True)
            target_serializer.save(mission=mission)

        return Response(serializer.data, status=status.HTTP_201_CREATED)