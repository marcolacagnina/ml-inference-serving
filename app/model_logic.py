from transformers import pipeline

print("Loading model...")
classifier = pipeline("sentiment-analysis", 
                      model="distilbert-base-uncased-finetuned-sst-2-english"
                      )

def predict_sentiment(text: str):
    result = classifier(text)[0]
    return {
        "label": result['label'],
        "score": round(result['score'], 4)
    }

# To test the model
if __name__ == "__main__":
    print(predict_sentiment("I love learning MLOps!"))