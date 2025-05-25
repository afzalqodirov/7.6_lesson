from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from .models import New
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

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
    queryset = New.objects.all()
    serializer_class = NewsListSeria
    pagination_class = CustomPagination
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
