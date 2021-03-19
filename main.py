from lib_module.cli_inquirer import *
import json


def main():

    with open("./lib_module/Qchain.json") as file:
        data = json.load(file)

    rest = RESTful()
    Qchain = []
    
    for ctx in data:
        qid = ctx.get("name")
        msg = ctx.get("message")
        chain = 
        
        if ctx.get("type") == "list":
            

    main_Qchain = [
        create_listQ(questionID="main_menu", message="select menu", choicelist=MAIN_Q),
        create_confQ(
            questionID="login_confirm",
            message="login!",
            when=lambda Q: Q["main_menu"] == "login",
        ),
        create_confQ(
            questionID="exit_confirm",
            message="Do you want to exit from FHIR Client?",
            when=lambda Q: Q["main_menu"] == "exit",
        ),
        create_confQ(
            questionID="test1",
            message="you choose test1 menu",
            when=lambda Q: Q["main_menu"] == "test1",
        ),
        create_confQ(
            questionID="test2",
            message="you choose test2 menu",
            when=lambda Q: Q["main_menu"] == "test1" and Q["test1"],
        ),
    ]

    while True:
        # clear terminal code
        print(u"{}[2J{}[;H".format(chr(27), chr(27)), end="")

        log("FHIR API CLI", color="blue", figlet=True)
        log("\t\tFHIR client by python", color="green")
        log(
            coloredList=getColoredTexts(
                [
                    {"string": "\t\t\tpowered by ", "color": "white"},
                    {"string": "presentJay", "color": "cyan"},
                ]
            )
        )
        log("\t")
        if rest.url:
            log(
                coloredList=getColoredTexts(
                    [
                        {"string": "\ttarget url : ", "color": "white"},
                        {"string": rest.url, "color": "yellow"},
                    ]
                )
            )

        client = execute(main_Qchain)

        if client["exit_confirm"]:
            break


if __name__ == "__main__":
    if DEBUG:
        main()
    else:
        try:
            main()
        except BaseException:
            print("trouble aborted")
