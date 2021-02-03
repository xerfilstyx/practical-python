# fileparse.py
#
# Exercise 3.10
import csv

def parse_csv(filename, select = None, types = [str, int, float], has_headers = True, delimiter = ',', silence_errors = False):
    """
    CSV 파일을 읽은 뒤 파싱하여 레코드의 목록(딕셔너리 리스트)을 생성
    """
    # select의 값이 존재하고 헤더가 존재하지 않는다면 틀린 인수 지정이므로 예외 발생
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    with open(filename) as f:
        # 구분자를 지정하지 않는 경우 콤마가 기본값이 되며, 지정한 경우에 그 구분자를 csv.reader()에 반영
        rows = csv.reader(f, delimiter = delimiter)

        # 헤더 키워드 인수가 없거나 True이면 헤더를 읽음
        headers = next(rows) if has_headers else []

        # 컬럼 선택 키워드 인수가 주어지면, 지정한 컬럼의 인덱스를 찾음
        # 또한 결과 딕셔너리에 사용할 헤더의 집합을 좁힌다
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        
        records = []
        for rowno, row in enumerate(rows, 1):
            if not row:     # 데이터가 없는 행은 건너뜀
                continue
            # 특정 컬럼 선택 키워드 인수가 존재하면 필터링
            if select:
                row = [row[index] for index in indices]
            # 형변환 선택 키워드 인수가 존재하면 형변환
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:  # silence_errors가 True로 지정된 경우에만 오류 메시지 출력
                        print(f'Row {rowno}: Couldn\'t convert {row}')
                        print(f'Row {rowno}: Reason - {e}')
                    continue    # 예외 발생시 해당 데이터는 row에 반영하지 않음

            # 헤더 여부에 따라 튜플 또는 딕셔너리 생성
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
    
    return records