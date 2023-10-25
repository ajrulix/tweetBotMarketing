from string import Template

## For the LLM Prompting
USER_ID = 'openai'
APP_ID = 'chat-completion'
MODEL_ID = 'GPT-4'
MODEL_VERSION_ID = '4aa760933afa4a33a0e5b4652cfa92fa'

PROMPT_TEMPLATE = Template("$system Write a short tweet to promote $topic. \
                           Only output the raw text of the tweet \
                           without any instructions or any preamble. \
                           Include the tag '@clarifai'. Include the \
                           hashtags '#Clarifai #AI'. Include the \
                           relevant link `$link`. Limit the tweet \
                           to 260 characters including the link.")

YEAR_ONWARDS = 2023
SITEMAP_URL = "https://www.clarifai.com/sitemap.xml"
LASTMOD = "lastmod"

SYSTEM_PROMPTS = [
    "",
    "You are a Twitter influencer who summarizes news for your lovely AI enthusiast audience, don't be boring or generic and keep it conversational" 
]

## For building the HTML
TWITTER_USER_ID='RealAIPlusMe'

## For uploading the screenshot to clarifai
UPLOAD_USER_ID = 'Isaac'
UPLOAD_APP_ID = 'q4-tweet-screenshots'
