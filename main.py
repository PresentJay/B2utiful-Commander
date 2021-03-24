from lib_module.cli_inquirer import *
import json


def main():
    with open("./lib_module/Qchain.json") as file:
        data = json.load(file)
        
    rest = RESTful()
    Qchain = []

    make_chain(Qchain, data, data)
    
    # event loop
    while True:
        clear_Terminal()
        main_logo(title="FHIR API CLI", msg="FHIR client by python", auth="PresentJay")

        if rest.url:
            log(
                coloredList=getColoredTexts(
                    [
                        {"string": "\ttarget url : ", "color": "white"},
                        {"string": rest.url, "color": "yellow"},
                    ]
                )
            )
        log("\t")

        client = execute(Qchain)

        if EXIT_COND in client.keys() and client[EXIT_COND]:
            break


if __name__ == "__main__":
    if DEBUG:
        main()
    else:
        try:
            main()
        except BaseException:
            print("trouble aborted")
            