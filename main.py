from datetime import datetime, timedelta, timezone

# 1: mon, 2: tue, 3: wed, 4:thu, 5:fri
groupA = {"1": "ビストロカルロス(ビーフステーキライス、ハーブチキンライス)", "2": "Comida Latina(タコライス)", "3": "PINOS(グリルチキン丼、ビーフステーキ丼)", "4": "てふてふ(ムーデン、てふてふ)", "5": "グリーンスペイン(パエリアランチBOX)"}
groupB = {"1": "Jule's spices(甘辛丼、ナシゴレン)", "2": "ROCKET CHICKEN(ロケットチキン)", "3": "フレーミングノラ(ガパオライス、グリーンカレー)", "4": "エジプトめしコシャリ屋さん(コシャリ)", "5": "オリーブ亭(オムライス)"}
groupC = {"1": "Caffe Latte(イタリアご飯4種盛り)", "2": "Dudes(テリヤキチキン丼、デミチキ)", "3": "ミラーン(南インドカレー各種)", "4": "パパガヤデリ(ファラフェル、シュニッツェル)", "5": "栄屋(横手やきそば)"}
groupD = {"1": "Mr.Chicken(シンガポールチキンライス)", "2": "TOKYO PAELLA(週替りパエリア)", "3": "MOCHIKO chicken factory(モチコチキン)", "4": "デリキムチ(プルコギ、タッカルビ、カルビクッパ)", "5": "NAOCAFE(スパム丼、男前ハワイ丼)"}
groupE = {"1": "火の鳥食堂(ハヤシライス)", "2": "GRILL TOKYO(ローストビーフ、グリルチキン)", "3": "カリフォルニアカフェ フラワーズ(ケイジャンチキン、BBQライス)", "4": "CHERIE(ハイチ料理)", "5": "+Spice(インドカレー(ナン/ライス))"}

place1 = "【学生支援センター】"
place2 = "【工学部8号館】"
place3 = "【本部棟】"
place4 = "【経済学研究棟】"
place5 = "【病院・管理・研究棟】"

week0 = {1: groupD, 2: groupE, 3: groupA, 4: groupB, 5: groupC}
week1 = {1: groupE, 2: groupA, 3: groupB, 4: groupC, 5: groupD}
week2 = {1: groupA, 2: groupB, 3: groupC, 4: groupD, 5: groupE}
week3 = {1: groupB, 2: groupC, 3: groupD, 4: groupE, 5: groupA}
week4 = {1: groupC, 2: groupD, 3: groupE, 4: groupA, 5: groupB}

# タイムゾーンの生成
JST = timezone(timedelta(hours=+9), "JST")

today = datetime.now(JST)
# today = datetime(2021, 2, 1, tzinfo=JST)
weeknumber = today.isocalendar()

this_week_number = weeknumber[1] % 5
this_day_number = str(weeknumber[2])

if this_day_number == "6" or this_day_number == "7":
  print("お休み")
else:
  if this_week_number == 0:
    print(place1 + week0[1][this_day_number] + "、" + place2 + week0[2][this_day_number] + "、" + place3 + week0[3][this_day_number] + "、" + place4 + week0[4][this_day_number] + "、" + place5 + week0[5][this_day_number])
  elif this_week_number == 1:
    print(place1 + week1[1][this_day_number] + "、" + place2 + week1[2][this_day_number] + "、" + place3 + week1[3][this_day_number] + "、" + place4 + week1[4][this_day_number] + "、" + place5 + week1[5][this_day_number])
  elif this_week_number == 2:
    print(place1 + week2[1][this_day_number] + "、" + place2 + week2[2][this_day_number] + "、" + place3 + week2[3][this_day_number] + "、" + place4 + week2[4][this_day_number] + "、" + place5 + week2[5][this_day_number])
  elif this_week_number == 3:
    print(place1 + week3[1][this_day_number] + "、" + place2 + week3[2][this_day_number] + "、" + place3 + week3[3][this_day_number] + "、" + place4 + week3[4][this_day_number] + "、" + place5 + week3[5][this_day_number])
  elif this_week_number == 4:
    print(place1 + week4[1][this_day_number] + "、" + place2 + week4[2][this_day_number] + "、" + place3 + week4[3][this_day_number] + "、" + place4 + week4[4][this_day_number] + "、" + place5 + week4[5][this_day_number])
