from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pandas as pd

# Selenium 세팅
options = Options()
options.headless = True  # headless 모드
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 국가들
countries = ['algeria', 'argentina', 'armenia', 'australia', 'austria', 'azerbaijan', 'bahrain',
'bangladesh', 'belarus', 'belgium', 'bosnia-and-herzegovina', 'brazil', 'bulgaria',
'cambodia', 'canada', 'chile', 'colombia', 'costa-rica', 'croatia', 'czech-republic',
'denmark', 'dominican-republic', 'ecuador', 'egypt', 'el-salvador', 'finland', 'france',
'germany', 'ghana', 'greece', 'guatemala', 'honduras', 'hong-kong', 'hungary', 'india',
'indonesia', 'ireland', 'israel', 'italy', 'jamaica', 'japan', 'jordan', 'kazakhstan',
'kenya', 'korea-republic-of', 'kuwait', 'kyrgyzstan', 'latvia', 'lithuania',
'macedonia-the-former-yugoslav-republic-of', 'malaysia', 'mexico', 'moldova-republic-of', 'morocco',
'nepal', 'netherlands', 'new-zealand', 'nigeria', 'norway', 'oman', 'pakistan', 'panama',
'paraguay', 'peru', 'philippines', 'poland', 'portugal', 'puerto-rico', 'qatar', 'romania',
'russian-federation', 'saudi-arabia', 'serbia', 'singapore', 'slovakia', 'slovenia', 'south-africa',
'spain', 'sri-lanka', 'sweden', 'switzerland', 'taiwan', 'tanzania-united-republic-of',
'thailand', 'trinidad-and-tobago', 'tunisia', 'turkey', 'ukraine', 'united-arab-emirates',
'united-kingdom', 'united-states', 'uruguay', 'uzbekistan', 'venezuela-bolivarian-republic-of', 'vietnam']

for country in countries:
    url = f'https://www.similarweb.com/top-apps/google/{country}'
    driver.get(url)
    time.sleep(5)  # js 기다림
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    app_rows = soup.select('.top-table__body .top-table__row')
    print(f'국가: {country}')
    data = []
    if not app_rows:
        print("데이터 없음")
    else:
        for row in app_rows:
            app_name = row.select_one('.top-table__column--app .ta-table__compare .ta-table__name').get_text(strip=True)
            category = row.select_one('.top-table__column--category .ta-table__category').get_text(strip=True)
            data.append({'App 이름': app_name, '카테고리': category})
            print('App 이름:', app_name, '카테고리:', category)
        # csv로 저장하기
        df = pd.DataFrame(data)
        df.to_csv(f'{country}_apps.csv', index=False)
        print(f'{country}_apps.csv 파일 저장됨')
    print('---')

driver.quit()
