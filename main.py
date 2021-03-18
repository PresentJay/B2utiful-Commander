from lib_module.cli_inquirer import *


def main():

    main_Qchain = [
        create_listQ("main_menu", "select main menu", MAIN_Q),
        create_confQ(
            "login_confirm", "login!", when={"QID": "main_menu", "choice": "login"}
        ),
        create_confQ(
            "exit_confirm",
            "Do you want to exit from FHIR Client?",
            when={"QID": "main_menu", "choice": "exit"},
        ),
    ]

    while True:
        # clear terminal code
        print(u"{}[2J{}[;H".format(chr(27), chr(27)), end="")

        log("FHIR API CLI", color="blue", figlet=True)
        log("\t\tFHIR client by python", color="green")

        client = execute(main_Qchain)


if __name__ == "__main__":
    main()