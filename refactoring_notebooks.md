# Refactoring notebooks

My process for refactoring the titanic notebook
- Ensure that notebooks when run from start to end
- Read notebook and list code smells
- Make a copy of the original notebook (for comparing the end result later)
- Delete code that are just for side effects
    - many of such code are for exploratory data analysis, for giving us feedback and insight into the data (e.g. how many target classes are there, what do the features look like, etc.). But when we're done digesting the information, we've gotten what we need, there's no need to leave them lying around.


Code smells
- too many comments
- bad variable names
    - train_df and test_df could be better named (without type information)
    - combine
- too many print statements
    - df.info(), df.head(), df.describe(), etc. - is there any other way that we can get feedback on the data?
- no tests for data transformations (e.g. cell 17 onwards)
- cell 18, 19 (mutation to `dataset` outside of a function)
- [x] duplication in model training code. Can extract to a function.
- duplication in EDA code. Can extract to a function.
- [x] duplication in how test_df and train_df are joined. Why not just join it once, and use the combined df for all data transformations?

Refactoring:
- Extract function and add tests for:
    - [x] Extract titles from names and encode it