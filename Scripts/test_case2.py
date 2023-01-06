from pom2.Loginpage_POM import Login


def test_TC2(setup):
    driver = setup
    l = Login(driver)
    l.username("manager")
    l.password("admin")
    l.loginbtn()
    l.errormsg()


