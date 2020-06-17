from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

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


class HelloViewSet(viewsets.ViewSet):
    """Test APi ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'User actions (List, Create, Retrieve, Update, Partial_Update)',
            'Automatically Maps TO URLs Using Routers',
            'Provides More Functionality With Less Code',
        ]

        return Response({'message' : 'Hello' , 'a_viewset' : a_viewset})

    def create(self, request, pk=None):
        """Create a new HEllo Message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = [
                f'Hello {name}',
                'This is Create Method'
            ]
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle Getting an Object By Its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle Update an Object By Its ID"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle Updating Part an Object By Its ID"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle Removing an Object"""
        return Response({'http_method': 'DELETE'})
