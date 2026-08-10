'''あなたは友達たちと N 人でしりとりを行うことにしました。
1 人目、 2 人目、...、 N 人目、 1 人目、2 人目、... という順序で発言をします。

ここで、それぞれの人は、次に挙げる 4 つのしりとりのルールを守って発言をする必要があります。

1. 発言は、単語リストにある K 個の単語のうちのいずれかの単語でなければならない。
2. 最初の人以外の発言の頭文字は、直前の人の発言の最後の文字と一緒でなければならない。
3. 今までに発言された単語を発言してはならない。
4. z で終わる単語を発言してはならない。

ここで、発言の途中で上のルールを破った場合、ルールを破った人はしりとりから外れます。
そして、その人を抜いて引き続きしりとりを続けていきます。このとき、後続の人は、ルール 2 を守る必要はありません。

N 人がしりとりを行ったログが M 行分与えられます。
このとき、M 回の発言が終わった後、しりとりから脱落せずに残っている人のリストを表示するプログラムを書いてください。
'''
import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    N, K = int(data[0]), int(data[1])
    valid_words = set(data[3:3 + K])  
    logs = data[3 + K:]               
    
    players = list(range(1, N + 1))
    used = set()
    last = None
    idx = 0
    
    for w in logs:
        
        if not players:
            break

        
        ok = (w in valid_words) and (last in (None, w[0])) and (w not in used) and (w[-1] != 'z')
        used.add(w)
        
        if ok:
            last = w[-1]
            idx = (idx + 1) % len(players)
        else:
            players.pop(idx)
            last = None
            
            if players:
                idx %= len(players)
            
    sys.stdout.write(f"{len(players)}\n" + "\n".join(map(str, players)) + "\n")

if __name__ == "__main__":
    main()