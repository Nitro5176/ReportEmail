from bs4 import BeautifulSoup
import requests as r


def amd_stocks():
    response = r.get("https://finance.yahoo.com/quote/AMD/")
    soup = BeautifulSoup(response.text, "html.parser")
    string = soup.find("div", class_="D(ib) Mend(20px)")
    string = string.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    string = string.text

    return "\nAmd stocks now: " + str(string)


def amc_stocks():
    response = r.get("https://finance.yahoo.com/quote/AMC/")

    soup = BeautifulSoup(response.text, "html.parser")
    # find a div that has that class name
    string = soup.find("div", class_="D(ib) Mend(20px)")
    # find that span that has the class name
    string = string.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    # After finding a div, and finding a span with the class, we find the text. number
    string = string.text

    return "\nAMC stocks now: " + str(string)
