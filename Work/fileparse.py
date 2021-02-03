# fileparse.py
#
# Exercise 3.6
import csv

def parse_csv(filename, select = None, types = [str, int, float], has_headers = True):
    """
    CSV 파일을 읽은 뒤 파싱하여 레코드의 목록(딕셔너리 리스트)을 생성
    """
    with open(filename) as f:
        rows = csv.reader(f)

        # 헤더 키워드 인수가 없거나 True이면 헤더를 읽음
        headers = next(rows) if has_headers else []

        # 컬럼 선택 키워드 인수가 주어지면, 지정한 컬럼의 인덱스를 찾음
        # 또한 결과 딕셔너리에 사용할 헤더의 집합을 좁힌다
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []
        
        records = []
        for row in rows:
            if not row:     # 데이터가 없는 행은 건너뜀
                continue
            # 특정 컬럼 선택 키워드 인수가 존재하면 필터링
            if indices:
                row = [row[index] for index in indices]
            # 형변환 선택 키워드 인수가 존재하면 형변환
            if types:
                row = [func(val) for func, val in zip(types, row)]
            # 헤더 여부에 따라 튜플 또는 딕셔너리 생성
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
    
    return records