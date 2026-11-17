# Que --> Given a Pandas DataFrame employee containing employee salary information, find the second highest distinct salary. Return the result as a DataFrame with a single column named SecondHighestSalary. If there is no second highest distinct salary, return None in that column.

import pandas as pd

class Solution:
    def secondHighestSalary(self, employee: pd.DataFrame) -> pd.DataFrame:
        distinct_salaries = employee['salary'].drop_duplicates()

                # If there are fewer than 2 distinct salaries, return None
        if len(distinct_salaries) < 2:
            return pd.DataFrame({'SecondHighestSalary': [None]})

                # Fetch the second largest distinct value
        second_highest = distinct_salaries.nlargest(2).iloc[-1]

        return pd.DataFrame({'SecondHighestSalary': [second_highest]})
        