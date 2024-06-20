r"""
                                                             
 _______  _______         _______  _______  _______  _______  _______  _______  _______ 
(  ___  )(  ____ \       (  ____ \(  ____ \(  ____ )(  ___  )(  ____ )(  ____ \(  ____ )
| (   ) || (    \/       | (    \/| (    \/| (    )|| (   ) || (    )|| (    \/| (    )|
| |   | || (__     _____ | (_____ | |      | (____)|| (___) || (____)|| (__    | (____)|
| |   | ||  __)   (_____)(_____  )| |      |     __)|  ___  ||  _____)|  __)   |     __)
| |   | || (                   ) || |      | (\ (   | (   ) || (      | (      | (\ (   
| (___) || )             /\____) || (____/\| ) \ \__| )   ( || )      | (____/\| ) \ \__
(_______)|/              \_______)(_______/|/   \__/|/     \||/       (_______/|/   \__/
                                                                                      
"""

import hashlib
import json
import logging
import time
from urllib.parse import urlparse

import ofscraper.classes.sessionmanager.sessionmanager as sessionManager
import ofscraper.utils.auth.file as auth_file
import ofscraper.utils.constants as constants
import ofscraper.utils.settings as settings
import ofscraper.utils.cache as cache



def read_request_auth(refresh=True,forced=False):
    request_auth = {
        "static_param": "",
        "format": "",
        "checksum_indexes": [],
        "checksum_constant": 0,
    }

    # *values, = get_request_auth()
    result = get_request_auth(refresh=refresh,forced=forced)
    if not result:
        raise json.JSONDecodeError("No content")
    (*values,) = result

    request_auth.update(zip(request_auth.keys(), values))
    return request_auth


def get_request_auth(refresh=False,forced=False):
    #curr_auth = cache.get("api_onlyfans_sign")
    # if not (refresh or forced) and curr_auth:
    #     return curr_auth
    dynamic=settings.get_dynamic_rules()
    auth=None

    if constants.getattr("DYNAMIC_RULE") and dynamic in {"manual"}:
        auth=get_request_auth_dynamic_rule_manual()
    elif constants.getattr("DYNAMIC_GENERIC_URL") and dynamic in {"generic"}:
        auth=get_request_auth_generic()


    elif (dynamic) in {
        "datawhores"
    }:
        auth = get_request_auth_datawhores()
    elif (dynamic) in {
        "xagler"
    }:
        auth = get_request_auth_xagler()
    elif (dynamic) in {
        "rafa"
    }:
        auth = get_request_auth_rafa()
    
    elif not constants.getattr("ALLOW_OTHER_DYNAMIC_RULES"):
        pass
    elif (dynamic) in {
        "riley"
    }:
        auth = get_request_auth_riley()
    elif (dynamic) in {
        "deviint",
        "dv",
        "dev",
    }:

        auth = get_request_auth_deviint()
    elif (dynamic) in {
        "dc","digital","digitalcriminal","digitalcriminals"
    }:
        auth = get_request_auth_digitalcriminals()
    if auth==None:
        auth = get_request_auth_datawhores()
    cache.set(
        "api_onlyfans_sign",
        auth,
    )
    time.sleep(10)
    return auth

def get_request_auth_dynamic_rule_manual():
    content = constants.getattr("DYNAMIC_RULE")
    return request_auth_helper(content)

def get_request_auth_generic():
    logging.getLogger("shared").debug(f"getting new signature with generic")
    with sessionManager.sessionManager(
        backend="httpx",
        retries=constants.getattr("GIT_NUM_TRIES"),
        wait_min=constants.getattr("GIT_MIN_WAIT"),
        wait_max=constants.getattr("GIT_MAX_WAIT"),
        refresh=False,
    ) as c:
        
        with c.requests(
            constants.getattr("DYNAMIC_GENERIC_URL"),
        ) as r:
            content = r.json_()
            return request_auth_helper(content)

def get_request_auth_deviint():
    logging.getLogger("shared").debug(f"getting new signature with deviint")

    with sessionManager.sessionManager(
        backend="httpx",
        retries=constants.getattr("GIT_NUM_TRIES"),
        wait_min=constants.getattr("GIT_MIN_WAIT"),
        wait_max=constants.getattr("GIT_MAX_WAIT"),
        refresh=False,
    ) as c:
        
        with c.requests(
            constants.getattr("DEVIINT"),
        ) as r:
            content = r.json_()
            return request_auth_helper(content)


def get_request_auth_datawhores():
    logging.getLogger("shared").debug(f"getting new signature with datawhores")

    with sessionManager.sessionManager(
        backend="httpx",
        retries=constants.getattr("GIT_NUM_TRIES"),
        wait_min=constants.getattr("GIT_MIN_WAIT"),
        wait_max=constants.getattr("GIT_MAX_WAIT"),
        refresh=False,
    ) as c:
        
        with c.requests(
            constants.getattr("DATAWHORES_URL"),
        ) as r:
            content = r.json_()
            return request_auth_helper(content)


