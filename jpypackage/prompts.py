from pydantic import BaseModel
from typing import Optional, Dict

class Prompt(BaseModel):
    name: str
    description: str
    system: str
    user: str
    model: str
    response_format: Optional[Dict] = {"type": "json_object"}
    temperature: Optional[float] = 0.0
    
absa = Prompt(
    name = "Aspect-based sentiment analysis",
    description = "Prompt for identifying aspects in a document and extracting a sentiment classification for each aspect,",
    system = "You are a helpful assistant designed to output JSON. You identify companies, products, and services in a document and extract a sentiment classification for each aspect.\nOutput JSON  fields for entity, aspect, sentiment.",
    user = "",
    model = "gpt-4-1106-preview"
)

entity_sentiment = Prompt(
    name = "An entity-specific sentiment classification",
    description = "Prompt for identifying high-level entities in a document and extracting a sentiment classification for each entity",
    system = "You are a helpful assistant designed to output JSON. You recognise Named Entities and output a sentiment classification for each entity.\nOutput JSON fields for entity, and sentiment only.",
    user = "",
    model = "gpt-3.5-turbo-1106"
)