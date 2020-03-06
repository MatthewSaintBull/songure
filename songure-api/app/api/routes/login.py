from fastapi import APIRouter, HTTPException, Request
from app.models.user import User
from app.db.mongo import DB
from starlette.responses import RedirectResponse
from app.config.config import config

import requests
from oauthlib.oauth2 import WebApplicationClient

import uuid

import json

db = DB()
router = APIRouter()
GOOGLE_CLIENT_ID = config["dev"]["google_client_id"]
GOOGLE_CLIENT_SECRET = config["dev"]["google_secret_id"]
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)
client = WebApplicationClient(GOOGLE_CLIENT_ID)


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


@router.get('/login')
def login():

    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    print("AUTH END", authorization_endpoint)

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri="http://localhost:8080/auth",
        scope=["openid", "email", "profile"],
    )
    return RedirectResponse(request_uri)


def gen_rand_user(fullname, email):
    username = email.split("@")[0] + str(uuid.uuid4())[:8]
    result = db.search_user_by_username(username)
    if not result:
        return username
    gen_rand_user(fullname, email)


@router.get('/auth')
def auth(code: str, request: Request):
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(
        token_url=token_endpoint,
        authorization_response=str(request.url),
        redirect_url="http://localhost:8080/auth",
        code=code,
    )

    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )
    print("TOKEN ? : ", token_response.json())
    client.parse_request_body_response(json.dumps(token_response.json()))
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    print(userinfo_response.json())
    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        email = userinfo_response.json()["email"]
        fullname = userinfo_response.json()["name"]

        db.register({"email": email, "full_name": fullname, "username": gen_rand_user(
            fullname, email), "Oauth": "google"})

        # db.login()

    else:
        return "User email not available or not verified by Google.", 400

    return RedirectResponse("http://localhost:8080/set_user")