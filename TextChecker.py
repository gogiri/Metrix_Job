import tkinter as tk
from tkinter import scrolledtext
import webbrowser  # 웹 브라우저 모듈

# NIA 정제 창
def nia_refine_window():
    for widget in root.winfo_children():
        widget.destroy()  # 기존 창의 위젯들을 모두 삭제
    root.title("NIA 정제 작업")
    
    # 새로운 NIA 정제 작업 화면 위젯
    label = tk.Label(root, text="NIA 정제 작업 화면입니다.", font=("Arial", 14))
    label.pack(pady=20)
    
    # 뒤로 가기 버튼
    back_button = tk.Button(root, text="뒤로 가기", command=open_nia_window, width=30, height=2)
    back_button.pack(pady=10)

# NIA 검수 창
def nia_review_window():
    for widget in root.winfo_children():
        widget.destroy()  # 기존 창의 위젯들을 모두 삭제
    root.title("NIA 검수 작업")
    
    # 새로운 NIA 검수 작업 화면 위젯
    label = tk.Label(root, text="NIA 검수 작업 화면입니다.", font=("Arial", 14))
    label.pack(pady=20)
    
    # 뒤로 가기 버튼
    back_button = tk.Button(root, text="뒤로 가기", command=open_nia_window, width=30, height=2)
    back_button.pack(pady=10)

# NIA 가공 창
def nia_process_window():
    for widget in root.winfo_children():
        widget.destroy()  # 기존 창의 위젯들을 모두 삭제
    root.title("NIA 가공 작업")
    
    # 새로운 NIA 가공 작업 화면 위젯
    label = tk.Label(root, text="NIA 가공 작업 화면입니다.", font=("Arial", 14))
    label.pack(pady=20)
    
    # 뒤로 가기 버튼
    back_button = tk.Button(root, text="뒤로 가기", command=open_nia_window, width=30, height=2)
    back_button.pack(pady=10)

# NIA 메인 창
def open_nia_window():
    for widget in root.winfo_children():
        widget.destroy()  # 기존 창의 위젯들을 모두 삭제
    root.title("NIA 작업 툴")

    # NIA 정제 버튼
    refine_button = tk.Button(root, text="NIA 정제", command=nia_refine_window, width=30, height=2)
    refine_button.pack(pady=10)

    # NIA 검수 버튼
    review_button = tk.Button(root, text="NIA 검수", command=nia_review_window, width=30, height=2)
    review_button.pack(pady=10)

    # NIA 가공 버튼
    process_button = tk.Button(root, text="NIA 가공", command=nia_process_window, width=30, height=2)
    process_button.pack(pady=10)

    # 뒤로 가기 버튼 추가
    back_button = tk.Button(root, text="뒤로 가기", command=open_main_window, width=30, height=2)
    back_button.pack(pady=20)

import tkinter as tk
from tkinter import scrolledtext
import webbrowser

# 기호를 교체하는 함수 정의
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

# NIPA 작업 툴 창
def open_nipa_window():
    for widget in root.winfo_children():
        widget.destroy()  # 기존 창의 위젯들을 모두 삭제
    root.title("NIPA 작업 툴")

    # 가이드라인 제목 추가
    guideline_label = tk.Label(root, text="가이드라인", font=("Arial", 14, "bold"))
    guideline_label.pack(pady=10)
    
    # 링크 버튼을 생성하여 클릭 시 브라우저에서 열리도록 함
    def open_link():
        webbrowser.open("https://buly.kr/BeJ74FT")

    # 링크 버튼을 생성
    link_button = tk.Button(root, text="https://buly.kr/BeJ74FT", fg="blue", cursor="hand2", command=open_link)
    link_button.pack(pady=10)
    
    # 중요한 메모 텍스트 추가
    memo_text = (
        "&& : 표시 글 제목 및 저자, 목차\n"
        "@@ : 글 본문 (참고문헌 포함)\n"
        "## : 머리말, 꼬리말 (페이지 번호만 있는 경우 포함)\n"
        "$$ : 각주/미주"
    )
    # 메모 텍스트 활성화 (ScrolledText로 변경)
    memo_label = tk.Label(root, text="메모:", font=("Arial", 12), justify=tk.LEFT)
    memo_label.pack(pady=5)

    memo_field = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=6)
    memo_field.insert(tk.END, memo_text)
    memo_field.pack(pady=10)
    
    # 입력 필드 라벨
    input_label = tk.Label(root, text="각주/미주 텍스트를 입력하세요:")
    input_label.pack(pady=10)
    
    # 텍스트 입력 필드 (스크롤 가능)
    input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
    input_text.pack(pady=10)

    # 결과 출력 필드
    output_label = tk.Label(root, text="변경된 텍스트:")
    output_label.pack(pady=10)

    output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, state='disabled')
    output_text.pack(pady=10)

    # 함수 실행 및 결과 출력하는 함수
    def process_text():
        # 입력 데이터를 가져옴
        input_data = input_text.get("1.0", tk.END).strip()
        # 기호 교체 함수 실행
        output_data = replace_alternating_symbols(input_data)
        # 결과를 출력 필드에 삽입
        output_text.config(state='normal')
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, output_data)
        output_text.config(state='disabled')
    
    # 텍스트 처리 버튼
    process_button = tk.Button(root, text="텍스트 처리", command=process_text, width=20)
    process_button.pack(pady=20)

    # 뒤로 가기 버튼 추가
    back_button = tk.Button(root, text="뒤로 가기", command=open_main_window, width=20)
    back_button.pack(pady=10)

# 메인 화면 창
def open_main_window():
    for widget in root.winfo_children():
        widget.destroy()  # 기존 창의 위젯들을 모두 삭제
    root.title("텍스트체커 - 시작 인터페이스")

    # NIA 작업 툴로 이동하는 버튼
    nia_button = tk.Button(root, text="NIA 작업 툴로 이동", command=open_nia_window, width=30, height=2)
    nia_button.pack(pady=20)

    # NIPA 작업 툴로 이동하는 버튼
    nipa_button = tk.Button(root, text="NIPA 작업 툴로 이동", command=open_nipa_window, width=30, height=2)
    nipa_button.pack(pady=20)

# Tkinter 윈도우 생성 및 시작 화면 호출
root = tk.Tk()
open_main_window()  # 메인 화면을 첫 화면으로 설정
root.mainloop()


