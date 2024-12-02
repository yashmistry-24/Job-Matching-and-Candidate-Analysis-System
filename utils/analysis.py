from transformers import pipeline

# Load pre-trained models for classification tasks
communication_model = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
engagement_model = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
active_listening_model = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
sentiment_model = pipeline('sentiment-analysis')

# Function to perform analysis
def analyze_interview_v3(transcription):
    # Sentiment analysis
    sentiment = sentiment_model(transcription)
    sentiment_label = sentiment[0]['label']
    sentiment_score = sentiment[0]['score']
    
    # Define thresholds for sentiment
    if sentiment_label == "NEGATIVE" and sentiment_score > 0.5:
        sentiment = "NEGATIVE"
    else:
        sentiment = "POSITIVE"
    
    # Communication Style (using BART for classification)
    communication_labels = ["Clear and concise", "Unclear", "Verbose", "Confusing"]
    communication_result = communication_model(transcription, candidate_labels=communication_labels)
    communication_style = communication_result['labels'][0]
    
    # Active Listening (using BART for classification)
    listening_labels = ["Attentive", "Inattentive", "Passive", "Engaged", "Disengaged"]
    listening_result = active_listening_model(transcription, candidate_labels=listening_labels)
    active_listening = listening_result['labels'][0]
    
    # Engagement (using BART for classification)
    engagement_labels = ["Engaging", "Disengaged", "Passive", "Interactive", "Active"]
    engagement_result = engagement_model(transcription, candidate_labels=engagement_labels)
    engagement = engagement_result['labels'][0]
    
    return {
        'communication_style': communication_style,
        'active_listening': active_listening,
        'engagement': engagement
    }
