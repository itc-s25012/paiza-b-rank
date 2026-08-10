'''あなたは念願の3Dプリンタを購入しました。早速、いろいろな立体を出力して楽しみましょう！

3Dプリンタに入力される立体のデータは、大きさ 1×1×1 の立方体（セルという）を一つ以上組み合わせることで得られます。より正確に述べると次のようになります：

三次元空間で図１のような座標系 (x,y,z) を考えます。
立体データは、各座標 (x,y,z) でのセルが立体に含まれるかどうかを指定することで得られます。例えば、図２の立体は 14 個のセル (1,1,1), (1,2,1), (1,3,1), (2,1,1), (2,2,1), (3,1,1), (1,1,2), (1,2,2), (2,1,2), (2,2,2), (1,1,3), (1,2,3), (2,1,3), (2,2,3) を組み合わせることで得られます。
あなたはまず、出力したい立体のデータを作りました。あとは、データを3Dプリンタに入力して印刷するだけです。

しかし、データにミスがあっては大変です。慎重なあなたは、実際に印刷を始める前に、出力される立体を正面（x軸の正の方向）から見たときの図を求めてみることにしました。（図３）
立体のデータが入力された時、この立体を正面から見たときの図を出力するプログラムを書きましょう。'''

import sys

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    
   
    X, Y, Z = map(int, lines[0].split())
    
   
    front_view = [['.'] * Y for _ in range(Z)]
    
    line_idx = 1
    for x in range(X):
        for z in range(Z):
            row = lines[line_idx]
            line_idx += 1
            for y in range(Y):
                if row[y] == '#':
                    front_view[Z - 1 - z][y] = '#'
        
       
        if line_idx < len(lines) and lines[line_idx] == '--':
            line_idx += 1

   
    for z in range(Z - 1, -1, -1):
        sys.stdout.write("".join(front_view[z]) + "\n")

if __name__ == "__main__":
    main()