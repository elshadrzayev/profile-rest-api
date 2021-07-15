#import APIview class from rest_framework.views module
from rest_framework.views import APIView
#import resonse object used to return responses
#from APIview
from rest_framework.response import Response
# from rest_framework.decorators import api_view

class HelloApiView(APIView):
    #Creates a new class based on APIview class
    #Define an application logic for our endpoint we will assign to this view
    #you define url and assign it to this view and django framework handles it
    #by calling the appropriate function in the view for the HTTP request
    """Test API view"""
    #APIview expects function for different HTTP requests that can be made
    #to view

    #
    # @api_view(['GET', 'POST'])
    def get(request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as functions (get, post, patch, put, delete)',
        'Is similar to a traditional Django View',
        'Gives you the most control over your logic',
        'Is mapped manually to URLs',]
        # if request.method == 'POST':
        #     return Response({"message": "Got some data!", "data": request.data})
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
