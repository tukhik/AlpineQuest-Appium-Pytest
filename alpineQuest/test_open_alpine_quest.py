from alpineQuest.pages.base_page import BasePage

def test_open_alpine_quest(application):
    base_page = BasePage(application)
    current_activity = application.current_activity
    print(current_activity, '============')
    assert base_page is not None, "The 'Alpine Quest' app has not been launched."
