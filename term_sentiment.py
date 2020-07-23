import sys

def create_sent_dict(sentiment_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

        Args:
            sentiment_file (string): The name of a tab-separated file that contains
                                     all terms and scores (e.g., the AFINN file).

        Returns:
            dicitonary: A dictionary with schema d[term] = score
        """
    afinnfile = open(sentiment_file, 'r')
    scores = {}
    for line in afinnfile:
        term, score = line.split("\t") 
        scores[term] = int(score) 
    afinnfile.close()

    
    return scores

def get_tweet_sentiment(tweet, sent_scores):
    """A function that find the sentiment of a tweet and outputs a sentiment score.

            Args:
                tweet (string): A clean tweet
                sent_scores (dictionary): The dictionary output by the method create_sent_dict

            Returns:
                score (numeric): The sentiment score of the tweet
        """
    score = 0
    
    for word in tweet.split():
        if word in sent_scores:
            score += sent_scores[word]
    
    return score

def term_sentiment(sent_scores, tweets_file):
    """A function that creates a dictionary which contains terms as keys and their sentiment score as value

            Args:
                sent_scores (dictionary): A dictionary with terms and their scores (the output of create_sent_dict)
                tweets_file (string): The name of a txt file that contain the clean tweets
            Returns:
                dicitonary: A dictionary with schema d[new_term] = score
            """
    new_term_sent = {}
    
    afinnfile = open(tweets_file, 'r')
    
    for line in afinnfile:
        score = get_tweet_sentiment(line, sent_scores)
        for word in line.split():
            if word not in sent_scores:
                if word in new_term_sent:
                    new_term_sent[word] = (new_term_sent[word]+int(score))/2
                else:   
                    new_term_sent[word] = int(score)
    afinnfile.close()
    
    return new_term_sent


def main():
    sentiment_file = sys.argv[1]
    tweets_file = sys.argv[2]

    # Read the AFINN-111 data into a dictionary
    sent_scores = create_sent_dict(sentiment_file)

    # Derive the sentiment of new terms
    new_term_sent = term_sentiment(sent_scores, tweets_file)

    for term in new_term_sent:        
        print(term, new_term_sent[term])


if __name__ == '__main__':
    main()