from pydantic import BaseModel, Field, validator
from enum import Enum

""""
The process we want to define classes for here, is ensuring that our calls to the OpenAI (for now) API return JSON with the right key:value pairs. We'll be using pydantic to do this, and enum because our sentiment options are limited. 
"""

#Sentiment will currently throw an error if the value is "Positive", make it case insensitive

class Sentiment(Enum):
    positive = "positive"
    negative = "negative"
    neutral = "neutral"
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return self.value

    @classmethod
    def _missing_(cls, value):
        for member in cls:
            if member.value.lower() == value.lower():
                return member
        return super()._missing_(value)
    
    
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
        sentiment = "Negative"
    )
    print(x.entity)
    print(x.aspect)
    print(x.sentiment.value)

if __name__ == "__main__":
    main()
    