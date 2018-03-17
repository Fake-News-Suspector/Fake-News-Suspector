from rake_nltk import Rake
r=Rake()
mytext="Fake news is Siddarth died when he was Bathing"
r.extract_keywords_from_text(mytext)
result=r.get_ranked_phrases_with_scores()
keywords = []
i=0
for score,text in result:
    if score > 1.0:
        keywords.insert(i,text)
        i=i+1
print(keywords)
        
