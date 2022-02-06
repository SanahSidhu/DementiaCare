from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from django.http import response
from core.throttle import throttle

class signup(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]
    
    def post(self, request, **kwargs) -> response.JsonResponse:
        pass

class Login(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]

    def post(self, request, **kwargs) -> response.JsonResponse:
        pass


class CheckList(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]

    def get(self, request, **kwargs) -> response.JsonResponse:
        pass

    def post(self, request, **kwargs) -> response.JsonResponse:
        pass


class Media(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]

    def get(selfself, request, **kwargs) -> response.JsonResponse:
        pass

    def post(self, request, **kwargs) -> response.JsonResponse:
        pass


class MedList(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]

    def get(selfself, request, **kwargs) -> response.JsonResponse:
        pass

    def post(self, request, **kwargs) -> response.JsonResponse:
        pass


class Inventory(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]

    def get(selfself, request, **kwargs) -> response.JsonResponse:
        pass

    def post(self, request, **kwargs) -> response.JsonResponse:
        pass
