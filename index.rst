**Table of Contents**

\[TOCM\]

\[TOC\]

About
=====

TractorDriver is an end-to-end test framework for Angular and AngularJS
applications. With TractorDriver you can run Python tests with extended
functionality which provides [Protractor]. TractorDriver supports
Angular-specific locator strategies, which allows you to test
Angular-specific elements. TractorDriver uses scripts with some
modifications provided by protractor and added a lot of useful staff for
test engineers who prefers Python tests.

TractorDriver is built on top of Selenium WebDriver, which uses native
events and browser-specific drivers. When you use TractorDriver You no
longer need to add waits and sleeps to your test. so you don’t have to
worry about waiting for your test and webpage to sync.

TractorDriver is tested with Python 3.6 and 3.7 by using pytest. No need
to download any webdriver and put it in some path. Tracktor driver and
webdrivermanager will automatically do it.

Installation
============

You can install TractorDriver by one single command.
`pip install tractordriver`

or do it manually with downloading the repository and installing it by
the following command:

`python setup.py instasll`

Usage
=====

    from tractordriver import webdriver
    driver = webdriver.Chrome()

You do not need to download any webdriver file or install anything.
TractorDriver will download and install it automatically. Learn more
[here]. By default it will download and run the latest webdrivers. You
can specify a specific versions if you wish.

    driver = webdriver.Chrome(version=SOME_VERSION)

TractorDriver supports all kind of webdrivers

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

Finding Element(s)
==================

The find\_element or find\_elements method accepts 4 arguments. - By -
Value - auto wait - timeout **By default the auto\_wait is True. The
program will wait until the selected element becomes visible during the
timeout perios. So you don’t need to add additional waits in your code.
**

    from tractordriver import webdriver
    from TractorScripts import By

    driver = webdriver.Chrome()
    element = driver.find_element(By.MODEL, "MODEL NAME")
    element = driver.find_elements(By.MODEL, "MODEL NAME")
    element = driver.find_element_by_model("MODEL NAME")
    element = driver.find_elements_by_model("MODEL NAME")

Model
-----

Find an element by ng-model expression.

Example

    <input type="text" ng-model="SomeModelName">

Code

    element = driver.find_element(By.MODEL, "MODEL NAME")
    or
    element = driver.find_element_by_model("MODEL NAME")

Binding
-------

Find an element by text binding. Doe

  [Protractor]: https://www.protractortest.org/
  [here]: https://github.com/rasjani/webdrivermanager