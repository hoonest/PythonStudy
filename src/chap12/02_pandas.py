# 팬더스와 NumPy를 임포트합니다.
import pandas as pd
import numpy as np

# s에 Series 데이터 타입을 정의합니다.
s = pd.Series(["m","i","l","e", 5, 9, 35, 3.1415])
print(s)

# index 파라미터를 이용해 영어로 인덱스를 설정합니다.
s = pd.Series(["m","i","l","e", 5, 9, 35, 3.1415],
              index=["A","B","Z","X","y","h","i","D"])
print(s)

# 깊이가 1인 딕셔너리를 생성합니다.
heroes_dict = {
    'ana': 200, 'bastion': 300, 'dva': 500,
    'genji': 200, 'hanjo': 200, 'junkrat': 200,
    'lucio': 200, 'macree': 200, 'mei': 250,
    'mercy': 200, 'pharah': 200, 'reaper': 250,
    'reinhardt': 500, 'roadhog': 600, 'soldier76': 200,
    'symmetra': 200, 'torbjorn': 200, 'tracer': 150,
    'widowmaker': 200, 'winston': 500, 'zarya': 400,
    'zenyatta': 200
}

#해당 딕셔너리를 Series 타입으로 변환합니다.
heroes_series = pd.Series(heroes_dict)
print(heroes_series)



# 22개의 행과 4개의 열을 갖는 딕셔너리를 정의합니다.
heroes = {
    "name":[
        'ana', 'bastion', 'dva',
        'genji', 'hanjo', 'junkrat',
        'lucio', 'macree', 'mei',
        'mercy', 'pharah', 'reaper',
        'reinhardt', 'roadhog', 'soldier76',
        'symmetra', 'torbjorn', 'tracer',
        'widowmaker', 'winston', 'zarya',
        'zenyatta'
    ],
    "health":[
        200, 300, 500,
        200, 200, 200,
        200, 200, 250,
        200, 200, 250,
        500, 600, 200,
        200, 200, 150,
        200, 500, 400,
        200
    ],
    "position":[
            "support", "defense", "tank",
            "offense", "defense", "defense",
            "support", "offense", "defense",
            "support", "offense", "offense",
            "tank", "tank", "offense",
            "support", "defense", "offense",
            "defense", "tank", "tank",
            "support"
        ],
    "id":[
        1, 2, 3,
        4, 5, 6,
        7, 8, 9,
        10, 11, 12,
        13, 14, 15,
        16, 17, 18,
        19, 20, 21,
        22
    ]
}

# 딕셔너리를 dataFrame타입으로 변환합니다.
heroes_df = pd.DataFrame(heroes)
print(heroes_df)


# read_csv()를 이용해 CSV 파일을 불러옵니다.
csv_data = pd.read_csv('data/book_list.csv')
#열 제목이 있는 형태로 출력합니다.
print(csv_data.head())

#열 제목을 직접 설정합니다.
columns = ['제목', '저자', '번역자', '출간일', 'isbn']
#열 제목이 없는 csv파일을 불러옵니다.
#인덱스가 없도록 설정한 다음 names 파라미터의 값을 columns로 설정합니다.
csv_data2 = pd.read_csv('data/book_list_headless.csv', header=None, names=columns)

#열 제목이 있는 형태로 5개데이터를 출력합니다.
print(csv_data2.head())

#read_excel()을 이용해 엑셀 파일을 불러옵니다.
# 이때 heroes 시트를 선택하도록 합니다.
# pip install xlrd : 파일 데이터 추출
# pip install openpyxl : 파일 읽거나 저장
heroes_excel = pd.read_excel('data/heroes.xlsx', 'heroes')
#열제목이 있는 형태로 5개 데이터를 출력합니다.
print(heroes_excel.head())





