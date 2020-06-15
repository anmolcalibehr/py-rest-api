from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

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