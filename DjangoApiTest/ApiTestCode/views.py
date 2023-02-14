from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import datetime
import pandas as pd
import plotly.express as ptx
import matplotlib.pyplot as plt

def Curves(request):
    curve1 = {datetime.date(2019, 9, 25): -0.00466409748080834, datetime.date(2019, 10, 2): -0.004664280020498285, datetime.date(2019, 10, 18): -0.004698021218080331, datetime.date(2019, 11, 18): -0.00460670858152141, datetime.date(2019, 12, 18): -0.004592056380061808, datetime.date(2020, 1, 20): -0.0046585378376474175, datetime.date(2020, 2, 18): -0.004718536457197049, datetime.date(2020, 3, 18): -0.004769786756021426, datetime.date(2020, 4, 20): -0.004874746470445734, datetime.date(2020, 5, 18): -0.004935401549416456, datetime.date(2020, 6, 18): -0.005018516837404588, datetime.date(2020, 7, 20): -0.00510789388408658, datetime.date(2020, 8, 18): -0.00517499848814673, datetime.date(2020, 9, 18): -0.005232141141046573, datetime.date(2021, 3, 18): -0.0055295057033356776, datetime.date(2021, 9, 20): -0.005680297450665653, datetime.date(2022, 3, 18): -0.005757382500003766, datetime.date(2022, 9, 19): -0.00574686350887154, datetime.date(2023, 9, 18): -0.005651736542643933, datetime.date(2024, 9, 18): -0.005341700616949887, datetime.date(2025, 9, 18): -0.00483604612961748, datetime.date(2026, 9, 18): -0.00429144904348859, datetime.date(2027, 9, 20): -0.0035845817027494154, datetime.date(2028, 9, 18): -0.0029161548614790394, datetime.date(2029, 9, 18): -0.0022558630111570457, datetime.date(2030, 9, 18): -0.001626935601694614, datetime.date(2031, 9, 18): -0.0009997935123168928, datetime.date(2034, 9, 18): 0.0006194403258350283, datetime.date(2039, 9, 19): 0.002154218568495939, datetime.date(2044, 9, 19): 0.0027303358455033778, datetime.date(2049, 9, 20): 0.002940880176923635, datetime.date(2054, 9, 18): 0.0027967605652070428, datetime.date(2059, 9, 18): 0.002601493834845569, datetime.date(2069, 9, 18): 0.002280671073090913}
    curve2 = {datetime.date(2019, 11, 18): -0.0046453880942072855, datetime.date(2019, 12, 18): -0.00457825971142517, datetime.date(2020, 1, 20): -0.004666725034804451, datetime.date(2020, 2, 18): -0.0047833199670820285, datetime.date(2020, 3, 18): -0.004801365649370856, datetime.date(2020, 4, 20): -0.004935425825643432, datetime.date(2020, 5, 18): -0.00491982757513074, datetime.date(2020, 6, 18): -0.00501238301126456, datetime.date(2020, 7, 20): -0.005135338429462258, datetime.date(2020, 8, 18): -0.005201183712231305, datetime.date(2020, 9, 18): -0.00520741202645822, datetime.date(2020, 12, 18): -0.0055893055793215865, datetime.date(2021, 3, 18): -0.005434909592871408, datetime.date(2021, 6, 18): -0.00568773821904882, datetime.date(2021, 9, 20): -0.005565800801370585, datetime.date(2022, 9, 19): -0.005472235478186272, datetime.date(2023, 9, 18): -0.005302289681747808, datetime.date(2024, 9, 18): -0.004903556589564554, datetime.date(2025, 9, 18): -0.004397907034476121, datetime.date(2026, 9, 18): -0.0037923305700211084, datetime.date(2027, 9, 20): -0.0031403775635564816, datetime.date(2028, 9, 18): -0.002446188493265599, datetime.date(2029, 9, 18): -0.0017856553631288086, datetime.date(2031, 9, 18): -0.0004776972951790307, datetime.date(2034, 9, 18): 0.0011281714496101782, datetime.date(2039, 9, 19): 0.0027439284855105173, datetime.date(2044, 9, 19): 0.003234848718656888, datetime.date(2049, 9, 20): 0.0033711988285778875}
    plt.plot(curve1.keys(), curve1.values())
    plt.plot(curve2.keys(), curve2.values())
    showfigure = plt.show()
    return render(request, "ApiTest.html", {showfigure})
    pass

def Unis(request):
    response = requests.get('http://universities.hipolabs.com/search?country=Netherlands')
    Unis = response.json()
    print(Unis)    

    return render(request, "universities.html", {'universities': Unis})
    pass

