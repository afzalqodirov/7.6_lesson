from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from .models import New
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.response import Response

# my serializer
class NewsListSeria(ModelSerializer):
    class Meta:
        model = New
        fields = ['id','title','views_count']
class NewsDetailSeria(ModelSerializer):
    class Meta:
        model = New
        fields = '__all__'
# end serializer


#custom throttling
class CustomThrottle(AnonRateThrottle):
    scope = 'news'
# end


# viewset, listapiview
class NewsViewSet(ModelViewSet):
    def get_throttles(self):
        if self.action == 'list':
            return [CustomThrottle()]
        return []
    def get_serializer_class(self):
        if self.action == 'list':return NewsListSeria
        return NewsDetailSeria
    queryset = New.objects.all()

class NewsListView(ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewsListSeria
    pagination_class = LimitOffsetPagination
    throttle_classes = [AnonRateThrottle, UserRateThrottle]

class News2ListView(ListAPIView):
    class CustomPagination(LimitOffsetPagination):
        limit_query_param = 'size'
        offset_query_param = 'index_after'

        def get_paginated_response(self, data):
            return Response({
                'starts_from':int(self.request.GET.get('index_after'))+1,
                'size':self.request.GET.get('size'),
                'next':self.get_next_link(),
                'previous':self.get_previous_link(),
                'result':data})
                
    queryset = New.objects.all()
    serializer_class = NewsListSeria
    pagination_class = CustomPagination
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
