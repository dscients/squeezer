# DF-Squeezer

DF-Squeezer is a Python package designed to help reduce the memory usage of pandas DataFrames. By analyzing the data
types of DataFrame columns, DF-Squeezer suggests and can automatically apply data type conversions that are more
memory-efficient without losing information.

## Features

- **Analysis of DataFrame Columns**: Identifies columns that can be converted to more memory-efficient data types.
- **Memory Usage Reporting**: Calculates and reports the potential memory savings from suggested conversions.
- **Automatic Conversion Application**: Optionally applies suggested conversions directly to the DataFrame.

## Installation

To install DF-Squeezer, run the following command in your terminal:

```sh
pip install df-squeezer
```

Ensure you have pandas installed in your environment as it is a required dependency.

## Usage

```
from df_squeezer import df_squeeze
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({
    'a': range(1000),
    'b': [float(i) for i in range(1000)],
    'c': ['category' + str(i % 3) for i in range(1000)]
})

# Use df_squeeze to analyze and report potential dtype conversions
optimized_df = df_squeeze(df, report=True, edit=False)

# To directly apply the suggested conversions
optimized_df = df_squeeze(df, report=True, edit=True)


```

## Parameters

df (pd.DataFrame): The input DataFrame to analyze and optimize.
report (bool, optional): If True (default), prints suggested changes for data type conversions along with potential
memory savings.
edit (bool, optional): If False (default), the function only reports potential optimizations without applying them. If
True, the function applies the suggested data type conversions directly to the DataFrame.
Returns
pd.DataFrame: The original DataFrame with applied changes if edit=True. Otherwise, returns the original DataFrame
unmodified.
Contributing
Contributions to DF-Squeezer are welcome! Please refer to the contribution guidelines for more information.

License
This project is licensed under the MIT License - see the LICENSE file for details.