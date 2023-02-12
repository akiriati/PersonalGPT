import argparse
import os
import sys

from constants import init_constants_from_config
from db import init_db
from folder_scan import extract_text_from_path
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
            segments = extract_text_from_path(os.path.expanduser(args.path))
            print (segments)
            exit()
            print ("I'm always happy to learn new things :)")
            print("I'm sure there are a lot of interesting things I can learn in " + args.path)
            teach(segments)

        else:
            print("Error: the 'teach' command requires a '--path' argument")
    elif args.command == "query":
        if args.text:
            print(query(args.text)["choices"][0]["text"])
        else:
            print("Error: the 'query' command requires a '--query' argument")
    elif args.command == "bot":
        print("Hi, I'm you're personal chatbot. Ask me anything. Say 'bye' to quit")
        history = ""
        while True:
            message = input("You: ")
            collected_events = []
            completion_text = ''
            streaming_response = query(message, stream=True, history=history)
            print("Chatbot:", end="")
            for event in streaming_response:
                collected_events.append(event)  # save the event response
                event_text = event['choices'][0]['text']  # extract the text
                sys.stdout.write(event_text)
                sys.stdout.flush()
                completion_text += event_text  # append the text
            print("")
            history += completion_text + "."
            if message.lower() in ["bye", "goodbye", "exit", "quit"]:
                break
    else:
        print ("Command not supported. Please use --teach, --query or --bot")