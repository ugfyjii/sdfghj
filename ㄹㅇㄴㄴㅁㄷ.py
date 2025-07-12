import numpy as np
import matplotlib.pyplot as plt

def plot_trigonometric_function():
    print("삼각함수 그래프를 그려드립니다.")
    print("지원하는 함수: sin, cos, tan")

    while True:
        func_type = input("함수 종류를 입력하세요 (sin, cos, tan): ").lower()
        if func_type in ['sin', 'cos', 'tan']:
            break
        else:
            print("잘못된 함수 종류입니다. 다시 입력해주세요.")

    a = float(input("진폭(Amplitude, A)을 입력하세요 (예: 1): "))
    b = float(input("주기 관련 계수(Frequency, B)를 입력하세요 (예: 1, 주기는 2π/|B|): "))
    c = float(input("위상 이동(Phase Shift, C)을 입력하세요 (예: 0, x축으로 -C/B만큼 이동): "))
    d = float(input("수직 이동(Vertical Shift, D)을 입력하세요 (예: 0, y축으로 D만큼 이동): "))

    # x 값의 범위 설정 (라디안)
    x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

    if func_type == 'sin':
        y = a * np.sin(b * x + c) + d
        title = f'y = {a}sin({b}x + {c}) + {d}'
    elif func_type == 'cos':
        y = a * np.cos(b * x + c) + d
        title = f'y = {a}cos({b}x + {c}) + {d}'
    elif func_type == 'tan':
        # 탄젠트 함수는 점근선이 있기 때문에, 점근선 근처의 값을 NaN으로 처리하여 그래프가 끊기게 만듭니다.
        # 이렇게 하면 무한대로 뻗어나가는 부분이 보기 좋게 처리됩니다.
        
        y_raw = a * np.tan(b * x + c) + d
        
        # 특정 범위 밖의 값을 NaN으로 처리하여 점근선을 시각적으로 표현
        y = np.where(np.abs(y_raw) > 20, np.nan, y_raw) # 20은 조절 가능한 값입니다.
        title = f'y = {a}tan({b}x + {c}) + {d}'


    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=title, color='blue')
    plt.axhline(0, color='black', linewidth=0.5) # x축
    plt.axvline(0, color='black', linewidth=0.5) # y축
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.title(title)
    plt.xlabel('x (라디안)')
    plt.ylabel('y')
    plt.legend()
    
    # x축 눈금 (틱)을 라디안 값으로 보기 좋게 설정
    plt.xticks(np.arange(-2*np.pi, 2*np.pi + np.pi/2, np.pi/2), 
               ['$-2\pi$', '$-3\pi/2$', '$-\pi$', '$-\pi/2$', '$0$', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$'])
    plt.show()

if __name__ == "__main__":
    plot_trigonometric_function()
