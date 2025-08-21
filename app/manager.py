class Manager:
    def __init__(self, connector, dal, rare_word_processor, sentiment_processor, weapon_processor):
        self.connector = connector
        self.dal = dal
        self.rare_word_processor = rare_word_processor
        self.sentiment_processor = sentiment_processor
        self.weapon_processor = weapon_processor

    def process_records(self, collection_name):
        with self.connector as conn:
            db = conn.get_db()
            self.dal.db = db 
            processed = []
            for record in self.dal.fetch_all(collection_name):
                original_text = record.get('Text', '')
                rarest_word = self.rare_word_processor.find_rare_word(original_text)
                sentiment = self.sentiment_processor.get_sentiment(original_text)
                weapon = self.weapon_processor.find_weapon(original_text)
                processed.append({
                    'id': str(record.get('_id', '')),
                    'original_text': original_text,
                    'rarest_word': rarest_word,
                    'sentiment': sentiment,
                    'weapons_detected': weapon
                })
            return processed