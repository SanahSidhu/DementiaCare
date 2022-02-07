from rest_framework import status
from django.http import response

from .errors import InvalidUserCredentialsError, UserDoesNotExistError, UserExistsError


def signup_user(request, **kwargs) -> response.JsonResponse:
    try:
        print("Register")
        print("request.data", request.data)

        name = request.data.get("Name")
        email = request.data.get("Email")
        password = request.data.get("Password")
        phone_num = request.data.get("Phone Number")
        emergency_contact = request.data.get("Emergency Contact")

        print(name, email, password, phone_num, emergency_contact)

        # required: function to insert user data into db

    except UserExistsError as uee:
        return response.JsonResponse(
            {"error": str(uee)},
            status=status.HTTP_400_BAD_REQUEST,
        )

    except Exception as e:
        print(e)
        return response.JsonResponse(
            {
                "error": "Error Occured While Receiving Registration Data",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def login_user(request, **kwargs) -> response.JsonResponse:
    try:
        print("Login")
        print("request.data", request.data)

        email = request.data.get("Email")
        password = request.data.get("Password")

        print(email, password)

        # required: function to match email with password

    except UserDoesNotExistError as udne:
        return response.JsonResponse(
            {"error": str(udne)},
            status=status.HTTP_404_NOT_FOUND,
        )

    except InvalidUserCredentialsError as ice:
        return response.JsonResponse(
            {"error": str(ice)},
            status=status.HTTP_401_UNAUTHORIZED,
        )

    except Exception as e:
        print(e)
        return response.JsonResponse(
            {
                "error": "Error Occured While Receiving Login Data",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def recv_checklist(request, **kwargs) -> response.JsonResponse:
    try:
        print("Receive check list data")
        print("request.data", request.data)

        checkbox = request.data.get("Checkbox")
        checkbox_text = request.data.get("Text")

        # required: function to insert data into db

        return response.JsonResponse(
            {"success_status": True},
            status=status.HTTP_200_OK,
        )

    except Exception as e:
        print(e)
        return response.JsonResponse(
            {"error": "Error Occured While Receiving Data", "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def send_checklist():
    pass


def recv_media():
    pass


def send_media():
    pass


def send_medlist():
    pass


def recv_medlist():
    pass


def send_inventory():
    pass


def recv_inventory():
    pass
