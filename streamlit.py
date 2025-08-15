{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "86d8fd0a-0d34-41bd-8214-9c3df75a302b",
   "metadata": {},
   "outputs": [],
   "source": [
    "# =====================================\n",
    "# STEP 11: Optional UI with Streamlit\n",
    "# =====================================\n",
    "import streamlit as st\n",
    "from nltk.sentiment.vader import SentimentIntensityAnalyzer\n",
    "from transformers import pipeline\n",
    "\n",
    "# Load VADER\n",
    "vader = SentimentIntensityAnalyzer()\n",
    "\n",
    "# Load HuggingFace sentiment pipeline\n",
    "hf_pipeline = pipeline(\"sentiment-analysis\", model=\"distilbert-base-uncased-finetuned-sst-2-english\")\n",
    "\n",
    "st.title(\"🎬 Movie Review Sentiment Analysis\")\n",
    "st.write(\"Paste a review below to see sentiment analysis from both VADER and HuggingFace Transformer.\")\n",
    "\n",
    "# Input text\n",
    "user_review = st.text_area(\"Enter your movie review here:\")\n",
    "\n",
    "if st.button(\"Analyze Sentiment\"):\n",
    "    if user_review.strip() != \"\":\n",
    "        # VADER Analysis\n",
    "        vader_scores = vader.polarity_scores(user_review)\n",
    "        if vader_scores['compound'] >= 0.05:\n",
    "            vader_sentiment = \"Positive\"\n",
    "        elif vader_scores['compound'] <= -0.05:\n",
    "            vader_sentiment = \"Negative\"\n",
    "        else:\n",
    "            vader_sentiment = \"Neutral\"\n",
    "        \n",
    "        # HuggingFace Analysis\n",
    "        hf_result = hf_pipeline(user_review)[0]\n",
    "        hf_sentiment = hf_result['label']\n",
    "        hf_score = hf_result['score']\n",
    "\n",
    "        # Display results\n",
    "        st.subheader(\"📊 VADER Sentiment\")\n",
    "        st.write(f\"Sentiment: **{vader_sentiment}**\")\n",
    "        st.json(vader_scores)\n",
    "\n",
    "        st.subheader(\"🤖 HuggingFace Transformer Sentiment\")\n",
    "        st.write(f\"Sentiment: **{hf_sentiment}** (Confidence: {hf_score:.2f})\")\n",
    "\n",
    "    else:\n",
    "        st.warning(\"Please enter a review before analyzing.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
