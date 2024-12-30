import mss
import numpy as np
import cv2

# Захват экрана
with mss.mss() as sct:
    monitor = sct.monitors[1]  # Выбираем основной экран (можно изменить на другой)
    screenshot = np.array(sct.grab(monitor))  # Получаем скриншот в виде массива


img = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
img = cv2.resize(img, (1680, 1360))
img = cv2.GaussianBlur(img, (1, 1), 0)
img = cv2.Canny(img,40,40)

contorus, hirevi = cv2.findContours(img, cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
print(f"{len(contorus)} ")




cv2.imwrite("image_final.png", img)

# Отображение обработанного изображения
cv2.imshow("image_final", img)
cv2.waitKey(0)
cv2.destroyAllWindows()