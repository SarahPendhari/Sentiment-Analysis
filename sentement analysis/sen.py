# In[104]:
import pandas as pd
# In[105]:
df=pd.read_csv("twitter_training.csv",header=None)
# In[106]:
df.head()
# In[107]:
df.columns=['id','place','type','text']
# In[108]:
df.head()
# In[109]:
df=df.drop(['id','place'],axis=1)
# In[110]:

df
# In[111]:
df.isnull().sum()
# In[112]:
df.dropna(inplace=True)

# In[113]:
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# Load data
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['type'], test_size=0.2, random_state=0)
# Create pipeline for preprocessing and model training
pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', MultinomialNB())
])
# Train pipeline on training data
pipeline.fit(X_train, y_train)
# Make predictions on testing data
y_pred = pipeline.predict(X_test)
# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
# In[116]:

ans=pipeline.predict(['I was extremely disappointed with this product. It didnt work at all and was a complete waste of money.'])
print(ans)
# In[ ]:




