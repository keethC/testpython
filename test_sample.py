def test_browser_and_url(browser, url):
    print(f"Browser: {browser}")
    print(f"URL: {url}")
    assert "http" in url
