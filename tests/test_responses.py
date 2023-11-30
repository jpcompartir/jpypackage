from jpypacakge.responses import Sentiment, AbsaResponse
import pytest

def test_sentiment():    
    assert Sentiment.positive.value == "positive"
    assert Sentiment.negative.value == "negative"
    assert Sentiment.neutral.value == "neutral"
    
def test_absa_response():
    pass



