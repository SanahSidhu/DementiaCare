from rest_framework import status
from django.http import response
import datetime as d

from core.settings import AWS_BUCKET_FOLDER, AWS_OBJECT_URL_PREFIX
from .errors import (
    DataInsertionError,
    InvalidUserCredentialsError,
    UserDoesNotExistError,
    InvalidInsertionError,
    DataFetchingError,
    InvalidFieldError,
    DataRemovalError,
    UserExistsError,
)
from . import userdb, s3


def signup_user(request, **kwargs) -> response.JsonResponse:
    try:
        print("POST REQUEST SIGNUP")
        print("Request Object DATA:", request.data)

        name = request.data.get("Name")
        email = request.data.get("Email")
        password = request.data.get("Password")
        phone_num = request.data.get("Phone Number")

        print(name, email, password, phone_num)

        userdb.insert_user(name, email, password, phone_num)

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
            userdb.insert_cl_nt_data(email, text, add=True, cl=True)
        elif function == "Remove":
            userdb.insert_cl_nt_data(email, text, remove=True, cl=True)

        return response.JsonResponse(
            {"success_status": True},
            status=status.HTTP_200_OK,
        )

    except DataRemovalError as dre:
        return response.JsonResponse(
            {"error": str(dre)},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
    except DataInsertionError as die:
        return response.JsonResponse(
            {"error": str(die)},
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

        userdb.get_cl_nt_data(email, cl=True)

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


def recv_notes_data(request, **kwargs) -> response.JsonResponse:
    try:
        print("POST REQUEST NOTES")
        print("request.data:", request.data)

        email = request.data.get("Email")
        note = request.data.get("Note")
        function = request.data.get("Function")

        if function == "Add":
            userdb.insert_cl_nt_data(email, note, add=True, nt=True)
        elif function == "Remove":
            userdb.insert_cl_nt_data(email, note, remove=True, nt=True)

        return response.JsonResponse(
            {"success_status": True},
            status=status.HTTP_200_OK,
        )

    except DataRemovalError as dre:
        return response.JsonResponse(
            {"error": str(dre)},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
    except DataInsertionError as die:
        return response.JsonResponse(
            {"error": str(die)},
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


def send_notes_data(request, **kwargs) -> response.JsonResponse:
    try:
        print("GET REQUEST NOTES")
        print("request.data:", request.data)

        email = request.data.get("Email")

        userdb.get_cl_nt_data(email, nt=True)

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


def recv_medlist_data(request, **kwargs) -> response.JsonResponse:
    try:
        print("POST REQUEST MEDLIST")
        print("request.data:", request.data)

        email = request.data.get("Email")
        medicine = request.data.get("Medicine")
        time = request.data.get("Time")
        purpose = request.data.get("Purpose")
        function = request.data.get("Function")

        time_lst = time.split(",")

        med_data = {
            "Medicine": medicine,
            "Purpose": purpose,
            "Time": time_lst,
        }

        if function == "Add":
            userdb.insert_ml_inv_emg_data(email, med_data, add=True, ml=True)
        elif function == "Remove":
            userdb.insert_ml_inv_emg_data(email, med_data, remove=True, ml=True)

        return response.JsonResponse(
            {"success_status": True},
            status=status.HTTP_200_OK,
        )

    except DataRemovalError as dre:
        return response.JsonResponse(
            {"error": str(dre)},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
    except DataInsertionError as die:
        return response.JsonResponse(
            {"error": str(die)},
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


def send_medlist_data(request, **kwargs) -> response.JsonResponse:
    try:
        print("GET REQUEST MEDLIST")
        print("request.data:", request.data)

        email = request.data.get("Email")

        userdb.get_ml_inv_emg_data(email, ml=True)

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


def recv_inv_data(request, **kwargs) -> response.JsonResponse:
    try:
        print("POST REQUEST INVENTORY")
        print("request.data:", request.data)

        email = request.data.get("Email")
        item = request.data.get("Item")
        location = request.data.get("Location")
        function = request.data.get("Function")

        inv_data = {
            "Item": item,
            "Location": location,
        }

        if function == "Add":
            userdb.insert_ml_inv_emg_data(email, inv_data, add=True, inv=True)
        elif function == "Remove":
            userdb.insert_ml_inv_emg_data(email, inv_data, remove=True, inv=True)

        return response.JsonResponse(
            {"success_status": True},
            status=status.HTTP_200_OK,
        )

    except DataRemovalError as dre:
        return response.JsonResponse(
            {"error": str(dre)},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
    except DataInsertionError as die:
        return response.JsonResponse(
            {"error": str(die)},
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


def send_inv_data(request, **kwargs) -> response.JsonResponse:
    try:
        print("GET REQUEST INVENTORY")
        print("request.data:", request.data)

        email = request.data.get("Email")

        userdb.get_ml_inv_emg_data(email, inv=True)

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


def recv_emg_contact(request, **kwargs) -> response.JsonResponse:
    """
    Func Desc
    """
    try:
        print("POST REQUEST EMERGENCY DATA")
        print("request.data:", request.data)

        email = request.data.get("Email")
        contact_name = request.data.get("Name")
        contact_num = request.data.get("Number")
        relation = request.data.get("Relation")
        function = request.data.get("Function")

        em_data = {
            "Name": contact_name,
            "Number": contact_num,
            "Relation": relation,
        }

        if function == "Add":
            userdb.insert_ml_inv_emg_data(email, em_data, add=True, emg=True)
        elif function == "Remove":
            userdb.insert_ml_inv_emg_data(email, em_data, remove=True, emg=True)

        return response.JsonResponse(
            {"success_status": True},
            status=status.HTTP_200_OK,
        )

    except DataRemovalError as dre:
        return response.JsonResponse(
            {"error": str(dre)},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
    except DataInsertionError as die:
        return response.JsonResponse(
            {"error": str(die)},
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


def send_emg_contact(request, **kwargs) -> response.JsonResponse:
    """
    Func Desc
    """
    try:
        print("GET REQUEST EMERGENCY DATA")
        print("request.data:", request.data)

        email = request.data.get("Email")

        userdb.get_ml_inv_emg_data(email, emg=True)

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
        print("POST REQUEST MEDIA DATA")
        print("request.data:", request.data)

        email = request.data.get("Email")
        filename = request.data.get("Filename")
        fileobj = request.data.get("File")
        desc = request.data.get("Description")
        function = request.data.get("Function")

        print(email, filename, fileobj, desc)

        date = d.datetime.now()
        date = date.strftime("%d/%m/%Y, %H:%M:%S")
        filename = filename.lower()
        subfolder = email.split("@")[0]
        cloudFilename = AWS_BUCKET_FOLDER + subfolder + "/" + filename
        objectURL = AWS_OBJECT_URL_PREFIX + cloudFilename

        data = {
            "Date": date,
            "Filename": filename,
            "CloudFilename": cloudFilename,
            "ObjectURL": objectURL,
        }

        if function == "Add":
            userdb.insert_media(email, data, add=True)
        elif function == "Remove":
            userdb.insert_media(email, data, remove=True)

        s3.upload_file_to_s3(cloudFilename, fileobj)

        return response.JsonResponse(
            {"success_status": True},
            status=status.HTTP_200_OK,
        )

    except DataRemovalError as dre:
        return response.JsonResponse(
            {"error": str(dre)},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
        )
    except DataInsertionError as die:
        return response.JsonResponse(
            {"error": str(die)},
            status=status.HTTP_503_SERVICE_UNAVAILABLE,
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


def send_media(request, **kwargs) -> response.JsonResponse:
    """
    Func Desc
    """
    try:
        print("GET REQUEST MEDIA DATA")
        print("request.data:", request.data)

        email = request.data.get("Email")

        userdb.get_media(email)

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
