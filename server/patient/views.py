from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from core.throttle import throttle
from django.http import response

from .utils import login_user, signup_user


class SignUp(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]

    def post(self, request, **kwargs) -> response.JsonResponse:
        """Receiving user signup data via POST requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """
        print("SignUp Post Request")

        singup_data = signup_user(request, **kwargs)

        return singup_data


class Login(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]

    def post(self, request, **kwargs) -> response.JsonResponse:
        """Receiving user login credentials via POST requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """
        print("Login Post Request")

        login_data = login_user(request, **kwargs)

        return login_data


class CheckList(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]

    def get(self, request, **kwargs) -> response.JsonResponse:
        pass

    def post(self, request, **kwargs) -> response.JsonResponse:
        pass


class Notes(APIView):
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


class Calendar(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]

    def get(self, request, **kwargs) -> response.JsonResponse:
        pass

    def post(self, request, **kwargs) -> response.JsonResponse:
        pass


class RemindersAlerts(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]

    def get(self, request, **kwargs) -> response.JsonResponse:
        pass

    def post(self, request, **kwargs) -> response.JsonResponse:
        pass


class EmergencyContacts(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = [throttle]

    def get(self, request, **kwargs) -> response.JsonResponse:
        pass

    def post(self, request, **kwargs) -> response.JsonResponse:
        pass
