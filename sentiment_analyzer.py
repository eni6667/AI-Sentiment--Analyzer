from transformers import pipeline

sentiment = pipeline("sentiment-analysis")

print("AI Sentiment Analyzer")
print("---------------------")

while True:
    text = input("\nWrite a sentence (or type exit): ")

    if text.lower() == "exit":
        break

    result = sentiment(text)

    label = result[0]['label']
    score = result[0]['score']

    print("Prediction:", label)
    print("Confidence:", round(score * 100, 2), "%")