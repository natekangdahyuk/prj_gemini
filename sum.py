# sum.py

def main():
    try:
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))
        
        sum_result = num1 + num2
        print(f"두 숫자의 합은: {sum_result}")
    except ValueError:
        print("유효한 숫자를 입력해주세요.")

if __name__ == "__main__":
    main()
