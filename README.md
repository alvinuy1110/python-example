
# Generate PIP requirements

```
pip freeze > requirements.txt
```

## install
```
pip install -r requirements.txt
```


# Running tests

* will be using "unittest"
* ensure it is a python module (i.e. have an __init__.py)

## run all tests
```
cd <project root>
python -m unittest discover -v
```

## Run individual
```
cd <project root>
python -m unittest tests.test_my_sum
```


# Reference 

unittest - https://docs.python.org/3.4/library/unittest.html

