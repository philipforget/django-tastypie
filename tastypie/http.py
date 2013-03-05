"""
The various HTTP responses for use in returning proper HTTP codes.
"""
from django.http import HttpResponse


class HttpResponseWithLocationHeader(HttpResponse):
    def __init__(self, *args, **kwargs):
        try:
            location = kwargs.pop('location', '')
        except KeyError:
            location = None

        super(HttpResponseWithLocationHeader, self).__init__(*args, **kwargs)
        if location is not None:
            self['Location'] = location


class HttpCreated(HttpResponseWithLocationHeader):
    status_code = 201


class HttpAccepted(HttpResponseWithLocationHeader):
    status_code = 202


class HttpNoContent(HttpResponse):
    status_code = 204


class HttpMultipleChoices(HttpResponse):
    status_code = 300


class HttpSeeOther(HttpResponse):
    status_code = 303


class HttpNotModified(HttpResponse):
    status_code = 304


class HttpBadRequest(HttpResponse):
    status_code = 400


class HttpUnauthorized(HttpResponse):
    status_code = 401


class HttpForbidden(HttpResponse):
    status_code = 403


class HttpNotFound(HttpResponse):
    status_code = 404


class HttpMethodNotAllowed(HttpResponse):
    status_code = 405


class HttpConflict(HttpResponse):
    status_code = 409


class HttpGone(HttpResponse):
    status_code = 410


class HttpTooManyRequests(HttpResponse):
    status_code = 429


class HttpApplicationError(HttpResponse):
    status_code = 500


class HttpNotImplemented(HttpResponse):
    status_code = 501

