# OpenAI API

### About this project
This API was originally built 11/2023 for a Machine Learning and Artificial Intelligence in Business Strategy course. The prompt was to come up with an idea for an artificial intelligence-driven refresh of the course. My idea centered around using artificial intelligence to hyperpersonalize content and teaching techniques, to power interactive and adaptive case studies, and to mediate many small-group debates at once. This API is the "Proof of Concept" portion of my project. 

### Technologies 
This project is coded in Python. Libraries used include: 🤖openai | 🎨streamlit 

### How to run
This project relies on the utilization of an OpenAI key. Once you possess one, utilize the Environmental Variables feature in your Control Panel (on PC) to create an environmental variable with the variable OPENAI_API_KEY and the value of your key. Additionally, the folder structure is important to run this project on your local host. The main page must be called via command prompt (author used Anaconda Prompt); additional pages must be placed in a "pages" folder. These additional pages will then appear in the app as module pages. Lastly, note the requirements.txt file in this project; this file was added to deploy the app. It is not needed to run the app on local host.

### Future features
The next step in the development of this code is to add in the ability for the bot to "remember" a dialogue. This can be accomplished by adding a list to which dictionaries (for both user input and bot responses) can be appended; the bot can then be instructed to look at this list in addition to new user input.

### Deployed app
The deployed app URL is: https://ai-business-strategy.streamlit.app/ . Note that this deployment is for observational purposes only; as environmental variables are stored on local host, the deployment cannot read your personal OpenAI API key. See section "How to run" to run the app on your local host.
