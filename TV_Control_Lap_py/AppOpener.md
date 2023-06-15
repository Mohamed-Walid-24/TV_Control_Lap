# AppOpener

   [Documentation](https://pypi.org/project/appopener/)

> AppOpener is the python library to open any application.

## Installation

```cmd
pip install appopener
```

---

## Importing

```python
import AppOpener
```

- You should start your python code with this line to get access to all library features 

--- 

## Features

### 1] AppOpener.open

```python
AppOpener.open("settings")
```

- Open the written AppName `settings`

> ###### Example
> 
> ```python
> import AppOpener
> AppOpener.open("settings")
> ```

---

### 2] AppOpener.give_appnames

```python
AppOpener.give_appnames()
```

- Get all the valid app names, so you can use it in the previous function

> ###### Example
> 
> ```python
> import AppOpener
> 
> AppNames = list(AppOpener.give_appnames())
> AppNames.sort()
> 
> print(AppNames)
> ```
> 
> ![](https://github.com/Mohamed-Walid-24/TVControlLap/blob/main/Pics/AppNames.png?raw=true)
> 
> - `list` change output to a list to easily work with
> 
> - `sort` list function for sorting alphabetically if working with strings

---

### 3] AppOpener.mklist

```python
AppOpener.mklist()
```

- Create a json file containing AppNames and Appids

--- 
