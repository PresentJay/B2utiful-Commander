from lib_module.cli_inquirer import *


def main():

    main_Qchain = [
        create_listQ(
            questionID="main_menu", message="select main menu", choicelist=MAIN_Q
        ),
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
