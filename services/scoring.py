from typing import List, Dict
from datetime  import time
from datetime import datetime , timedelta
import math
import re

#Min-Max正規化(評価指数を0〜１にするため)
def min_max(value, min_value, max_value):
    if max_value == min_value: #割り切れない時
        return 0.0
    return (value - min_value) / (max_value - min_value)

# user_genre: str, #選択ジャンル
#     keywords: List[str] = [], #推測キーワード
#     mode: str = "base", #ジャンル推定と好み推定モードがある
#    eta: datetime = None #時間

#お店の評価関数
def score_shops(
    shop_list: List[Dict], #複数のお店の情報
) -> List[Dict]: #お店のリスト情報を返す
    
    #特徴量の取得
    distances = [shop.get("distance") or 0 for shop in shop_list] #各距離
    ratings = [shop.get("rating") or 0 for shop in shop_list] #各お店の評価
    #レビュー数（差が出過ぎるためlogスケーリングで緩やかに）
    log_reviews = [math.log(1 + (shop.get("user_ratings_total") or 0)) for shop in shop_list]

    #数値を正規化
    min_dist, max_dist = min(distances), max(distances) #距離
    min_rating, max_rating = min(ratings), max(ratings) #評価
    max_log_review = max(log_reviews) if log_reviews else 1 #レビュー数のminは0のため不要
    
    score_shops = []

    # 各お店を評価
    for shop in shop_list:
        #各評価指数を0〜1に
        distance_score = min_max(shop.get("distance") or 0, min_dist, max_dist)
        rating_score = min_max(shop.get("rating") or 0, min_rating, max_rating)
        #minがないため関数を使わず計算
        log_review = math.log(1 + (shop.get("user_ratings_total") or 0))
        review_score = log_review / max_log_review

        #現在営業中かどうかを取得
        is_open = shop.get("opening_hours",{}).get("open_now",True)

        #評価の重みを設定
        if not is_open:
            score = 0.0
        else:
            score = (
                -0.5 * distance_score +
                0.7 * rating_score +
                0.3 * review_score
            )

        #スコアをお店ごとに追加
        shop["score"] = round(score, 2) #小数点第2位までに
        score_shops.append(shop)

    #評価が高い順にソート
    score_shops.sort(key=lambda x: x["score"], reverse=True)

    return score_shops

#営業時間が残り１時間半あるかを判定する関数
def is_closing_soon(business_hours , end_tm , shop) -> bool:
    try:
        #現在の日付を取得
        now = datetime.now()
        today = now.date() 

        weekday_index = now.weekday() #現在の曜日

        #今日の営業時間を抽出
        today_schedule = business_hours[weekday_index]

        #時間帯部分を抜き出す
        parts = today_schedule.split(":",1)
        time_ranges = parts[1].split(",")

        end_tm = datetime.strptime(end_tm, "%H:%M").time()

        #営業時間が２つに分かれてる場合も対応するため
        for time_renge in time_ranges:
            match = re.match(r"(\d{1,2})時(\d{2})分～(\d{1,2})時(\d{2})分", time_renge.strip())

            h1, m1, h2, m2 = map(int, match.groups())

            start = time(h1,m1)
            end = time(h2,m2)

            shop["start_hours"] += str(start.strftime("%H:%M"))
            shop["end_hours"] += str(end.strftime("%H:%M"))

            end_shop = datetime.combine(today,end)

            end_tm = datetime.combine(today,end_tm)

            if end_shop < now:
                end_shop += timedelta(days=1)
            
            if now + timedelta(minutes=90) <= end_shop and end_tm <= end_shop:
                return True
    except:
        return False


    return False

#details後の評価関数
def score_details_shops(
        shop_list: List[Dict],
        time
) -> List[Dict]:
    
    shop_list = score_shops(shop_list)

    shops_score = []

    #各お店を取得
    for shop in shop_list:
        #営業時間に関する情報のみ抽出
        business_hours = shop.get("current_opening_hours", {}).get("weekday_text", {})
        shop_score = shop.get("score")

        shop["start_hours"] = ""
        shop["end_hours"] = ""

        if  not is_closing_soon(business_hours,time,shop):
            shop_score = 0

        #スコアをお店ごとに追加
        shop["score"] = round(shop_score, 2) #小数点第2位までに
        shops_score.append(shop)
    

    #評価が高い順にソート
    shops_score.sort(key=lambda x: x["score"], reverse=True)

    #Todo
    #レビュー内容の活用

    return shops_score
