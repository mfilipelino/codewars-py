from codewars.extract_domain_name import domain_name

def test_domain_name_http_only():
    assert domain_name("http://github.com/carbonfive/raygun") == 'github'
    assert domain_name("http://google.com") == "google"
    assert domain_name("http://google.co.jp") == "google"
    assert domain_name("www.xakep.ru") == "xakep"
    assert domain_name("https://youtube.com") == "youtube"
    assert domain_name("google.com") == "google"