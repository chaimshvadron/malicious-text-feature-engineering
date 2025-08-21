import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class SentimentProcessor:

	def __init__(self):
		nltk.download('vader_lexicon', quiet=True)
		self.analyzer = SentimentIntensityAnalyzer()

	def get_sentiment(self, text):
		score = self.analyzer.polarity_scores(text)
		compound = score['compound']
		if compound >= 0.5:
			return 'Positive'
		elif compound <= -0.5:
			return 'Negative'
		else:
			return 'Neutral'

