import argparse
from constants import init_constants_from_config
from db import init_db
from folder_scan import scan_all_files_in_path
from query import query
from teach import teach

if __name__ == "__main__":

    init_constants_from_config()
    init_db()

    parser = argparse.ArgumentParser()
    parser.add_argument("command", type=str, help="The command to run: 'teach' or 'query'")
    parser.add_argument("--text", type=str, help="The text to pass to the 'query' command")
    parser.add_argument("--path", type=str, help="The path to pass to the 'teach' command")
    args = parser.parse_args()

    if args.command == "teach":
        if args.path:
            segments = scan_all_files_in_path(args.path)
            print ("I'm always happy to learn new things :)")
            print("I'm sure there are a lot of interesting things I can learn in " + args.path)
            teach(segments)

        else:
            print("Error: the 'teach' command requires a '--path' argument")
    elif args.command == "query":
        if args.text:
            print(query(args.text, ""))
        else:
            print("Error: the 'query' command requires a '--query' argument")
    elif args.command == "bot":
        print("Hi, I'm you're personal chatbot. Ask me anything. Say 'bye' to quit")
        history = ""
        while True:
            message = input("You: ")
            chatbot_response = "Chatbot: " + query(message, history)
            print(chatbot_response)
            history += message + "."
            if message.lower() in ["bye", "goodbye", "exit", "quit"]:
                break
    else:
        print ("Command not supported. Please use --teach, --query or --bot")