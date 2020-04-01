import os

from ctypes import CDLL, c_void_p, c_char_p, c_double, c_int, c_longlong, CFUNCTYPE
import pyforex

def signature_telegram_library(tdjson: CDLL) -> CDLL:
    """
    From a loaded library define all signature methods from C to Python
    """
    tdjson.td_json_client_create.restype = c_void_p
    tdjson.td_json_client_create.argtypes = []

    tdjson.td_json_client_receive.restype = c_char_p
    tdjson.td_json_client_receive.argtypes = [c_void_p, c_double]

    tdjson.td_json_client_send.restype = None
    tdjson.td_json_client_send.argtypes = [c_void_p, c_char_p]

    tdjson.td_json_client_execute.restype = c_char_p
    tdjson.td_json_client_execute.argtypes = [c_void_p, c_char_p]

    tdjson.td_json_client_destroy.restype = None
    tdjson.td_json_client_destroy.argtypes = [c_void_p]

    tdjson.td_set_log_file_path.restype = c_int
    tdjson.td_set_log_file_path.argtypes = [c_char_p]

    tdjson.td_set_log_max_file_size.restype = None
    tdjson.td_set_log_max_file_size.argtypes = [c_longlong]

    tdjson.td_set_log_verbosity_level.restype = None
    tdjson.td_set_log_verbosity_level.argtypes = [c_int]

    fatal_error_callback_type = CFUNCTYPE(None, c_char_p)

    tdjson.td_set_log_fatal_error_callback.restype = None
    tdjson.td_set_log_fatal_error_callback.argtypes = [fatal_error_callback_type]
    return tdjson
