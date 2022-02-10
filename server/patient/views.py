from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from core.throttle import throttle
from django.http import response

from .utils import (
    send_checklist_data,
    recv_checklist_data,
    send_medlist_data,
    recv_medlist_data,
    send_emg_contact,
    recv_emg_contact,
    send_notes_data,
    recv_notes_data,
    send_inv_data,
    recv_inv_data,
    signup_user,
    login_user,
)


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
    throttle_classes = [throttle]

    def get(self, request, **kwargs) -> response.JsonResponse:
        """Sending checklist data when hit with GET requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """

        print("Sending Checklist Data API")

        cl_data = send_checklist_data(request, **kwargs)

        return cl_data

    def post(self, request, **kwargs) -> response.JsonResponse:
        """Receiving checklist data via POST requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """

        print("Receiving Checklist Data API")

        cl_data = recv_checklist_data(request, **kwargs)

        return cl_data


class Notes(APIView):
    throttle_classes = [throttle]

    def get(self, request, **kwargs) -> response.JsonResponse:
        """Sending Notes data when hit with GET requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """

        print("Sending Notes Data API")

        nt_data = send_notes_data(request, **kwargs)

        return nt_data

    def post(self, request, **kwargs) -> response.JsonResponse:
        """Receiving Notes data via POST requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """

        print("Receiving Notes Data API")

        nt_data = recv_notes_data(request, **kwargs)

        return nt_data


class MedList(APIView):
    throttle_classes = [throttle]

    def get(self, request, **kwargs) -> response.JsonResponse:
        """Sending MedList data when hit with GET requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """

        print("Sending MedList Data API")

        ml_data = send_medlist_data(request, **kwargs)

        return ml_data

    def post(self, request, **kwargs) -> response.JsonResponse:
        """Receiving MedList data via POST requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """

        print("Receiving MedList Data API")

        ml_data = recv_medlist_data(request, **kwargs)

        return ml_data


class Inventory(APIView):
    throttle_classes = [throttle]

    def get(self, request, **kwargs) -> response.JsonResponse:
        """Sending inventory data when hit with GET requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """

        print("Sending Inventory Data API")

        inv_data = send_inv_data(request, **kwargs)

        return inv_data

    def post(self, request, **kwargs) -> response.JsonResponse:
        """Receiving inventory data via POST requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """

        print("Receiving Inventory Data API")

        inv_data = recv_inv_data(request, **kwargs)

        return inv_data


class Media(APIView):
    throttle_classes = [throttle]

    def get(selfself, request, **kwargs) -> response.JsonResponse:
        pass

    def post(self, request, **kwargs) -> response.JsonResponse:
        pass


class Calendar(APIView):
    throttle_classes = [throttle]

    def get(self, request, **kwargs) -> response.JsonResponse:
        pass

    def post(self, request, **kwargs) -> response.JsonResponse:
        pass


class RemindersAlerts(APIView):
    throttle_classes = [throttle]

    def get(self, request, **kwargs) -> response.JsonResponse:
        pass

    def post(self, request, **kwargs) -> response.JsonResponse:
        pass


class EmergencyContacts(APIView):
    throttle_classes = [throttle]

    def get(self, request, **kwargs) -> response.JsonResponse:
        """Sending emergency contact data when hit with GET requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """

        print("Sending Emergency Contact Data API")

        em_contact_data = send_emg_contact(request, **kwargs)

        return em_contact_data

    def post(self, request, **kwargs) -> response.JsonResponse:
        """Receiving emergency contact data via POST requests

        Args:
            request ([type])

        Returns:
            JsonResponse
        """

        print("Receiving Emergency Contact Data API")

        em_con_data = recv_emg_contact(request, **kwargs)

        return em_con_data
