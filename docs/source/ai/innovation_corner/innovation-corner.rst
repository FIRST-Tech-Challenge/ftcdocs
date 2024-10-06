AI Innovation Corner
====================

These articles are part of the *FIRST* Tech Challenge AI Innovation Corner.
This is a place where we'll post custom and curated articles relevant to
*FIRST* Tech Challenge as it relates to AI and its impact on our daily
lives and the world around us. We would like to thank Google for their 
generous contributions to *FIRST* Tech Challenge to increase access to 
our program in underserved communities and for providing
sponsorship and occasional technical direction for this content.

Articles are ordered on this page chronologically, with the newest content
at the top of the page expanded. Just click to expand any other articles
you'd like to see.

.. dropdown:: Week of 09/30/2024 "AI Competition Manual Assistant"
   :open:

   .. _competition_manual_assistant:

   **AI Competition Manual Assistant**

   In our first article, the Google AI Studio was introduced as a
   tool to interact with Google’s Gemini AI. Gemini is one of several flagship
   Large Language Models (LLM’s) that have been meticulously trained on massive
   amounts of text data to learn the patterns and relationships between units
   of language - these models have actually learned how to recognize text-based
   language, read and understand data, and synthesize what it learned to
   predict and interpret future data. This is the exact process humans make in
   learning and understanding the world around us! In Google AI Studio, users
   can interact with the Gemini AI through “prompts” to perform tasks for them.
   Prompts are instructions or queries given to an AI in order to generate a
   response - the quality of the response is often directly related to the
   quality of the prompt. Through these prompts, Gemini can provide responses
   based on the massive dataset that it has been pre-trained with, or users can
   also provide additional documents, text, or media that the AI has never seen
   before. These multimodal prompts, or prompts that include multiple types of
   content, can be very beneficial in interacting with an AI using content that
   is specific to a niche area like *FIRST* Tech Challenge. Can you think of ways
   to put this ability to good use in *FIRST* Tech Challenge?

   In *FIRST* Tech Challenge, one of the first tasks teams have to do is to read
   and understand the *FIRST* Tech Challenge Competition Manual. This can be a
   very painstaking task, and even a skilled reader can miss subtle nuances
   provided by the manual. However, an AI can break down and analyze the manual
   in a matter of seconds, usually preserving the nuance provided in the
   document. Users can then interact with the AI that has analyzed the
   Competition Manual, and prompt the AI to provide insights - these questions
   might involve locating specific information likely found in the Competition
   Manual, summarize important rules or processes, or even involve asking the
   AI to make a best guess. Through a process known as “role playing” the user
   can prompt the AI to take on a role or persona and direct the AI to follow
   specific rules as it interacts with the user in subsequent prompts. The
   remainder of this article is a tutorial on how to set up a “role playing”
   session with the Google Gemini AI through Google AI Studio to analyze and
   answer questions based on the *FIRST* Tech Challenge 2024-2025 Competition
   Manual for the INTO THE DEEP presented by RTX season. While some of the
   nuanced elements (like AI prompting) will be shallowly covered in this
   article, it is something we’ll cover a lot more in future articles.

   Creating an AI expert using Google AI Studio is fairly straightforward - the
   hard part is creating the proper prompt, and there we’ve got you covered.

   **Step 1** - First, log into `Google AI Studio
   <https://ai.google.dev/aistudio>`_. You can do this by clicking the “Sign in
   to Google AI Studio” button on the front page of the Google AI Studio home
   page. You will need a Google account in order to do this - getting one is
   left as an exercise to the reader. The Google account is used to store your
   Google AI Studio prompt sessions and any content you upload to the model,
   and to track usage of the Gemini APIs.

   **Step 2** - Let’s download the *FIRST* Tech Challenge Competition Manual to your
   local computer. You can always find the latest Competition Manual PDF at the
   following link: 

   * https://ftc-resources.firstinspires.org/file/ftc/game/manual

   **Step 3** - In the left navigation pane towards the top of the pane, there
   is a circle with a plus inside it with the text “Create new prompt” next to
   it.  Clicking on this button will start a new prompt - though if you’re
   using Google AI Studio for the first time it’s likely a new prompt is
   already open. 

   Now that we have a new prompt, you can give the prompt a name.  This will
   allow the prompt to be saved in your "My Library" so you can come back and
   interact with the prompt later without having to recreate the prompt session
   every time. 

   In the bottom center of the workspace is a text field where you can enter in
   your prompt (it has a default prompt of “Type something”). BEFORE we enter
   our prompt, we want to add our Competition Manual PDF document. To add the
   document, click the “Plus” icon to the right of the prompt area.  This will
   give you several options, choose “Upload to Drive”. You can either click the
   “Browse” button to browse for the PDF of the Competition Manual that you
   downloaded, or you can drag the file into the window. This adds the
   Competition Manual to your prompt, it may take a minute or two to upload the
   PDF so please be patient.

   .. figure:: images/new_prompt.*
      :align: center
      :alt: Google AI Studio Screen
      :width: 75%

      Creating a prompt in Google AI Studio

   **Step 4** - Now that we have our document uploaded, we now want to enter our
   prompt. This prompt directs the AI in how to manage its responses, what
   information to use when developing a response, and sets up the role that the
   AI will attempt to play. Enter the following prompt and press the “Run”
   button:

   * *You are a helpful AI assistant providing answers to questions about the
     provided PDF. Do not use any prior knowledge; you have everything you need
     to answer questions in the one PDF provided. Cite all references.*

   Once the AI processes the initial prompt, we can then ask questions that the
   AI will use the Competition Manual to answer. Depending on the question, it
   may take the AI between several seconds up to a couple minutes to answer -
   be patient! Here are several questions you can ask (remember to press the
   “Run” button after asking each question):

   Example sample questions:

   * How many SAMPLES is a ROBOT allowed to CONTROL at a time?
   * What are the different ways to score points?
   * How large can a ROBOT be in its STARTING CONFIGURATION?
   * Which awards are best for advancement?
   * How do I write a strong engineering portfolio?

   Some prompts that require a lot of complex understanding or strategy can yield
   results that are not correct, especially if there is information “understood
   but not supplied.” For example, the following prompts provide some correct and
   some incorrect information:

   Examples of difficult questions:

   * What is the maximum score for an alliance?
   * Can ROBOTS pick up an opposing ALLIANCE'S SAMPLES?
   * How many matches does a team play at an event?

   This example was specific to FIRST Tech Challenge, but this process can be
   used for virtually any documents or media. Using AI as an analysis assistant
   can help you summarize news articles, find specific instructions in user
   manuals, review books, and more! Remember that the quality of the responses
   the AI provides is directly related to the quality of the prompt provided -
   even so, the AI isn’t always going to be able to provide correct answers so
   it’s up to you to verify the correctness of all answers provided by an AI.

