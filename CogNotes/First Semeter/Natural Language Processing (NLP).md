Written by: Laurits Lyngbæk
Source of information: [Introduction to NLP](https://algorithmia.com/blog/introduction-natural-language-processing-nlp)
Association links: [[001 CogCom]]
Tags: #🌿Sprout 
___
# Natural language processing 
NLP is the processing of natural language production. This could be transcribed dialogue, books or tweets (etc.). It can be used to perform tasks such as:
- automatic summarization
- translation 
- named entity recognition
 - relationship extraction
 - sentiment analysis
 - speech recognition
 - topic segmentation.

NLP allows the developer to create software that understands human language (and possibly is able to interact with it).


#### Links for interface NLP:

-   **Summarize blocks of text** using [Summarizer](https://algorithmia.com/algorithms/nlp/Summarizer?utm_source=blog&utm_medium=post&utm_campaign=nlp) to extract the most important and central ideas while ignoring irrelevant information. 
-   **Automatically generate keyword tags** from content using [AutoTag](https://algorithmia.com/algorithms/nlp/AutoTag?utm_source=blog&utm_medium=post&utm_campaign=nlp), which leverages LDA, a technique that discovers topics contained within a body of text.
-   **Identify the type of entity extracted**, such as it being a person, place, or organization using [Named Entity Recognition](https://algorithmia.com/algorithms/StanfordNLP/NamedEntityRecognition?utm_source=blog&utm_medium=post&utm_campaign=nlp).
-   Use [Sentiment Analysis](https://algorithmia.com/algorithms/nlp/SentimentAnalysis?utm_source=blog&utm_medium=post&utm_campaign=nlp) to **identify the sentiment of a string of text**, from very negative to neutral to very positive.
-   **Reduce words to their root**, or stem, using [PorterStemmer](https://algorithmia.com/algorithms/codeb34v3r/PorterStemmer?utm_source=blog&utm_medium=post&utm_campaign=nlp), or **break up text into tokens** using [Tokenizer](https://algorithmia.com/algorithms/ApacheOpenNLP/Tokenizer?utm_source=blog&utm_medium=post&utm_campaign=nlp).

### Preprocessing of text data:
##### **Tokenization:**
- Splitting up texts in smaller chucks (most often individual words) 
- Cleaning up punctutations 

##### **Regular expressions:**
- Search for patterns (rather than individual word tokens) in texts
- If the text uses ‘meta-characters’ such as ?, * and + 
- For example: 
	- we could use the pattern ”(red|blue|green|yellow)” to count color words 
	- ”colo(u)r” matches both "color" and "colour”
	- ”ab*c” matches "ac", "abc", "abbc", "abbbc", and so on 
	- ”\d” any digit 

##### **Stop words:**
Sometimes we are not interested in including very frequent function words like “a”, “the”, “that”, “in”, “on”:
**This can be filtered using a "stop word list".** Some standard lists comes with NLP packages:
Tidytext: list of 1149 words 
TM: 174 
Quanteda: 175

##### **Stemming**
- Cuts words to their stem (throw away suffixes and affixes)
- “overcook”, “cooking,” and “cooked” --> “**cook**”
**Be aware of potential overstemming:** 
- “university”, “universal”, “universities”, and “universe” could become “**univers**”

##### **Lemmatization**
- Replace word by its dictionary or canonical form
	- “is”, “was”, “were” --> “**be**” 
	-  “runs”, “running”, “ran” --> “**run**”


## [[Word Embeddings]]
A numeric representation of a word (a vector of values). Used to visualize [[Semantic Network|Semantic]] distance between words.


