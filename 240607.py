def kiosk():
    menu = ["냉면", "볶음밥", "피자", "짜장면"]

    while True:
        try:
            choice = int(input("메뉴를 선택하세요 (1. 냉면, 2. 볶음밥, 3. 피자, 4. 짜장면): ")) - 1
            print(f"선택한 메뉴: {menu[choice]}")
            break
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")
        except IndexError:
            print("메뉴에 없는 번호입니다. 다시 입력하세요.")

kiosk()

