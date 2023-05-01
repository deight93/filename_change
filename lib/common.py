import pytesseract
import cv2
import os
import json
import re
import shutil

def change_name(dir:str, new_path:str, temp:int):
    for i in os.listdir(dir):
        img=cv2.imread(dir+"/"+i, cv2.IMREAD_COLOR)
        result = pytesseract.image_to_string(img, lang='eng+kor').split()

        with open(os.getcwd()+"/setting"+"/setting.json", "r", encoding='UTF8') as file:
            setting = json.load(file)
            if temp == 0:
                setting["2"]['value'] = setting["2"]['parse'][0]
            else:
                setting["2"]['value'] = setting["2"]['parse'][1]
        
        set_num = [setting[i]['value'] for i in setting]
        for k, v in enumerate(result):
            if re.match(setting['1']['value'], v) and result[k-1] == "상세":
                set1 = v.split(setting['1']['parse'][0])
                set1 = "".join([set1[j] for j in setting['1']['parse'][1:]])
                set_num[1] = set1
            if re.match(setting['3']['value'], v) and result[k+1] == "-":
                set3 = v.split(setting['3']['parse'][0])
                set3 = "".join([set3[j] for j in setting['3']['parse'][1:]])
                set_num[3] = set3
            if re.match(setting['5']['value'], v) and result[k-1] == "-":
                set5 = v.split(setting['5']['parse'][0])
                set5 = "".join([set5[j] for j in setting['5']['parse'][1:]])
                set_num[5] = set5
        
        shutil.copy(dir+"/"+i, new_path)
        new_file_name = "".join(set_num)
        os.rename(new_path+"/"+i, new_path+"/"+new_file_name+"."+i.split(".")[1])
