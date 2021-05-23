from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import base64
import cv2 as cv
import numpy as np
from time import sleep


def grab(img_base64):
    img_base64 = img_base64.split('base64,')[1]
    image_bytes = base64.b64decode(img_base64)

    image_np = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv.imdecode(image_np, flags=2)
    return image

options= Options()
options.headless= True

print('loading Firefox...')
driver= webdriver.Firefox(options= options, executable_path="./geckodriver")

print('open worldview.earthdata.nasa.gov...')
driver.get('https://worldview.earthdata.nasa.gov/?v=-307.69227075855747,-172.79143899276977,265.9895122383497,150.24604119477436&l=MODIS_Combined_Thermal_Anomalies_All,Reference_Labels_15m(hidden),Reference_Features_15m(hidden),Coastlines_15m,VIIRS_NOAA20_CorrectedReflectance_TrueColor(hidden),VIIRS_SNPP_CorrectedReflectance_TrueColor(hidden),MODIS_Aqua_CorrectedReflectance_TrueColor(hidden),MODIS_Terra_CorrectedReflectance_TrueColor(hidden)&lg=true&t=2021-05-23-T15%3A25%3A19Z')
print('sleep...')
sleep(3)
xpath_coastlines= '/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div[1]/canvas'
xpath_fires= '/html/body/div[1]/div/div[4]/div[1]/div/div[1]/div[2]/canvas'

print('get coastlines')
base64_coastlines= driver.execute_script(f"""
        var canvas = document.evaluate('{xpath_coastlines}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        var img_data = canvas.toDataURL();
        return img_data;
    """)
coastlines= grab(base64_coastlines)

print('get fires')
base64_fires= driver.execute_script(f"""
        var canvas = document.evaluate('{xpath_fires}', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        var img_data = canvas.toDataURL();
        return img_data;
    """)
fires= grab(base64_fires)

combined= cv.add(coastlines, fires)
cv.imwrite('sat_pic.png', combined)

print('done')
cv.waitKey(0)



