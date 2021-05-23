from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options= Options()
options.headless= True

driver= webdriver.Firefox(options= options, executable_path="./geckodriver")

driver.get('https://worldview.earthdata.nasa.gov/?v=-307.69227075855747,-172.79143899276977,265.9895122383497,150.24604119477436&t=2021-05-23-T15%3A25%3A19Z')

xpath_coastlines= '/html/body/div[1]/div/div[3]/div[1]/div/div[1]/div/canvas'
xpath_fires= ''

base64_coastlines= driver.execute_script(f"""
        var canvas = document.evaluate('{xpath_coastlines}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        var img_data = canvas.toDataURL();
        return img_data;
    """)


