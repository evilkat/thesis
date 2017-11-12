#import TextBlob
from textblob import TextBlob

def computeSentiment(count,timestamptweet,sentence_text,rtc,fc,mention):
    blob = TextBlob(sentence_text)
    #print(blob.tags)
    #print(blob.noun_phrases)
    if blob.sentiment.polarity > 0.0 or blob.sentiment.subjectivity > 0.0:
        print(timestamptweet,'retweet count: ',rtc,'favorite_count: ',fc,'Mention count: ',mention)
        print(blob.sentiment.polarity)
        print(blob.sentiment.subjectivity)
        count = count + 1
        
        if blob.sentiment.polarity == 0.0:
            print("Neutral")

        elif blob.sentiment.polarity < 0:
                print("Negative")
        else:
                print("Positive")

    return count
        #print(blob.noun_phrases)
