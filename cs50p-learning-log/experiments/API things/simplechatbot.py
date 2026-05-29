# first made chatbot.py, but renamed to simplechatbot.py to avoid confusion with the chatbot package.
# was introduced to api and libraries like cowsay and ollama.
# the script starts an ollama server, then enters a loop where it takes user input, sends it to the ollama model,
# and displays the response in a cowsay text bubble. the conversation continues until the user types 'exit' or 'quit'.

from sys import exit
import subprocess
import time
import cowsay
import ollama


def start_ollama():
    subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(3)


def main():
    start_ollama()

    print("==================================================")
    cowsay.cow("Moo! I am an AI-powered CowBot. Ask me anything!")
    print("Type 'exit' or 'quit' to end our conversation.")
    print("==================================================")

    messages = [
        {
            "role": "system",
            "content": "You are a helpful, witty AI assistant. Keep your responses very short (under 2 sentences) so they fit nicely inside a cowsay text bubble.",
        }
    ]

    while True:
        try:
            user_input = input("\nYou: ").strip()

            if not user_input:
                continue

            if user_input.lower() in ["exit", "quit"]:
                print("\nGoodbye!")
                exit(0)

            messages.append({"role": "user", "content": user_input})

            print("\nCowBot is thinking...")

            response = ollama.chat(model="tinyllama", messages=messages)

            bot_reply = response["message"]["content"]

            messages.append({"role": "assistant", "content": bot_reply})

            cowsay.cow(bot_reply)

        except KeyboardInterrupt:
            print("\n\n[Session closed] Goodbye!")
            exit(0)


if __name__ == "__main__":
    main()


