
'''１行目にそれぞれ座席の数を表す整数、グループの数を表す整数 n, m がこの順で半角スペース区切りで与えられます。
続く m 行のうち i 行目 (1 ≦ i ≦ m)には、i番目のグループの人数を表す整数 a_i と 着席開始座席番号 b_i が与えられます。
a_i 人それぞれが座る座席を順に出力してください。
なお、実際に座るわけではなく、座席番号の確認のみを行う点に注意してください。
'''
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        seats = [str((b - 1 + i) % n + 1) for i in range(a)]
        sys.stdout.write(" ".join(seats) + "\n")

if __name__ == "__main__":
    main()

