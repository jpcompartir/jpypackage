from jpypackage.prompts import Prompt, absa
from pydantic import ValidationError
import pytest

def test_prompt_errors():
    with pytest.raises(ValidationError):
        Prompt()
    
def test_prompt_runs():
    x = Prompt(
        name = "a",
        description = "b",
        system = "c",
        user = "d",
        model = "e"
    )
    
    assert isinstance(x, Prompt)
    
    #Custom values are as expected
    assert x.name == "a"
    assert x.description == "b"
    assert x.system == "c"
    assert x.user == "d"
    assert x.model == "e"
    
    #Default values are as expeccted
    assert x.response_format == {"type": "json_object"}
    assert x.temperature == 0.0


def test_absa():
    assert isinstance(absa, Prompt)
    
    assert absa.name == "Aspect-based sentiment analysis"
    assert absa.description.startswith("Prompt for identifying")
    assert absa.system == 'You are a helpful assistant designed to output JSON. You identify companies, products, and services in a document and extract a sentiment classification for each aspect.\nOutput JSON  fields for entity, aspect, sentiment.'
    assert absa.model == "gpt-4-1106-preview"
        

    
