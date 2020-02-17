# **Variables**

## Variable names should reveal intent

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

## Use meaningful and pronounceable variable names

**Bad:**

```python
ymdstr = datetime.date.today().strftime("%y-%m-%d")
```

**Good**:

```python
current_date: str = datetime.date.today().strftime("%y-%m-%d")
```

## Use the same vocabulary for the same type of variable

**Bad:**
Here we use three different names for the same underlying entity:

```python
get_user_info()
get_client_data()
get_customer_record()
```

**Good**:
If the entity is the same, you should be consistent in referring to it in your functions:

```python
get_user_info()
get_user_data()
get_user_record()
```

## Avoid magic numbers and magic numbers

**Bad:**

```python
# What the heck is 86400 for?
time.sleep(86400);
```

**Good**:

```python
# Extract magic number as a variable
SECONDS_IN_A_DAY = 86400

time.sleep(SECONDS_IN_A_DAY)
```

## Use variables to keep code "DRY" ("Don't Repeat Yourself")

DRY stands for "Don't Repeat Yourself". If you find yourself changing the same thing in multiple places, then that thing which you're changing is a candidate for refactoring.

**Bad:**
Notice how `amount` is duplicated in multiple places. If the column name in the data should change (e.g. to `literally_anything`), then we would need to waste effort in finding and replacing `amount` in multiple places.

```python
loans = loans.fillna({'amount': 0})
loans.groupby(['amount']).mean().sort_values(by='amount')
```

**Good**:
Now, should the `amount` column need to be changed, we can change it in one place:

```python
target_column = 'amount'

loans = loans.fillna({target_column: 0})
loans.groupby([target_column]).mean().sort_values(by=target_column)
```

## Use explanatory variables

**Bad:**

```python
address = 'One Infinite Loop, Cupertino 95014'
city_zip_code_regex = r'^[^,\\]+[,\\\s]+(.+?)\s*(\d{5})?$'
matches = re.match(city_zip_code_regex, address)

save_city_zip_code(matches[1], matches[2])
```

**Not bad**:

It's better, but we are still heavily dependent on regex.

```python
address = 'One Infinite Loop, Cupertino 95014'
city_zip_code_regex = r'^[^,\\]+[,\\\s]+(.+?)\s*(\d{5})?$'
matches = re.match(city_zip_code_regex, address)

city, zip_code = matches.groups()
save_city_zip_code(city, zip_code)
```

**Good**:

Decrease dependence on regex by naming subpatterns.

```python
address = 'One Infinite Loop, Cupertino 95014'
city_zip_code_regex = r'^[^,\\]+[,\\\s]+(?P<city>.+?)\s*(?P<zip_code>\d{5})?$'
matches = re.match(city_zip_code_regex, address)

save_city_zip_code(matches['city'], matches['zip_code'])
```

## Avoid mental mapping

Don’t force the reader of your code to translate what the variable means.
Explicit is better than implicit.

**Bad:**

```python
seq = ('Austin', 'New York', 'San Francisco')

for item in seq:
    do_stuff()
    do_some_other_stuff()
    # ...
    # Wait, what's `item` for again?
    dispatch(item)
```

**Good**:

```python
locations = ('Austin', 'New York', 'San Francisco')

for location in locations:
    do_stuff()
    do_some_other_stuff()
    # ...
    dispatch(location)
```

## Don't add unneeded context

If your class/object name tells you something, don't repeat that in your variable name.

**Bad:**

```python
class Car:
    car_make: str
    car_model: str
    car_color: str

# usage:
car = Car()
car.car_make
car.car_model
car.car_color
```

**Good**:

```python
class Car:
    make: str
    model: str
    color: str

# usage
car = Car()
car.make
car.model
car.color
```
