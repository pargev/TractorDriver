

# About
TractorDriver is an end-to-end test framework for Angular and AngularJS applications. With TractorDriver you can run Python tests with extended functionality which provides  [Protractor](https://www.protractortest.org/). TractorDriver supports Angular-specific locator strategies, which allows you to test Angular-specific elements. TractorDriver uses scripts with some modifications provided by protractor and added a lot of useful staff for test engineers who prefers Python tests.

TractorDriver is built on top of Selenium WebDriver, which uses native events and browser-specific drivers. When you use TractorDriver You no longer need to add waits and sleeps to your test. so you don’t have to worry about waiting for your test and webpage to sync.

TractorDriver is tested with Python 3.6 and 3.7 by using pytest.
No need to download any webdriver and put it in some path. Tracktor driver and webdrivermanager will automatically do it.


# Installation

You can install TractorDriver by one single command. 
`pip install tractordriver`

or do it manually with downloading the repository and installing it by the following command:

`python setup.py instasll`

# Usage
```python
from tractordriver import webdriver
driver = webdriver.Chrome()
```

You do not need to download any webdriver file or install anything. TractorDriver will download and install it automatically. Learn more [here](https://github.com/rasjani/webdrivermanager).
By default it will download and run the latest webdrivers. You can specify a specific versions if you wish.
```python
driver = webdriver.Chrome(version=SOME_VERSION)

```
TractorDriver supports all kind of webdrivers
```
    driver = webdriver.Chrome()
    driver = webdriver.Firefox()
    driver = webdriver.Safari()
    driver = webdriver.Ie()
    driver = webdriver.Edge()
    driver = webdriver.Opera()
    driver = webdriver.BlackBerry()
    driver = webdriver.PhantomJS()
    driver = webdriver.Android()
    driver = webdriver.WebKitGTK()
    driver = webdriver.Remote()
```

# Finding Element(s)
The find_element or find_elements method accepts 4 arguments.
- By
- Value
- auto wait
- timeout
**By default the auto_wait is True. The program will wait until the selected element becomes visible during the timeout perios.  So you don't need to add additional waits in your code. **

```python
from tractordriver import webdriver
from TractorScripts import By

driver = webdriver.Chrome()
element = driver.find_element(By.MODEL, "MODEL NAME")
element = driver.find_elements(By.MODEL, "MODEL NAME")
element = driver.find_element_by_model("MODEL NAME")
element = driver.find_elements_by_model("MODEL NAME")

```

## Model

Find an element by ng-model expression.

Example
```html
<input type="text" ng-model="SomeModelName">
```
Code
```python
element = driver.find_element(By.MODEL, "MODEL NAME")
or
element = driver.find_element_by_model("MODEL NAME")

```

## Binding
Find an element by text binding. Does a partial match, so any elements bound to variables containing the input string will be returned.

Note: For AngularJS version 1.2, the interpolation brackets, (usually {{}}), are optionally allowed in the binding description string. For Angular version 1.3+, they are not allowed, and no elements will be found if they are used.

Example
```html
<span>{{some.name}}</span>
<span ng-bind="some.email"></span>
```
```python
element = driver.find_element(By.BINDING, "some.name")
```
or
```python
element = driver.find_element_by_binding("some.email")
```

## Repeater rows
Find elements inside an ng-repeat.

Example
```html
<div ng-repeat="person in people">
  <span>{{person.name}}</span>
  <span>{{person.age}}</span>
</div>

<div class="car-img" ng-repeat-start="car in cars">
  <span>{{$index}}</span>
</div>
<div class="car-info" ng-repeat-end>
  <h4>{{car.name}}</h4>
  <p>{{car.make}}</p>
</div>
```
```python
element = driver.find_elements(By.REPEATER_ROWS, "person in people")
```
or
```python
element = driver.find_element_by_repeater_rows("car in cars")
```

## Options

Find an element by ng-options expression.

```html
<select ng-model="color" ng-options="c for c in colors">
  <option value="0" selected="selected">red</option>
  <option value="1">green</option>
</select>
```

```python
element = driver.find_elements_by_option("c for c in colors")
```

## find element by option and value
Documentation is comig soon

## find_elements_by_button_text
Documentation is comig soon


##  find_elements_by_partial_button_text
Documentation is comig soon


## find_all_repeater_rows
Documentation is comig soon

## find_all_repeater_rows_by_value
Documentation is comig soon

## find_repeater_row_by_value
Documentation is comig soon


## find_all_repeater_column
Documentation is comig soon

## find_element_by_css_containing_text
Documentation is comig soon

# Web Element Methods

## Click and JS Click, mousedown
Documentation is comig soon

## Wait, Wait status, Wait Visible, Wait Invisible
Documentation is comig soon

## is element enabled, or disabled
Documentation is comig soon

## submit
Documentation is comig soon

## Double Click
Documentation is comig soon

## Selecting and deselecting elements
Documentation is comig soon

## getting, setting nd removing js attributes 
Documentation is comig soon

## get value, get text, get raw text get ng_text
Documentation is comig soon

## Trigger event
Documentation is comig soon

## Scroll into view
Documentation is comig soon

## Control properties
Documentation is comig soon









