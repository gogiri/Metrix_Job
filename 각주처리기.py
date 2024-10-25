def replace_alternating_symbols(text):
    # 변경할 기호 설정
    search_symbol = ''
    replacements = ['『', '』']
    
    # 기호를 교체할 인덱스 (0: 『, 1: 』)
    replacement_index = 0
    
    # 변경된 텍스트 저장
    new_text = ''
    
    # 텍스트 순차적으로 탐색
    for char in text:
        if char == search_symbol:
            # 기호를 교체하고 인덱스 교체
            new_text += replacements[replacement_index]
            # 인덱스를 0과 1 사이에서 반복
            replacement_index = 1 - replacement_index
        else:
            # 기호가 아닌 경우 그대로 저장
            new_text += char
    
    return new_text

# 예시 텍스트 데이터
input_data = input("텍스트 데이터를 입력하세요: ")

# 함수 호출하여 기호 변경
output_data = replace_alternating_symbols(input_data)

# 결과 출력
print("Original Text: ", input_data)
print("Modified Text: ", output_data)