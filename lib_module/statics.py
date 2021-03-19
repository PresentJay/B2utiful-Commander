class RESTful:
    def __init__(self):
        self.http = "http://"
        self.https = "https://"
        self.get = "get"
        self.post = "post"
        self.patch = "patch"
        self.delete = "delete"

        self.LocalHost = "localhost"
        self.Referer = "Referer"

    def set_Url(self, url):
        self.url = url


# set Debug mode in entire project
DEBUG = True

# set basic font in decorator
BASE_LOG_FONT = "slant"

# set the Chain-Question List
GET_SESSION = "GetSession"
SET_URL = "setURL"
RUN_HTTPMETHOD = "RunHTTPmethod"
EXIT = "exit"
MAIN_Q = [GET_SESSION, SET_URL, RUN_HTTPMETHOD, EXIT]

# Common statics
PAGEID = "pageid"
UID = "uid"
CATEGORY = "category"

PRETTY = "pretty"
SUMMARY = "_summary"


""" directory managing settings """
IGNORE_FILES = [
    ".vscode",
    "venv",
    ".gitignore",
    "readme.md",
    ".git",
    "__pycache__",
    "LICENSE",
    "lib_module",
    "main.py",
    "requirements.txt",
]
