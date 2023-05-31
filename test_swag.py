from playwright.sync_api import  expect
import pytest

def test_login(page):
    page.goto("/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    

def test_wrong_user(page):
    page.goto("/")
    page.fill("#user-name", "wrong_user")
    page.fill("#password", "secret sauce")
    page.click("#login-button")
    assert page.inner_text("h3") == "Epic sadface: Username and password do not match any user in this service"

def test_wrong_password(page):
    page.goto("/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_password")
    page.click("#login-button")
    assert page.inner_text("h3") == "Epic sadface: Username and password do not match any user in this service"


def test_empty_user(page):
    page.goto("/")
    page.fill("#user-name", "")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert page.inner_text("h3") == "Epic sadface: Username is required"


def test_empty_password(page):
    page.goto("/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "")
    page.click("#login-button")
    assert page.inner_text("h3") == "Epic sadface: Password is required"

def test_empty_user_password(page):
    page.goto("/")
    page.fill("#user-name", "")
    page.fill("#password", "")
    page.click("#login-button")
    assert page.inner_text("h3") == "Epic sadface: Username is required"


'''def test_locked_out_user(page):
    page.goto("/")
    page.fill("#user-name", "locked_out_user")
    page.fill("#password", "secret sauce")
    page.click("#login-button")
    assert page.inner_text("h3") == "Epic sadface: Sorry, this user has been locked out."'''


def test_sorting_button(page):
    page.goto("/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    
    page.get_by_role("combobox").select_option("za")
    assert page.inner_text(".active_option") == "Name (Z to A)"

    page.get_by_role("combobox").select_option("lohi")
    assert page.inner_text(".active_option") == "Price (low to high)"

    page.get_by_role("combobox").select_option("hilo")
    assert page.inner_text(".active_option") == "Price (high to low)"

    page.get_by_role("combobox").select_option("az")
    assert page.inner_text(".active_option") == "Name (A to Z)"


def test_order(page):
    page.goto("/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.click("#add-to-cart-sauce-labs-backpack")
    page.click("#add-to-cart-sauce-labs-bolt-t-shirt")
    page.click("#add-to-cart-sauce-labs-onesie")
  
    assert page.inner_text(".shopping_cart_badge") == "3"

    page.click("#shopping_cart_container")
    page.click("#checkout")

    page.click("#continue")
    assert page.inner_text("h3") == "Error: First Name is required"


    page.fill("#first-name", "Stanomir")
    page.click("#continue")
    assert page.inner_text("h3") == "Error: Last Name is required"
 

    page.fill("#last-name", "Zajebant")
    page.click("#continue")
    assert page.inner_text("h3") == "Error: Postal Code is required"


    page.fill("#postal-code", "12345")
    page.click("#continue")

    page.click("#finish")
    page.click("#back-to-products")
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_select_all(page):
    page.goto("/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")


    page.click("#add-to-cart-sauce-labs-backpack")
    page.click("#add-to-cart-sauce-labs-bolt-t-shirt")
    page.click("#add-to-cart-sauce-labs-onesie")
    page.click("#add-to-cart-sauce-labs-fleece-jacket")
    page.click("#add-to-cart-sauce-labs-bike-light")
  #  page.click("#add-to-cart-test.allthethings()-t-shirt-(red)")
    page.click("text= Sauce Labs Backpack")
    page.click("#back-to-products")
    page.click("#react-burger-menu-btn")
    page.click("#logout_sidebar_link")

def test_links_check(page):
    page.goto("/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    page.click("text = Twitter")
    #assert page.url == "https://twitter.com/saucelabs"
    

    page.click("text = Facebook")
   # assert page.url == "https://www.facebook.com/saucelabs"

    page.click("text = LinkedIn")
   # assert page.url == "https://www.linkedin.com/company/sauce-labs/"
