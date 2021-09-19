def domain_name(url):
    """
    Extract the domain name for the url
    :param url:
    :return:
    """
    return (
        url.replace("https://", "")
        .replace("http://", "")
        .replace("www.", "")
        .split(".")[0]
    )
