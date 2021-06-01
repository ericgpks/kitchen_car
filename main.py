from datetime import datetime, timedelta, timezone
import slackweb

places = ["【学生支援センター】", "【工学部8号館】", "【本部棟】", "【経済学研究棟】", "【病院・管理・研究棟】"]

# [mon, tue, wed, thu, fri]
groupA = ["DIG UP KITCHEN(ファラフェルオーバーライス、チキンオーバーライス)", "Comida Latina(タコライス)", "PINOS(グリルチキン丼、ビーフステーキ丼)", "デリキムチ(プルコギ、タッカルビ、カルビクッパ)", "＋Spice(インドカレー(ナン/ライス))"]
groupB = ["ビストロカルロス(ビーフステーキライス、ハーブチキンライス)", "ROCKET CHICKEN(ロケットチキン)", "カリフォルニアカフェ フラワーズ(ケイジャンチキン、BBQライス)", "てふてふ(ムーデン、てふてふ)", "オリーブ亭(オムライス)"]
groupC = ["Jule's spices(甘辛丼、ナシゴレン)", "TOKYO PAELLA(週替りパエリア)", "フレーミングノラ(ガパオライス、グリーンカレー)", "パパガヤデリ(ファラフェル、シュニッツェル)", "NAOCAFE(スパム丼、男前ハワイ丼)"]
groupD = ["Mr.Chicken(シンガポールチキンライス)", "GRILL TOKYO(ローストビーフ、グリルチキン)", "ミラーン(南インドカレー各種)", "street farm kitchen(タイスタイルBBQ、タイスタイルローストポーク)", "栄屋(横手やきそば)"]
groupE = ["Caffe Latte(イタリアご飯4種盛り)", "Dudes(テリヤキチキン丼、デミチキ)", "MOCHIKO chicken factory(モチコチキン)", "CHERIE(ハイチ料理)", "グリーンスペイン(パエリアランチBOX)"]

# 2021年のISO暦ではこの順番になっている
weeks = [
  [groupC, groupD, groupE, groupA, groupB],
  [groupD, groupE, groupA, groupB, groupC],
  [groupE, groupA, groupB, groupC, groupD],
  [groupA, groupB, groupC, groupD, groupE],
  [groupB, groupC, groupD, groupE, groupA]
]

# タイムゾーンの生成
JST = timezone(timedelta(hours=+9), "JST")

today = datetime.now(JST)
# today = datetime(2021, 3, 8, tzinfo=JST)
weeknumber = today.isocalendar()

this_week_number = weeknumber[1] % 5
this_day_number = weeknumber[2] # 1: mon, 2: tue, 3: wed, 4:thu, 5:fri, 6:sat, 7:sun

# sat or sun
if this_day_number == 6 or this_day_number == 7:
  text = "お休み"
else:
  groups = weeks[this_week_number]
  text = "\n".join([places[i] + groups[i][this_day_number - 1] for i in range(5)])

# slack.notify(text="今日のお昼〜〜〜〜\n" + text)
# print(text)