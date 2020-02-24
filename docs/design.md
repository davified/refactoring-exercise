# **Design**

## Avoid exposing your internals (Keep implementation details hidden)

```txt
"The purpose of abstraction is not to be vague, but to create a new semantic level in which one can be absolutely precise."

- Edsger Dijkstra
```

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
