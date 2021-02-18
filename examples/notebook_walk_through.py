# %% [markdown]

# # Test Data Generation

# This notebook runs through the key methods contained within
# this repo.

# %%
import seaborn as sns
import pandas as pd
import os
import sys
sys.path.insert(0, os.path.abspath('../test_data_gen'))
from test_data_gen import TestDataGenerator

# %% [markdown]

# ## Log Normal Distribution

# This method generates a random value from a log normal distribution.

# %%
print(TestDataGenerator.log_normal(100))

# %%
df = pd.DataFrame.from_dict(
    {
        'random_log_normal': [TestDataGenerator.log_normal(100) for i in range(0, 1000)]
    }
)

# %%
sns.set(rc={'figure.figsize': (10, 8)})
sns.histplot(data=df)

# %% [markdown]

# ## Choose Log

# This method chooses a categorical value from a list according
# to a log distribution of the values.


# %%
print(TestDataGenerator.choose_log(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']))

# %%
df = pd.DataFrame.from_dict(
    {
        'exponential_category': [TestDataGenerator.choose_log([
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']) for i in range(0, 1000)]
    }
)
df['count'] = 1

# %%
grouping_rules = ['exponential_category']
aggregation_rules = {'count': 'count'}
df_grouped = df.groupby(grouping_rules).count().reset_index()
df_grouped

# %%
sns.barplot(data=df_grouped, x='exponential_category', y='count')

# %%
