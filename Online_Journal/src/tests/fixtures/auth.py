from rest_framework.test import APIClient

api_client = APIClient()


def auth_client(user):
    client = APIClient(headers={"Authorization": f"Token {user['token']}"})

    return {"client": client, "user": user["user"]}

