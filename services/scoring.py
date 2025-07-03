from typing import List, Dict
from datetime import datetime
import math

#Min-Max正規化(評価指数を0〜１にするため)
def min_max(value, min_value, max_value):
    if max_value == min_value: #割り切れない時
        return 0.0
    return (value - min_value) / (max_value - min_value)

# user_genre: str, #選択ジャンル
#     keywords: List[str] = [], #推測キーワード
#     mode: str = "base", #ジャンル推定と好み推定モードがある
#    eta: datetime = None #時間

def score_shops(
    shop_list: List[Dict], #複数のお店の情報
) -> List[Dict]: #お店のリスト情報を返す
    
    #特徴量の取得
    distances = [shop.get("distance",0) for shop in shop_list] #各距離
    ratings = [shop.get("rating", 0) for shop in shop_list] #各お店の評価
    #レビュー数（差が出過ぎるためlogスケーリングで緩やかに）
    log_reviews = [math.log(1 + shop.get("user_ratings_total", 0)) for shop in shop_list]

    #数値を正規化
    min_dist, max_dist = min(distances), max(distances) #距離
    min_rating, max_rating = min(ratings), max(ratings) #評価
    max_log_review = max(log_reviews) if log_reviews else 1 #レビュー数のminは0のため不要
    
    score_shops = []

    # 各お店を評価
    for shop in shop_list:
        #各評価指数を0〜1に
        distance_score = min_max(shop.get("distance", 0), min_dist, max_dist)
        rating_score = min_max(shop.get("rating", 0), min_rating, max_rating)
        #minがないため関数を使わず計算
        log_review = math.log(1 + shop.get("user_ratings_total", 0))
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