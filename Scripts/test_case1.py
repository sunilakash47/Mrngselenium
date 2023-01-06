from pom2.Loginpage_POM import Login
from Generic.wait import *


def test_TC1(setup):
    driver = setup
    l = Login(driver)
    l.username("admin")
    l.password("manager")
    l.loginbtn()
    title_present(driver, "actiTIME - Enter Time-Track")


"""
framework architecure explination
=================================
3package
   generic pom scripts
   generic : reading excel, take scrshot, loading decorato,
     verification of title, error, assertion
   pom : each webpage we are developing single module with web page name and 
       we will deleove POM class and name as webpage without test keyword
           1.intialization
           2.decalrtion and utilization
   scripts:
       confest module - before executing all test_function conftest
       each and evert test case writing in separate module with test keyword and
       test function with testcase id(test_AC231)
       we have used parameterzed marker to pass data into test function
3directory
  defect   excel   drivers    reports
  
what is ur responsablity in framewok/contribution towards framework
====================================================================
*i have involved in writing pOM class for each web page
*i have involved in writing scripts/converting manual testcase into automation scripts ny using pytest
*i have involved execution 
*i have involed in genearting pytest report of my executed test case
*i haved mainiting automation scripts

to genetare report in specific folder
pytest -vs --html="../Reports/reportname.html"
"""


