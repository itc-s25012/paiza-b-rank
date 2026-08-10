
'''1行目に座席の数を表す整数 n が与えられます。
2行目にグループの人数を表す a と、着席開始座席番号 b が与えられます。
3行目に n 席の座席の状況が空白区切りで与えられます。
a 人が全員座れる場合は Yes を、そうでない場合は Noを出力してください。
また座れる場合は a 人が着席した後の座席の状況を空白区切りで出力してください
'''
import sys

def main():
    n = int(sys.stdin.readline())
    a, b = map(int, sys.stdin.readline().split())
    seats = list(map(int, sys.stdin.readline().split()))
    
   
    idx = [(b - 1 + i) % n for i in range(a)]
    
    if sum(seats[i] for i in idx) == 0:
        for i in idx: seats[i] = 1
        sys.stdout.write(f"Yes\n{' '.join(map(str, seats))}\n")
    else:
        sys.stdout.write("No\n")

if __name__ == "__main__":
    main()