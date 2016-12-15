"""This modulet tests the client and server modules for the CF 401 Python HTTP-Server assignment."""

import pytest

# Test the following:
# messages shorter than one buffer in length
# messages longer than several buffers in length
# messages that are an exact multiple of one buffer in length
# messages containing non-ascii characters

# def test_client_short():
#     """Test with message shorter than one buffer length."""
#     from client import client
#     test_msg = "twerp"
#     return client(test_msg) == u"twerp"

# def test_client_long():
#     """Test with message longer than several buffers in length."""
#     from client import client
#     test_msg = "This is a very long test message."
#     return client(test_msg) == test_msg

# def test_client_exact_buffer():
#     """Test messages that are an exact multiple of one buffer in length."""
#     from client import client
#     test_msg = "abcdefghij"
#     return client(test_msg) == test_msg


# def test_client_non_ASCII():
#     """Test messages that contain non ASCII characters."""
#     from client import client

"""BEGIN TESTS FOR STEP1 ASSIGNMENT"""

# GET /index.html HTTP/1.1<CRLF>
# Host: www.example.com<CRLF>
# <CRLF>

GOOD_REQ = u"GET /index.html HTTP/1.1\\r\\nHost: www.example.com\\r\\n\\r\\n"
BAD_REQs = [
    b"GOT /index.html HTTP/1.1\\r\\nHost: www.example.com\\r\\n\\r\\n",
    b"GET /index.html HTTP/0.1\\r\\nHost: www.example.com\\r\\n\\r\\n",
    b"GET index.html HTTP/0.1\\r\\nHost: www.example.com\\r\\n\\r\\n",
]


def test_test_request_good_req():
    """Test test_request() with a properly formatted HTTP message."""
    from server import parse_request
    assert parse_request(GOOD_REQ.encode('utf-8')) == b"/index.html"


@pytest.mark.parametrize("req", BAD_REQs)
def test_test_request_bad_req(req):
    """Test test_requrest() witih an improperly formatted HTTP message."""
    from server import parse_request
    assert parse_request(req) is None


def test_response_ok():
    """Test ok response."""
    from client import client
    assert b'200' == client(GOOD_REQ)[9:12]


@pytest.mark.parametrize("req", BAD_REQs)
def test_response_err(req):
    """Test response err."""
    from client import client
    assert b'500' == client(req)[9:12]
