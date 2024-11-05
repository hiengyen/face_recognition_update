import cv2

name = "hieu"  # replace with your name

cam = cv2.VideoCapture(0)

cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
cv2.resizeWindow("press space to take a photo", 500, 300)

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("press space to take a photo", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = "dataset/" + name + "/image_{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()

# import cv2
# import os
#
# name = "Caroline"  # replace with your name
# output_dir = os.path.join("dataset", name)
#
# # Tạo thư mục nếu chưa tồn tại
# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)
#
# cam = cv2.VideoCapture(0)
#
# # Thiết lập kích thước cửa sổ và độ phân giải của camera (tuỳ chọn)
# cv2.namedWindow("press space to take a photo", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("press space to take a photo", 500, 300)
#
# img_counter = 0
#
# while True:
#     ret, frame = cam.read()
#     if not ret:
#         print("Failed to grab frame")
#         break
#
#     cv2.imshow("press space to take a photo", frame)
#
#     k = cv2.waitKey(1)
#     if k % 256 == 27:
#         # Nhấn ESC để thoát
#         print("Escape hit, closing...")
#         break
#     elif k % 256 == 32:
#         # Nhấn SPACE để chụp ảnh
#         img_name = os.path.join(output_dir, f"image_{img_counter}.jpg")
#         cv2.imwrite(img_name, frame)
#         print(f"{img_name} written!")
#         img_counter += 1
#         cv2.waitKey(200)  # Thời gian trễ nhỏ để tránh nhấn phím nhanh
#
# cam.release()
# cv2.destroyAllWindows()
