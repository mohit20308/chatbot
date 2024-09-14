# ChatBOT 

## **Installing Dependencies**

The modules are added in requirements.txt. To install run,

	pip install -r requirements.txt

## Rule Based ChatBOT 

- It operates on set of predefined rules.
- It follows a decision tree or set of if-then statements to provide response.

**1_Rule_Based_ChatBot.ipynb** 
This is a Career Advisory System (Cairo). It assist the user in making decisions about the career.

The following images shows the Career options suggested by Cairo based on user input:

**(i)** BOT suggests Product based companies

<kbd>![](/README_images/1_image_job_p_p.PNG)</kbd>

**(ii)** BOT suggests exams for Government job

<kbd>![](/README_images/2_image_job_govt.PNG)</kbd>

**(iii)** BOT suggests tech giants for Game Devoper position

<kbd>![](/README_images/3_image_job_p_service.PNG)</kbd>

**(iv)** BOT suggests entrance exam for MBA

<kbd>![](/README_images/4_image_higher.PNG)</kbd>



## AI-Powered ChatBOT

- These use NLP and machine learning models to understand the context.
- These are capable of handling more complex conversations.

**2_ChatBot_Finetuned.ipynb** 
Here, a microsoft DialoGPT-medium model from HuggingFace is used and it's fine tuned on custom dataset for context specific answers.

The following example shows the BOT response when it's not fine tuned on custom dataset

<kbd>![](/README_images/q2_non_context.PNG)</kbd>

Now one can notice the change, here the fine tuned model is used for response for same question. It gives context-specific answers.

<kbd>![](/README_images/q2_context.PNG)</kbd>

## Web App

Streamlit is used to create UI.  
app.py file can be run as:  
   streamlit run app.py



