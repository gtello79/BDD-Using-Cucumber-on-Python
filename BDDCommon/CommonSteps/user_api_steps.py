from behave import step
from BDDCommon.CommonHelpers.UtilitiesHelpers import generate_random_user_and_password
from BDDCommon.CommonAPI.users_api import CustomerAPI
from BDDCommon.CommonDAO.customerDAO import CustomerDAO


@step("I generate random email and password")
def generate_random_email_and_password(context):
    random_info = generate_random_user_and_password()

    context.user_info = random_info


@step("I call 'create customer' API")
def make_api_call(context):
    try:
        user_info: dict = context.user_info
    except AttributeError as e:
        print(e.with_traceback())

    # Verificacion de email y contraseña
    assert "password" in list(
        user_info.keys()
    ), "Se necesita incluir por defecto la llave password"
    assert "email" in list(
        user_info.keys()
    ), "Se necesita incluir por defecto la llave email"

    # Crea el usuario
    rs_user_response = CustomerAPI().create_user(data=user_info)

    assert rs_user_response, (
        "Empty response for create user. " f"Payload {rs_user_response}"
    )

    user_email = rs_user_response["email"]

    assert user_email == user_info["email"], (
        "Wrong email in response of 'create user' api. "
        f"Payload {rs_user_response}"
        f"Call email {user_info['email']} response email {user_email}"
    )

    user_username = user_info["email"].split("@")[0]
    assert user_username == rs_user_response["username"], (
        "Wrong username in response of 'create user' api. "
        f"Payload {rs_user_response}"
        f"Call username {user_username} response username {rs_user_response['username']}"
    )


@step("Customer should be created")
def validate_customer_creation(context):
    # Get user info
    user_email = context.user_info["email"]

    rs_bd = CustomerDAO().get_user_by_email(email=user_email)

    assert len(rs_bd) == 1, (
        "Se han pasado más elementos de los esperados. "
        f"total respuesta BD: {len(rs_bd)}"
    )

    # obtiene al usuario
    user_data = rs_bd[0]
    rs_user_email = user_data["user_email"]

    assert user_email == rs_user_email, (
        "Wrong email in response of 'create user' BD. "
        f"Payload {user_data}"
        f"Call email {user_email} response email {rs_user_email}"
    )

    user_username = user_email.split("@")[0]
    assert user_username == user_data["user_login"], (
        "Wrong username in response of 'create user' api. "
        f"Payload {user_data}"
        f"Call username {user_username} response username {user_data['user_login']}"
    )