.. dropdown:: Week of 09/09/2024 "AI Innovation Corner - Google AI Studio"

   .. _googleAIstudio:

   **AI Innovation Corner - Google AI Studio**

   This first article launched as part of the *Tech Tips of the Week*, but is
   the official first article for the AI Innovation Corner.

   This week’s Tech Tip of the Week launches a new initiative in *FIRST* Tech
   Challenge, an AI Innovation Corner. Generative AI has taken the world by
   storm, becoming commonplace now in everything from personal assistants,
   search engines, recipe curation, music innovation, and vehicle maintenance!
   Machine Learning AI has been a part of *FIRST* Tech Challenge in some way for
   the past six years, and we’re now transitioning to help teams learn how to
   use and incorporate Generative AI in their *FIRST* Tech Challenge experience
   (while we’re learning ourselves!).

   The first step (or *FIRST* step?) to getting the most out of AI is choosing a
   model. What do I mean by model? Every AI is a neural network that has been
   trained with specific knowledge with the ability to do specific things based
   on that knowledge. Each version of this neural network is stored in a “model”.
   Each different company has different models available for different purposes,
   though most models are variations on their flagship model (Gemini from Google,
   ChatGPT 4-o from OpenAI, Claude from Anthropic, and so on). Each company has
   different web-based and API interfaces for interacting with their models, and
   everyone has their favorite. In *FIRST* Tech Challenge, the standard tool we use
   is `Google AI Studio <https://ai.google.dev/aistudio>`__ to interact with Gemini.

   Google AI Studio is free to use, but requires a Google account to access -
   virtually all models require a login or API token of some kind to use. Google
   AI Studio is our favorite for its list of examples (Prompt Gallery) and its
   easy to use interface to save prompt sessions and resume them later. With
   Google AI Studio, you also can select the specific model you want to use, and
   when available you can choose to use preview versions of up and coming models.


