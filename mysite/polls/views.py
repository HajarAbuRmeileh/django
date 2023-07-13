from django.shortcuts import render
from django.http import HttpResponse

#das
def index(request):
    # Get the value of the 'param' parameter from the URL
    param_value = request.GET.get('userMessage')
    #answer = response(param_value)
    # Do something with the parameter value
    if param_value:
        return HttpResponse(f"The value of 'param' is: {param_value}")
    else:
        return HttpResponse("No 'param' value provided.")

# Usage example
#print("Mobile Store ChatBot :)")
#while True:
 #   input_data = input("You- ")
  #  answer = response(input_data)
   # answer



