from pydantic import BaseModel, Field, validator
from enum import Enum

""""
The process we want to define classes for here, is ensuring that our calls to the OpenAI (for now) API return JSON with the right key:value pairs. We'll be using pydantic to do this.
"""
class Sentiment(Enum):
    positive = "positive"
    negative = "negative"
    neutral = "neutral"
    
    
class AbsaResponse(BaseModel):
    entity: str = Field(..., description="The entity identified in the document")
    aspect: str = Field(..., description="The aspect identified in the document")
    sentiment: Sentiment = Field(..., description="The sentiment classification for the aspect")
    
    class Config:
        schema_extra = {
            "example": {
                "entity": "Apple",
                "aspect": "customer service",
                "sentiment": "positive"
            }
        }
        
def main():
    x = AbsaResponse(
        entity = "Man Utd",
        aspect = "Playing staff",
        sentiment = "negative"
    )
    print(x.entity)
    print(x.aspect)
    print(x.sentiment.value)

if __name__ == "__main__":
    main()