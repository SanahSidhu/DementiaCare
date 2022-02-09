from rest_framework import status
from django.http import response

from .errors import (
    InvalidUserCredentialsError,
    InvalidInsertionError,
    UserDoesNotExistError,
    DataFetchingError,
    InvalidFieldError,
    DataRemovalError,
    UserExistsError,
)
from . import userdb


def signup_user(request, **kwargs) -> response.JsonResponse:
    try:
        print("POST REQUEST SIGNUP")
        print("Request Object DATA:", request.data)

        name = request.data.get("Name")
        email = request.data.get("Email")
        password = request.data.get("Password")
        phone_num = request.data.get("Phone Number")
        emergency_contact = request.data.get("Emergency Contact")

        print(name, email, password, phone_num, emergency_contact)

        userdb.insert_user(name, email, password, phone_num, emergency_contact)

        return response.JsonResponse(
            data={"success_status": True},
            status=status.HTTP_201_CREATED,
        )

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
        print("POST REQUEST LOGIN")
        print("Request Object DATA:", request.data)

        email = request.data.get("Email")
        password = request.data.get("Password")

        print(email, password)

        if userdb.check_hash(email, password):
            return response.JsonResponse(
                data={"success_status": True},
                status=status.HTTP_200_OK,
            )

    except InvalidUserCredentialsError as ice:
        return response.JsonResponse(
            {"error": str(ice)},
            status=status.HTTP_401_UNAUTHORIZED,
        )
    except UserDoesNotExistError as udne:
        return response.JsonResponse(
            {"error": str(udne)},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception as e:
        print(e)
        return response.JsonResponse(
            {
                "error": "Error Occured While Receiving Login Data",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def recv_checklist_data(request, **kwargs) -> response.JsonResponse:
    try:
        print("POST REQUEST CHECKLIST")
        print("request.data:", request.data)

        email = request.data.get("Email")
        text = request.data.get("Text")
        function = request.data.get("Function")

        if function == "Add":
            userdb.checklist_data(email, text, Add=True, cl=True)
        elif function == "Remove":
            userdb.checklist_data(email, text, Remove=True, cl=True)

        return response.JsonResponse(
            {"success_status": True},
            status=status.HTTP_200_OK,
        )

    except DataRemovalError as dre:
        return response.JsonResponse(
            {"error": str(dre)},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
    except InvalidInsertionError as iie:
        return response.JsonResponse(
            {"error": str(iie)},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )
    except UserDoesNotExistError as udne:
        return response.JsonResponse(
            {"error": str(udne)},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception as e:
        print(e)
        return response.JsonResponse(
            {"error": "Error Occured While Receiving Data", "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def send_checklist_data(request, **kwargs) -> response.JsonResponse:
    try:
        print("GET REQUEST CHECKLIST")
        print("request.data:", request.data)

        email = request.data.get("Email")

        userdb.get_db_data(email, cl=True)

    except InvalidFieldError as ife:
        return response.JsonResponse(
            {"error": str(ife)},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )
    except DataFetchingError as dfe:
        return response.JsonResponse(
            {"error": str(dfe), "success_status": False},
            status=status.HTTP_404_NOT_FOUND,
        )
    except Exception as e:
        print(e)
        return response.JsonResponse(
            {"error": "Error Occured While Sending Data", "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def recv_media(request, **kwargs) -> response.JsonResponse:
    try:
        print("Receive media")
        print("request.data:", request.data)

        # get user email
        # check image or video
        media = request.data.get("Media")

        # function to insert data into db

        return response.JsonResponse(
            {"success_status": True},
            status=status.HTTP_200_OK,
        )

    # other errors
    except Exception as e:
        print(e)
        return response.JsonResponse(
            {"error": "Error Occured While Receiving Data", "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def send_media():
    pass


def recv_medlist(request, **kwargs) -> response.JsonResponse:
    try:
        print("Receive medlist")
        print("request.data:", request.data)

        # get user email
        medname = request.data.get("Medicine")
        medinfo = request.data.get("Medicine Info")

        print(medname, medinfo)

        # function to insert data into db

        return response.JsonResponse(
            {"success_status": True},
            status=status.HTTP_200_OK,
        )

    # other errors
    except Exception as e:
        print(e)
        return response.JsonResponse(
            {"error": "Error Occured While Receiving Data", "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def send_medlist():
    pass


def recv_inventory(request, **kwargs) -> response.JsonResponse:
    try:
        print("Receive inventory")
        print("request.data:", request.data)

        # get user email
        item = request.data.get("Item")
        iteminfo = request.data.get("ItemInfo")

        print(item, iteminfo)

        # function to insert data into db

        return response.JsonResponse(
            {"success_status": True},
            status=status.HTTP_200_OK,
        )

    # other errors
    except Exception as e:
        print(e)
        return response.JsonResponse(
            {"error": "Error Occured While Receiving Data", "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def send_inventory():
    pass


def recv_caldata(request, **kwargs) -> response.JsonResponse:
    try:
        print("Receive caldata")
        print("request.data:", request.data)

        # get user email
        date = request.data.get("Date")
        event = request.data.get("Event")

        print(date, event)

        # function to insert data into db

        return response.JsonResponse(
            {"success_status": True},
            status=status.HTTP_200_OK,
        )

    # other errors
    except Exception as e:
        print(e)
        return response.JsonResponse(
            {"error": "Error Occured While Receiving Data", "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def send_caldata():
    pass


def send_reminder():
    pass


def recv_emcontact(request, **kwargs) -> response.JsonResponse:
    try:
        print("Receive medlist")
        print("request.data:", request.data)

        # get user email
        contact_name = request.data.get("ContactName")
        contact_num = request.data.get("ContactPhone")

        print(contact_name, contact_num)

        # function to insert data into db

        return response.JsonResponse(
            {"success_status": True},
            status=status.HTTP_200_OK,
        )

    # other errors
    except Exception as e:
        print(e)
        return response.JsonResponse(
            {"error": "Error Occured While Receiving Data", "success_status": False},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


def send_emcontacts():
    pass
