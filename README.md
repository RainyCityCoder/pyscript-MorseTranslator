# PyScript-based Morse Code / English Translator

## Description

The code behind the translator portion of this webpage was originally conceived as a [Command-Line-Interface program](https://github.com/RainyCityCoder/EarlyPyProj/tree/main/MorseTranslator) early in my coding learning journey. I felt the code would be more useful as a webpage, and after some research settled on a simple static webpage using [PyScript](https://pyscript.net/) to run the Python code.

## Forking

### Instructions:

After [forking](https://docs.github.com/en/get-started/quickstart/fork-a-repo) and [cloning](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) this repository, you may access a locally-hosted version of the site by running terminal command `python3 -m http.server --bind 127.0.0.1 9000` in the project's root directory (`~/pyscript-MorseTranslator`). Navigate in your browser to `127.0.0.1:9000` to access the page.

## User Interaction:

Near the top of the webpage there is a large text-entry box that allows entry of english letters (for English-to-Morse), or hyphens and periods (for Morse-to-English).

_Please Note: The input only accepts hyphens (`-`) as dashes, and periods (`.`) as dots at this time._

_Please Note: spaces, as well as Morse Code for numbers and punctuation are allowed._

1. Type or copy-paste the string of morse code or English you wish to convert to English into the aforementioned text-entry box.
   1. `...Letters-to-Morse` button will translate English characters into Morse Code.
   2. `...Morse-to-Letters` button will translate Morse Code into English characters.
2. The resulting translation will appear under the `Result ↴` test. 
   1. A `[space]` designator is used between words when translating from English to Morse. Including this in back-translating (Morse to English) is OK.
3. If you should need to delete the text in the text-entry box, you may use the `Clear Text` button found immediately underneath the text-entry box.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.
