from datetime import datetime, timedelta, timezone
import slackweb

places = ["【学生支援センター】", "【工学部8号館】", "【本部棟】", "【経済学研究棟】", "【病院・管理・研究棟】"]

# [mon, tue, wed, thu, fri]
groupA = ["ビストロカルロス(ビーフステーキライス、ハーブチキンライス)", "Comida Latina(タコライス)", "PINOS(グリルチキン丼、ビーフステーキ丼)", "てふてふ(ムーデン、てふてふ)", "グリーンスペイン(パエリアランチBOX)"]
groupB = ["Jule's spices(甘辛丼、ナシゴレン)", "ROCKET CHICKEN(ロケットチキン)", "フレーミングノラ(ガパオライス、グリーンカレー)", "エジプトめしコシャリ屋さん(コシャリ)", "オリーブ亭(オムライス)"]
groupC = ["Caffe Latte(イタリアご飯4種盛り)", "Dudes(テリヤキチキン丼、デミチキ)", "ミラーン(南インドカレー各種)", "パパガヤデリ(ファラフェル、シュニッツェル)", "栄屋(横手やきそば)"]
groupD = ["Mr.Chicken(シンガポールチキンライス)", "TOKYO PAELLA(週替りパエリア)", "MOCHIKO chicken factory(モチコチキン)", "デリキムチ(プルコギ、タッカルビ、カルビクッパ)", "NAOCAFE(スパム丼、男前ハワイ丼)"]
groupE = ["火の鳥食堂(ハヤシライス)", "GRILL TOKYO(ローストビーフ、グリルチキン)", "カリフォルニアカフェ フラワーズ(ケイジャンチキン、BBQライス)", "CHERIE(ハイチ料理)", "＋Spice(インドカレー(ナン/ライス))"]

weeks = [
  [groupD, groupE, groupA, groupB, groupC],
  [groupE, groupA, groupB, groupC, groupD],
  [groupA, groupB, groupC, groupD, groupE],
  [groupB, groupC, groupD, groupE, groupA],
  [groupC, groupD, groupE, groupA, groupB],
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