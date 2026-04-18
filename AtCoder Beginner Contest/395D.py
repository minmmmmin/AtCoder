N, Q = map(int, input().split())

# 鳩の位置を管理するリスト
pigeon_positions = list(range(1, N + 1))

# 操作の処理
for _ in range(Q):
    op = list(map(int, input().split()))
    
    if op[0] == 1:
        # 種類1: 鳩aを巣bに移動
        a, b = op[1], op[2]
        pigeon_positions[a - 1] = b
        
    elif op[0] == 2:
        # 種類2: 巣aと巣bの鳩を入れ替え
        a, b = op[1], op[2]
        
        # 鳩の位置を入れ替え
        for i in range(N):
            if pigeon_positions[i] == a:
                pigeon_positions[i] = b
            elif pigeon_positions[i] == b:
                pigeon_positions[i] = a
    
    elif op[0] == 3:
        # 種類3: 鳩aがいる巣を報告
        a = op[1]
        print(pigeon_positions[a - 1])
