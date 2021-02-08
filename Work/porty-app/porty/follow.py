# follow.py
#
# Exercise 9.1
import os, time

def follow(filename):
    """
    Generator that produces a sequence of lines being written at the end of a file.
    """

    with open(filename, 'r') as f:
        f.seek(0, os.SEEK_END)      # 파일 포인터를 파일의 끝으로부터 0바이트로 이동

        while True:
            line = f.readline()
            if line == '':
                time.sleep(0.1)     # 짧게 쉬었다가 재시도
                continue
            yield line              # yield로 새로 추가된 line을 밖으로 내보냄

if __name__ == '__main__':
    # portfolio로 지정된 종목(관심 종목)만 추적하도록 report.py 사용
    import report

    portfolio = report.read_portfolio('Data/portfolio.csv')

    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')