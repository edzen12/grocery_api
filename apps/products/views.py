from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import Product


class DemoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print(request.user)
        return Response({'success': "Авторизован"})


class ProductView(APIView):
    
    def get(self, request):
        category = self.request.query_params.get('category')
        if category:
            queryset = Product.objects.filter(category__category_name=category)
        else:
            queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryView(APIView):
    
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
