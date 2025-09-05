import pyautogui
import datetime
import time
import sys

# --- 설정 ---
# ⚙️ 상시 활성화 모드 설정
# True: 아래 날짜/시간과 상관없이 항상 마우스 반전 실행
# False: 아래 지정된 날짜/시간에만 마우스 반전 실행
ALWAYS_ACTIVE = True  # <--- 이 값을 True 또는 False로 변경하여 모드 선택

# 📅 활성화될 시작일과 종료일 (ALWAYS_ACTIVE가 False일 때만 적용)
START_DAY = 23
END_DAY = 30

# ⏰ 활성화될 시작 시간과 종료 시간 (ALWAYS_ACTIVE가 False일 때만 적용)
START_HOUR = 11  # 오전 11시
END_HOUR = 13    # 오후 1시 (13시는 포함되지 않음, 즉 11:00:00 ~ 12:59:59까지)
# ----------------

def invert_mouse_conditionally():
    """설정된 조건에 따라 마우스 움직임을 반전시키는 함수"""
    try:
        print("마우스 반전 프로그램 시작.")
        
        # 시작 시 현재 모드 안내
        if ALWAYS_ACTIVE:
            print(">> 현재 모드: 상시 활성화 (날짜/시간 조건 무시)")
        else:
            print(">> 현재 모드: 조건부 활성화")
            print(f"   - 활성 날짜: 매월 {START_DAY}일 ~ {END_DAY}일")
            print(f"   - 활성 시간: 매일 {START_HOUR}:00 ~ {END_HOUR}:00")
        
        print("\n프로그램을 종료하려면 터미널에서 Ctrl + C 를 누르세요.")

        screen_width, screen_height = pyautogui.size()

        while True:
            # 현재 날짜와 시간 확인
            now = datetime.datetime.now()

            # 조건 확인
            is_active_day = START_DAY <= now.day <= END_DAY
            is_active_hour = START_HOUR <= now.hour < END_HOUR

            # 📌 상시 활성화 모드이거나, 지정된 날짜/시간 조건이 맞을 경우 실행
            if ALWAYS_ACTIVE or (is_active_day and is_active_hour):
                # 활성 조건일 때: 마우스 위치 반전
                current_x, current_y = pyautogui.position()
                inverted_x = screen_width - current_x
                inverted_y = screen_height - current_y
                pyautogui.moveTo(inverted_x, inverted_y, duration=0)
                
                # 터미널에 현재 상태 출력
                sys.stdout.write(f"\r[활성] 마우스 위치를 반전 중... ({now.strftime('%H:%M:%S')})")
                sys.stdout.flush()

            else:
                # 비활성 조건일 때: 정상 작동 상태 알림
                sys.stdout.write(f"\r[비활성] 조건 시간이 아닙니다. 정상 작동합니다. ({now.strftime('%H:%M:%S')})")
                sys.stdout.flush()

            # CPU 과부하 방지
            time.sleep(0.01)

    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")
    except Exception as e:
        print(f"\n오류가 발생했습니다: {e}")

if __name__ == "__main__":
    invert_mouse_conditionally()