def get_request_auth_xagler():
    logging.getLogger("shared").debug(f"getting new signature with xagler")

    with sessionManager.sessionManager(
        backend="httpx",
        retries=constants.getattr("GIT_NUM_TRIES"),
        wait_min=constants.getattr("GIT_MIN_WAIT"),
        wait_max=constants.getattr("GIT_MAX_WAIT"),
        refresh=False,
    ) as c:
        
        with c.requests(
            constants.getattr("XAGLER_URL"),
        ) as r:
            content = r.json_()
            return request_auth_helper_alt_format(content)
def get_request_auth_rafa():
    logging.getLogger("shared").debug(f"getting new signature with rafa")

    with sessionManager.sessionManager(
        backend="httpx",
        retries=constants.getattr("GIT_NUM_TRIES"),
        wait_min=constants.getattr("GIT_MIN_WAIT"),
        wait_max=constants.getattr("GIT_MAX_WAIT"),
        refresh=False,
    ) as c:
        
        with c.requests(
            constants.getattr("RAFA_URL"),
        ) as r:
            content = r.json_()
            return request_auth_helper(content)

def get_request_auth_riley():
    logging.getLogger("shared").debug(f"getting new signature with riley")

    with sessionManager.sessionManager(
        backend="httpx",
        retries=constants.getattr("GIT_NUM_TRIES"),
        wait_min=constants.getattr("GIT_MIN_WAIT"),
        wait_max=constants.getattr("GIT_MAX_WAIT"),
        refresh=False,
    ) as c:
        
        with c.requests(
            constants.getattr("RILEY_URL"),
        ) as r:
            content = r.json_()
            return request_auth_helper(content)  
def get_request_auth_digitalcriminals():
    logging.getLogger("shared").debug(f"getting new signature with digitalcriminals")

    with sessionManager.sessionManager(
        backend="httpx",
        retries=constants.getattr("GIT_NUM_TRIES"),
        wait_min=constants.getattr("GIT_MIN_WAIT"),
        wait_max=constants.getattr("GIT_MAX_WAIT"),
        refresh=False,
    ) as c:
        with c.requests(
            constants.getattr("DIGITALCRIMINALS"),
        ) as r:
            content = r.json_()
            return request_auth_helper_alt_format(content)


def request_auth_helper_alt_format(content):
    static_param = content["static_param"]
    fmt = content["format"]
    checksum_indexes = content["checksum_indexes"]
    checksum_constant = content["checksum_constant"]
    return (static_param, fmt, checksum_indexes, checksum_constant)      

def request_auth_helper(content):
    static_param = content["static_param"]
    fmt = f"{content['prefix']}:{{}}:{{:x}}:{content['suffix']}"
    checksum_indexes = content["checksum_indexes"]
    checksum_constant = content["checksum_constant"]
    return (static_param, fmt, checksum_indexes, checksum_constant)





def make_headers():
    auth = auth_file.read_auth()
    headers = {
        "accept": "application/json, text/plain, */*",
        "app-token": constants.getattr("APP_TOKEN"),
        "user-id": auth["auth_id"],
        "x-bc": auth["x-bc"],
        "referer": "https://onlyfans.com",
        "user-agent": auth["user_agent"],
    }
    return headers


def add_cookies():
    auth = auth_file.read_auth()
    cookies = {}
    cookies.update({"sess": auth["sess"]})
    cookies.update({"auth_id": auth["auth_id"]})
    cookies.update({"auth_uid_": auth["auth_uid"] or auth["auth_id"]})
    return cookies


def get_cookies():
    auth = auth_file.read_auth()
    return f"auth_id={auth['auth_id']};sess={auth['sess']};"


def create_sign(link, headers, refresh=False,forced=False):
    """
    credit: DC and hippothon
    """
    content = read_request_auth(refresh=refresh,forced=forced)

    time2 = str(round(time.time() * 1000))

    path = urlparse(link).path
    query = urlparse(link).query
    path = path if not query else f"{path}?{query}"

    static_param = content["static_param"]

    a = [static_param, time2, path, headers["user-id"]]
    msg = "\n".join(a)

    message = msg.encode("utf-8")
    hash_object = hashlib.sha1(message, usedforsecurity=False)
    sha_1_sign = hash_object.hexdigest()
    sha_1_b = sha_1_sign.encode("ascii")

    checksum_indexes = content["checksum_indexes"]
    checksum_constant = content["checksum_constant"]
    checksum = sum(sha_1_b[i] for i in checksum_indexes) + checksum_constant

    final_sign = content["format"].format(sha_1_sign, abs(checksum))

    headers.update({"sign": final_sign, "time": time2})
    return headers
