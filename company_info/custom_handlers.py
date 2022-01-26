from operator import imod
from urllib import request
from rest_framework.response import Response
from rest_framework.views import exception_handler
from django.http import JsonResponse
from rest_framework import status
import linecache
import sys
import traceback
import os
import inspect
# def custom_exception_handler(exc, context):
#     response=exception_handler(exc, context)

#     if response is not None:
#         return response
    
#     print(exc)
#     exc_list=str(exc).split("Detail: ")
#     return Response({'error':exc_list[-1]}, status=403)


def custom_exception_handler(exc, context):
    handlers={
        "ValidationError":_handle_generic_error,
        "Http404":_handle_generic_error,
        "PermissionDenied":_handle_generic_error,
        "NotAuthenticated":handle_authentication_error,
    } 
    response=exception_handler(exc, context)


        

    exception_class=exc.__class__.__name__

    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)

    if response is not None:
        response.data['status_code']=response.status_code


    if response is None:
        # filename=inspect.currentframe().f_back.f_code.co_filename
        # frame = inspect.currentframe().f_back
        response = Response({'error': str(exc), 'status_code':status.HTTP_500_INTERNAL_SERVER_ERROR, 'Line_no':traceback.format_exc()}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return response


def _handle_generic_error(exc, context, response):
    response.data={
        'detail':'you have no access to perfome this section',
        'status_code':response.status_code
    }
    return response

def handle_authentication_error(exc, context, response):
   
    response.data= {
        'error':'Please Login to proceed!',
        'status_code':response.status_code
    }
    return response