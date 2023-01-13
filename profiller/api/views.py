from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from profiller.models import Profil, ProfilDurum
from profiller.api.serializers import ProfilSerializer, ProfilDurumSerializer, ProfilFotoSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet, ModelViewSet
from rest_framework import generics, mixins, views
from profiller.api.permissions import kendiProfiliYaDaReadOnly, durumSahibiYaDaReadOnly

class ProfilViewSet(

    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,

    ):

    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer
    permission_classes = [IsAuthenticated, kendiProfiliYaDaReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['sehir']

class ProfilDurumViewSet(ModelViewSet):

    serializer_class = ProfilDurumSerializer
    permission_classes = [IsAuthenticated, durumSahibiYaDaReadOnly]

    def get_queryset(self):

        queryset = ProfilDurum.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user_profil__user__username=username)
        return queryset

    def perform_create(self, serializer):
        user_profil = self.request.user.Profil
        serializer.save(user_profil=user_profil)

class ProfilFotoUpdateView(generics.UpdateAPIView):

    serializer_class = ProfilFotoSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profil_nesnesi = self.request.user.Profil
        return profil_nesnesi

