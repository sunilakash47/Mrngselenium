from Generic.wait import title_present
from pom2.Loginpage_POM import Login
from pom2.Homepage import Home

def test_TC3(setup):
    driver = setup
    l = Login(driver)
    l.username("admin")
    l.password("manager")
    l.loginbtn()
    title_present(driver, "actiTIME - Enter Time-Track")
    h = Home(driver)
    h.userstab()
    title_present(driver, "actiTIME - User List")
    h.userbtn()
    h.firstname("demo")
    h.lastname("automation")
    h.email("demoauto@gmail.com")
    h.username("demoauto")
    h.password("demo123")
    h.retypepassword("demo123")
    h.createuserbtn()
    h.logout()
    title_present(driver, "actiTIME - Login")


