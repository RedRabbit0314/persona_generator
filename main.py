from prompt.request import design_and_save_prompt
from utils.scraping import url_to_page_source

def make_prompt(category: str, name: str) -> str:
    """
    Generates a successful message based on the user's selected category and name.

    Args:
        category (str): Category selected by the user (e.g team, artist)
        name (str): Name selected by user(e.g DAY6, STACY..)

    Returns:
        str: Successful Message
    """
    try: 
        url =f'https://namu.wiki/w/{name}'
        raw_data = url_to_page_source(category=category, url=url)
        design_and_save_prompt(category=category, name=name, information=raw_data)
        completed_message = 'Prompt creation completed successfully.'
        return completed_message
    except Exception as e:
        uncompleted_message = f'Prompt creation failed due to {e}.'
        return uncompleted_message

if __name__ == "__main__":
    make_prompt(category='artist', name= '안성훈')