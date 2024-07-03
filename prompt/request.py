import os
from model.model import design_persona_repuest

def design_and_save_prompt(category: str, name: str, information: str) -> None:
    """
    Designs a persona prompt using the user's selected category, name, and information, 
    and saves the prompt to a file in a specified directory.
    
    Args:
        category (str): Category selected by the user (e.g., Team, Artist)
        name (str): Name selected by user (e.g., Psy, STACY)
        information (str): Data collected from the tree wiki via crawling

    Returns:
        None: This function does not return any value. It writes the designed prompt to a file.
    """
    designed_prompt = design_persona_repuest(category=category, name=name, information=information)
    
    directory_path = f'output/{name}'
    os.makedirs(directory_path, exist_ok=True)
    
    file_path = f'{directory_path}/persona.txt'
    with open(file_path, 'w') as file:
        file.write(designed_prompt)