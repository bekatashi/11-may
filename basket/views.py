from rest_framework import views
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import permissions


class BasketApiView(views.APIView):
    # permission_classes = [permissions.IsAuthenticated,]
    def post(self, request):
        print(request.user)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
