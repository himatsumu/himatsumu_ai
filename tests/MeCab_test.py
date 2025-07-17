import MeCab

def tokenize_with_pos(text):
    mecab = MeCab.Tagger()
    nodes = mecab.parseToNode(text)
    tokens = []
    while nodes:
        if nodes.surface != "":
            tokens.append((nodes.surface, nodes.feature.split(',')[0]))
        nodes = nodes.next
    return tokens

def filter_pos(tokens, pos_list):
    return [token for token, pos in tokens if pos in pos_list]

text = "梅田バッティングドームに行ってきました！\n梅田駅から徒歩圏内にあり、天候に左右されないドーム型施設なので、いつでもバッティングを楽しめます⚾️球速は80km/hから150km/hまで幅広く設定されており、初心者から上級者まで安心して利用できます。店内は清潔感があり、スタッフの方も親切で丁寧な対応でした。金曜・土曜は朝5時まで営業しているため、部活帰りや友人との遊びにも最適です。ストレス発散にもおすすめのスポットです！"
tokens_with_pos = tokenize_with_pos(text)
nouns = filter_pos(tokens_with_pos, ['名詞'])
print(nouns)