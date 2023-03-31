import logging
import requests
from requests.exceptions import JSONDecodeError, ConnectionError

from .response import Response
from .exceptions import APIClientError


def _process_response(response) -> Response:
    try:
        return Response(
            status_code=response.status_code,
            text=response.text,
            json=response.json(),
        )
    except JSONDecodeError:
        return Response(
            status_code=response.status_code,
            text=response.text,
        )


def get(url: str, headers: {} = None) -> Response:
    try:
        response = requests.get(url=url, headers=headers)
    except ConnectionError as ex:
        logging.error(f"API Client Error: {str(ex)}")
        raise APIClientError(
            description=str(ex),
            detail=ex,
        )
    return _process_response(response)


def post(url: str, payload: dict = None, headers: dict = None) -> Response:
    try:
        response = requests.post(url=url, headers=headers, data=payload)
    except ConnectionError as ex:
        logging.error(f"API Client Error: {str(ex)}")
        raise APIClientError(
            description=str(ex),
            detail=ex,
        )
    return _process_response(response)


def put(url: str, payload: dict = None, headers: dict = None) -> Response:
    try:
        response = requests.put(url=url, headers=headers, data=payload)
    except ConnectionError as ex:
        logging.error(f"API Client Error: {str(ex)}")
        raise APIClientError(
            description=str(ex),
            detail=ex,
        )
    return _process_response(response)


def delete(url: str, payload: dict = None, headers: dict = None) -> Response:
    try:
        response = requests.delete(url=url, headers=headers, data=payload)
    except ConnectionError as ex:
        logging.error(f"API Client Error: {str(ex)}")
        raise APIClientError(
            description=str(ex),
            detail=ex,
        )
    return _process_response(response)
