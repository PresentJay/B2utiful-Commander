class RESTful:
    def __init__(self):
        self.http = "http://"
        self.https = "https://"
        self.get = "get"
        self.post = "post"
        self.patch = "patch"
        self.delete = "delete"

        self.localhost = "localhost"
        self.referer = "Referer"
        self.url = False

    def set_Url(self, url, port=None):
        self.url = url
        if port:
            url = url + str(port) + "/"


# set Debug mode in entire project
DEBUG = True

# set basic font in decorator
BASE_LOG_FONT = "slant"

# set the Chain-Question List
GET_SESSION = "GetSession"
SET_URL = "setURL"
RUN_HTTPMETHOD = "RunHTTPmethod"
EXIT = "exit"
EXIT_COND = "exit_confirm"
MAIN_Q = [GET_SESSION, SET_URL, RUN_HTTPMETHOD, EXIT]


# cli_inquirer statics
TYPE = "type"
NAME = "name"
QMARK = "qmark"
MESSAGE = "message"
CHOICES = "choices"
WHEN = "when"

LIST = "list"
CHECKBOX = "checkbox"
CONFIRM = "confirm"
INPUT = "input"

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
