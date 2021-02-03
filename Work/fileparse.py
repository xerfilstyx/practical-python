# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename):
    """
    CSV 파일을 읽은 뒤 파싱하여 레코드의 목록(딕셔너리 리스트)을 생성
    """
    with open(filename) as f:
        rows = csv.reader(f)

        # 헤더를 읽음
        headers = next(rows)
        records = []
        for row in rows:
            if not row:     # 데이터가 없는 행은 건너뜀
                continue
            record = dict(zip(headers, row))
            records.append(record)
    
    return records