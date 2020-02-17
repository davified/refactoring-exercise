# Clean Code Cheat Sheet

## Table of Contents

[Variables](#variables)

- Variable names should reveal intent

[Dispensables](#dispensables)

- Avoid comments
- Remove dead code
- Avoid print statements (even glorified print statements such as df.head(), df.describe(), df.plot())

[Functions](#functions)

- Use functions to keep code "DRY"
- Functions should do one thing

[Design](#design)

- Don't expose your internals (Keep implementation details hidden)

---

## Variables

### Variable names should reveal intent

We will read more code than we will ever write. It's important for our code to express intent so that our readers don't have to waste mental effort to figure out puzzles.

One common culprit in data science code is dataframes. Every dataframe is named as `df`. In software programming, it's an unusual (and bad) practice to embed information about variable types in the variable name (e.g. we would probably never write `string = 'Hello friends'`. Instead, we would write `greeting = 'Hello friends'`).

**Bad:**

```python
df = pd.read_csv('loans.csv')

_df = df.groupby(['month']).sum()
__df = filter_loans(_df, month=12)

# let's try to calculate total loan amount for december
total_loan_amount = __df... # wait, should I use df, _df or __df?
```

**Good**:
One rule of thumb on how to name dataframes is to think about what is in each row. For instance, if each row in my dataframe is a loan, then the dataframe is a **collection of loan entries**. Hence, we could call the dataframe `loans`.

```python
loans = pd.read_csv('loans.csv')

monthly_loans = loans.groupby(['month']).sum()
monthly_loans_in_december = filter_loans(monthly_loans, month=12)

# let's try to calculate total loan amount for december
total_loan_amount = monthly_loans_in_december.sum()

```

**[⬆ back to top](#table-of-contents)**

---

## Dispensables

### Avoid comments

Comments can become problematic in a few ways:

- If some code needs comments, it's a smell for deeper issues (e.g. bad variable naming, violation of single responsibility principle, poor abstraction)
- Comments can grow stale and they can lie
- Comments can make code even harder to understand when there's too much of it.

With good variable names, proper abstraction of our code into functions with single responsibility and unit tests, we can understand our code without comments.

**Bad:**

```python
# Check to see if employee is eligible for full benefits
if (employee.flags and HOURLY_FLAG) and (employee.age > 65):
    # do something
```

**Good:**

```python
if employee.isEligibleForBenefits():
    # do something
```

---

### Remove dead code

Dead code is code which is executed but whose result is never used in any other computation. Dead code is yet another unrelated thing that developers have to hold in our head when coding. It adds unnecessary cognitive load.

If there's code which does not change the result of the program whether it runs or not, then it's not required for the code to run. We should remove it to keep the codebase clean. When we make small and frequent commits, we need not fear losing code. If we ever need those lines of code again, we can easily recover it from the git history.

One common type of dead code are print statements (even glorified print statements such as `df.head()`, `df.describe()`, `df.plot()`). While these offer useful feedback when we're writing code, too much of it makes code hard to read. The team has to visually parse the notebook and spend mental effort to filter out inconsequential print statements in order to find the code that actually has an effect on the output.

When our codebase has unit tests, the feedback from unit tests replaces the manual/visual feedback we used to use (e.g. df.head()) to check if things are working. This allows us to remove these print statements and make our code more readable.

**Bad:**

```python
df = get_data()
print(df)
# do_other_stuff()
# do_some_more_stuff()
df.head()
print(df.columns)

# do_so_much_stuff()
model = train_model(df)

```

**Good:**

```python
df  = get_data()
model = train_model(df)
```

**[⬆ back to top](#table-of-contents)**

---

## Functions

### Use functions to keep code "DRY"

The developer who learns to recognize duplication, and understands how to eliminate it through proper abstraction (i.e. defining the right functions or methods), can produce much cleaner code than one who continuously infects the application with unnecessary repetition.

Every line of code that goes into an application must be maintained, and is a potential source of future bugs. Duplication needlessly bloats the codebase, resulting in more opportunities for bugs and adding accidental complexity to the system. The bloat that duplication adds to the system also makes it more difficult for developers working with the system to fully understand the entire system, or to be certain that changes made in one location do not also need to be made in other places that duplicate the logic they are working on. DRY requires that "every piece of knowledge must have a single, unambiguous, authoritative representation within a system."

[Source: 97 Things Every Programmer Should Know](https://97-things-every-x-should-know.gitbooks.io/97-things-every-programmer-should-know/content/en/thing_30/)

**Bad:**

```python
decision_tree_model = DecisionTreeClassifier()
decision_tree_model.fit(X_train, Y_train)
Y_pred = decision_tree_model.predict(X_test)
decision_tree_accuracy = round(decision_tree_model.score(X_train, Y_train) * 100, 2)
print(decision_tree_accuracy)

random_forest_model = RandomForestClassifier(n_estimators=100)
random_forest_model.fit(X_train, Y_train)
Y_pred = random_forest_model.predict(X_test)
random_forest_model.score(X_train, Y_train)
random_forest_accuracy = round(random_forest_model.score(X_train, Y_train) * 100, 2)
print(random_forest_accuracy)

gaussian_model = GaussianNB()
gaussian_model.fit(X_train, Y_train)
Y_pred = gaussian_model.predict(X_test)
gaussian_accuracy = round(gaussian_model.score(X_train, Y_train) * 100, 2)
print(gaussian_accuracy)
```

**Good**:

```python
def train_model(ModelClass, X_train, Y_train, **kwargs):
    model = ModelClass(**kwargs)
    model.fit(X_train, Y_train)

    accuracy_score = round(model.score(X_train, Y_train) * 100, 2)
    print(f'accuracy ({ModelClass.__name__}): {accuracy_score}')

    return model, accuracy_score

decision_tree_model, decision_tree_accuracy = train_model(DecisionTreeClassifier, X_train, Y_train)
random_forest_model, random_forest_accuracy = train_model(RandomForestClassifier, X_train, Y_train, n_estimators=100)
gaussian_model     , gaussian_accuracy      = train_model(GaussianNB, X_train, Y_train)
```

**Tip**: Notice how the symmetry of the 3 code blocks in the bad example made it easier for us to identify and refactor the duplicated code? One useful practice in eliminating duplication is to **first make the duplication as obvious as possible**. This makes it easier for us to identify opportunities for extracting the duplication into their appropriate homes.

---

### Functions should do one thing

This is by far the most important rule in software engineering. When functions do more than one thing, they are harder to compose, test, and reason about. When you can isolate a function to just one action, they can be refactored easily and your code will read much cleaner. If you take nothing else away from this guide other than this, you'll be ahead of many developers.

**[⬆ back to top](#table-of-contents)**

---

## Design

### Avoid exposing your internals (Keep implementation details hidden)

Functions and classes simplify our code by abstracting away complicated implementation details and replacing them with a simpler representation - its name. When implementation details are all laid bare in a Jupyter notebook without any abstractions (functions), we are forced to understand the **how**'s in order to find out **what**'s happening.

Imagine you’re in a restaurant and you’re given a menu. Instead of telling you the name of the dishes, this menu spells out the recipe for each dish. For example, one such dish is:

<img src="../images/implementation_menu.png" width=500 alt="dinner menu without abstrations">

It would have been easier for us if the menu hid all the steps in the recipe (i.e. the implementation details) and instead gave us the name of the dish (an interface, a.k.a. an **abstraction**, of the dish). (Answer: that was Lentil Soup).

**Bad:**

```python
print(pd.qcut(df['Fare'], q=4)) # pd.Series([7.91, 14.454, 31])

df.loc[ df['Fare'] <= 7.91, 'Fare'] = 0
df.loc[(df['Fare'] > 7.91) & (df['Fare'] <= 14.454), 'Fare'] = 1
df.loc[(df['Fare'] > 14.454) & (df['Fare'] <= 31), 'Fare']   = 2
df.loc[ df['Fare'] > 31, 'Fare'] = 3
df['Fare'] = df['Fare'].astype(int)
df['FareBand'] = df['Fare']
```

**Good**:

```python
df['FareBand'] = categorize_column(df['Fare'], num_bins=4)
```

**[⬆ back to top](#table-of-contents)**
