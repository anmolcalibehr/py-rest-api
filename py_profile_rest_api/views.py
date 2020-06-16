from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from py_profile_rest_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a lists of APIViews Features"""
        an_apiview = [
            'Uses HTTP Methods as function (get, post, patch, put, delete)'
            'Is Similar to a traditional Django View',
            'Gives you the most control over you applications logic',
            'Is Mapped Manaually to URLs',
        ]

        return Response({
            'message' : 'Hello, Youre into API World' ,
            'an_apiview' : an_apiview
        })    
    
    def post(self, request):
        """Create a HEllo Message With Our Name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle Updating an Object"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = [
                f'Hello {name}',
                'This is PUT Method'
            ]
            return Response({'method': 'PUT' , 'message' : message})

    def patch(self, request , pk=None):
        """Handle Partial Update of an Object"""
        return Response({'method': 'PATCH'})