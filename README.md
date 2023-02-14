# My Personal Bot

A personal bot enriching GPT chatbot by using GPT3 API to get answers about your own content

## Features
- The bot can scan a pre-configured data source (currently a folder on your PC), and learn the content
- The bot will automatically learn each file that is added to the folder 
- The bot can then answer question about the content
- Supported files:
  - 📜 Text (txt, md)
  - 📄 Documents (pdf, doc, docx)
  - 🎬 Movies transcript (mp4, wmv, avi) 
  - 🔉 Sound (wav, mp3)
  - 🔗 Public web pages text (web, url, webloc)

## Installation
1. Clone the repository: `git clone https://github.com/akiriati/PersonalGPT.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Generate a token at `https://platform.openai.com/account/api-keys` (It's free! 💸)
4. Configure the bot by creating a `config-secrets.yaml` and put `OPENAI_KEY: <YOUR_KEY_HERE>`
5. Run the bot: `python chatbot.py bot`

## Getting started 
1. run `python chatbot.py teach --path "<PATH_TO_A_FOLDER_WITH_CONTENT>"`. This might a few seconds for each doc, and ~1 minute for every 30 minutes of sound/video 
2. run `python chatbot.py bot`

## Usage
- Use the bot and communicate about your content by running `python chatbot.py bot`
- Ask the bot single a question by running `python chatbot.py query --text "<YOUR_QUESTION_HERE>`
- Teach the bot the content of a folder / single file by running `python chatbot.py teach --path "<YOUR_PATH_HERE>`

## Autmoate folder
- You can also autmoate a folder to teach the bot the content of a new file when it is added to the folder. In Mac this can be done by using the Automator.app -> Folder Action -> Run Shell Script -> 
```
python3 </YOUR/PATH/TO/FOLDER>/chatbot.py teach --path "$1"
```

<img width="885" alt="Screenshot 2023-02-14 at 23 06 33" src="https://user-images.githubusercontent.com/10947653/218863170-cd6d2049-ac6c-438a-b394-32e4d29c585a.png">




## Contact
If you have any questions or feedback, please contact me at akiriati@hotmail.com
