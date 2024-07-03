from dotenv import load_dotenv
from prompt.prompt import ARTIST_PROMPT_TEMPLATE, TEAM_PROMPT_TEMPLATE
from langchain_core.prompts import PromptTemplate
from openai import OpenAI

load_dotenv()
client = OpenAI()

def design_persona_repuest(category: str, name:str, information: str) -> str:
    """
    Generates a persona prompt based on the user's selected category, name, and information collected from a data source.

    Args:
        category (str): Category selected by the user (e.g Team, Artist)
        name (str): Name selected by user(e.g Psy, STACY..)
        information (str): Data collected from the tree wiki via crawling

    Returns:
        str: Persona Prompt Content

    Raises:
        Exception: If any error occurs during the process

    Note:
        This function uses OpenAI's GPT-4 model to generate the persona prompt.
        It first defines a template for the prompt based on the selected category.
        Then, it formats the template with the provided name.
        Next, it creates a chat completion with the formatted prompt and the provided information.
        Finally, it returns the generated persona prompt.
    """
    try: 
        # Template definition
        template_category = {
            'artist': lambda : ARTIST_PROMPT_TEMPLATE,
            'team' : lambda : TEAM_PROMPT_TEMPLATE 
        }
        
        # Create a PromptTemplate object from the selected template
        model_prompt = PromptTemplate.from_template(template_category[category]())
        
        # Format the prompt template with the provided name
        FORMATTED_PROMPT = model_prompt.format(name=name)
        
        # Define the messages for the chat completion
        messages=[
            {"role": "system", "content":FORMATTED_PROMPT},
            {"role": "user", "content": information}
        ]

        # Create a chat completion with OpenAI's GPT-4 model
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=1.0,
            top_p=0.9,
            max_tokens=1024,
            presence_penalty=0,
            frequency_penalty=0,
            # response_format={'type': "json_object"}
        )
        
        # Return the generated persona prompt
        return completion.choices[0].message.content
    except Exception as e:
        # Print any error that occurs during the process
        print(e)