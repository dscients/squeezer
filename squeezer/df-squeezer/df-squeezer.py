import pandas as pd
import numpy as np


def df_squeeze(df, report=True, edit=False):
    """
    Enhance memory usage of a pandas DataFrame by suggesting or applying dtype conversions.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        report (bool): If True, prints suggested changes.
        edit (bool): If True, applies the suggested dtype conversions directly to the DataFrame.

    Returns:
        pd.DataFrame: DataFrame with applied changes if edit=True. Otherwise, returns the original DataFrame.
    """
    conversion_suggestions = []
    original_memory_usage = df.memory_usage(deep=True).sum()

    for col in df.columns:
        original_dtype = df[col].dtype
        best_dtype = original_dtype
        if df[col].dtype.kind in "if":  # Process float and int columns
            # Downcast integers and floats
            df[col] = pd.to_numeric(
                df[col], downcast="integer" if df[col].dtype.kind == "i" else "float"
            )
            best_dtype = df[col].dtype
        elif df[col].dtype == "object" and df[col].nunique() < df.shape[0] / 2:
            # Suggest converting object to category if it makes sense
            suggested_dtype = "category"
            conversion_suggestions.append((col, original_dtype, suggested_dtype))
            if edit:  # Apply conversion
                df[col] = df[col].astype(suggested_dtype)
                best_dtype = suggested_dtype

        if report:
            # Report the suggestion
            if original_dtype != best_dtype:
                print(
                    f"Suggested conversion for column '{col}': {original_dtype} -> {best_dtype}"
                )

    if report:
        new_memory_usage = df.memory_usage(deep=True).sum()
        print(f"\nOriginal total memory usage: {original_memory_usage:,} bytes")
        print(f"New total memory usage: {new_memory_usage:,} bytes")
        print(f"Memory saved: {original_memory_usage - new_memory_usage:,} bytes")

        # Print executable Python code for suggestions
        print("\n# Executable Python code for suggested dtype conversions:")
        for col, original_dtype, suggested_dtype in conversion_suggestions:
            print(f"df['{col}'] = df['{col}'].astype('{suggested_dtype}')")

    return df
