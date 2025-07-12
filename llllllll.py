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
    x = np.linspace(-2 * np.pi, 2 * np.pi, 400) # -2π 부터 2π 까지 400개의 점 생성

    if func_type == 'sin':
        y = a * np.sin(b * x + c) + d
        title = f'y = {a}sin({b}x + {c}) + {d}'
    elif func_type == 'cos':
        y = a * np.cos(b * x + c) + d
        title = f'y = {a}cos({b}x + {c}) + {d}'
    elif func_type == 'tan':
        # tan 함수는 점근선 처리가 필요하므로, 주기에 맞춰 범위를 조정하고 불연속점 처리
        # tan(theta)는 theta = n*pi + pi/2 에서 불연속
        # bx + c = n*pi + pi/2
        # x = (n*pi + pi/2 - c) / b
        # 여기서는 간단하게 매우 큰 값을 줘서 점근선처럼 보이게 처리합니다.
        # 더 정교한 처리를 위해서는 불연속점을 제외하고 여러 구간으로 나누어 그려야 합니다.
        y = a * np.tan(b * x + c) + d
        title = f'y = {a}tan({b}x + {c}) + {d}'
        
        # 탄젠트 함수의 점근선을 시각적으로 처리하기 위한 부분 (선택 사항)
        # 탄젠트는 특정 값에서 무한대로 발산하므로, 그래프가 끊겨 보일 수 있습니다.
        # 이를 위해 y값이 너무 커지거나 작아지는 경우를 처리합니다.
        y[y > 10] = np.nan  # y값이 너무 크면 NaN으로 처리하여 그래프에서 제외
        y[y < -10] = np.nan # y값이 너무 작으면 NaN으로 처리하여 그래프에서 제외


    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label=title, color='blue')
    plt.axhline(0, color='black', linewidth=0.5) # x축
    plt.axvline(0, color='black', linewidth=0.5) # y축
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.title(title)
    plt.xlabel('x (라디안)')
    plt.ylabel('y')
    plt.legend()
    plt.ylim([-5, 5]) # y축 범위 고정 (필요에 따라 조절)
    plt.xticks(np.arange(-2*np.pi, 2*np.pi + np.pi/2, np.pi/2), 
               ['$-2\pi$', '$-3\pi/2$', '$-\pi$', '$-\pi/2$', '$0$', '$\pi/2$', '$\pi$', '$3\pi/2$', '$2\pi$'])
    plt.show()

if __name__ == "__main__": # <-- 이 부분을 수정했습니다.
    plot_trigonometric_function()
