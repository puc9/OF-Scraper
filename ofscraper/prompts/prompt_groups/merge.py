from InquirerPy.base import Choice
from prompt_toolkit.shortcuts import prompt as prompt
from rich.console import Console

import ofscraper.prompts.prompt_validators as prompt_validators
import ofscraper.prompts.promptConvert as promptClasses
from InquirerPy.validator import  PathValidator
from ofscraper.utils.paths.common import get_profile_path


console = Console()
models = None




def backup_prompt() -> bool:
    name = "continue"
    answer = promptClasses.batchConverter(
        *[
            {
                "type": "list",
                "name": name,
                "message": "Have you backed up your database files?",
                "choices": [Choice(True,"Yes"),Choice(False,"No")],
            }
        ]
    )
    return answer[name]


def folder_prompt():
    answer = promptClasses.batchConverter(
        *[
            {
                "type": "filepath",
                "name": "database",
                "message": "root database folder: ",
                "option_instruction": "The database path given will be searched recursively, so pick the closest path possible",
                "filter": lambda x: prompt_validators.cleanTextInput(x),
                "validate": PathValidator(is_dir=True),
                "default": str(get_profile_path())
            },
        ]
    )
    return answer["database"]

def new_db_prompt():
    answer = promptClasses.batchConverter(
        *[
            {
                "type": "input",
                "name": "database",
                "message": "Merge db dir: ",
                "option_instruction": """
                directory for new merge database
                It is best if merged database is stored seperately from source database(s)"
                """,
                                "default": str(get_profile_path()),

                "filter": lambda x: prompt_validators.cleanTextInput(x),
            },
        ]
    )
    return answer["database"]