#import APIview class from rest_framework.views module
from rest_framework.views import APIView
#import resonse object used to return responses
#from APIview
from rest_framework.response import Response
# from rest_framework.decorators import api_view

from rest_framework import status

from profiles_api import serializers

from rest_framework import viewsets


class HelloApiView(APIView):
    #Creates a new class based on APIview class
    #Define an application logic for our endpoint we will assign to this view
    #you define url and assign it to this view and django framework handles it
    #by calling the appropriate function in the view for the HTTP request
    """Test API view"""
    #APIview expects function for different HTTP requests that can be made
    #to view
    #set serializers
    serializer_class = serializers.HelloSerializer
    #
    # @api_view(['GET', 'POST'])
    def get(self,request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as functions (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your logic',
        'Is mapped manually to URLs',]
        # if request.method == 'POST':
        #     return Response({"message": "Got some data!", "data": request.data})
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):

        """Create hello message with our name"""
        #Retrieve a serialize and pass in data that was sent in request
        serializer = self.serializer_class(data=request.data)
        #validate a serializer
        #valoidate a name that is no longer than 10 characters
        if serializer.is_valid():
            #here retrieve name field from validated data
            name = serializer.validated_data.get('name')
            message = f'My name is {name}'
            surname = serializer.validated_data.get('surname')
            sur_message = f'My surname is {surname}'
            return Response({'name':message, 'surname':sur_message})
        else:
            return Response(serializer.errors,
            status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating object"""
        #here we add API view to just test a browser
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return hello message"""

        a_viewsets = [
        'Users action (list, create, retrieve, update, partial_update, delete)',
        'Automatically maps to URLs using Routers',
        'Provides more functionalities with less code']
        return Response({'message': 'hellow', 'a_viewsets': a_viewsets})


    def create(self, request):
        """Create a new hello message"""
        # retrieve our serializers
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            name_message = f"my name is {name}"
            surname = serializer.validated_data.get('surname')
            surname_message = f"My surname is {surname}"
            return Response({'name':name_message, 'surname':surname_message})
        else:
            return Response(serializer.erros, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""
        return Response({"http method":"GET"})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http method':'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http method':'PATCH'})
    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http method':'DELETE'})
