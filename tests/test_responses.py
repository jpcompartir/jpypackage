from jpypackage.responses import Sentiment, AbsaResponse
import pytest

def test_sentiment():    
    assert Sentiment.positive.value == "positive"
    assert Sentiment.negative.value == "negative"
    assert Sentiment.neutral.value == "neutral"
    
def test_sentiment_case():
    assert Sentiment("Positive").value == "positive"
    assert Sentiment("NEGATIVE").value == "negative"
    
    