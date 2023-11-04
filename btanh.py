import numpy as np
import cv2  # Để đọc và hiển thị hình ảnh (sử dụng OpenCV)

# Đọc hình ảnh từ tệp ảnh
image = cv2.imread('cat.jpg')

# Kiểm tra xem hình ảnh đã được đọc thành công chưa
if image is not None:
    # Lấy các kích thước của hình ảnh
    height, width, channels = image.shape

    # Tạo một mảng NumPy mới chỉ chứa kênh màu đỏ
    red_channel = np.zeros((height, width, channels), dtype=np.uint8)
    red_channel[:, :, 2] = image[:, :, 2]  # Kênh màu đỏ

    # Tạo một mảng NumPy mới chỉ chứa kênh màu xanh
    blue_channel = np.zeros((height, width, channels), dtype=np.uint8)
    blue_channel[:, :, 0] = image[:, :, 0]  # Kênh màu xanh

    # Tạo một mảng NumPy mới chỉ chứa kênh màu xanh
    green_channel = np.zeros((height, width, channels), dtype=np.uint8)
    green_channel[:, :, 1] = image[:, :, 1]  # Kênh màu xanh

    new_height = height // 4  # Giảm độ phân giải theo chiều cao
    new_width = width // 4  # Giảm độ phân giải theo chiều rộng

    # Tạo một mảng NumPy mới với kích thước mới
    resized_image = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    # Giảm độ phân giải của hình ảnh bằng cách trích xuất pixel
    for i in range(new_height):
        for j in range(new_width):
            resized_image[i, j] = image[i * 4, j * 4]

        #Scale up:
    original_height, original_width, _ = resized_image.shape
    scale_x = width / original_width
    scale_y = height / original_height
    scaled_image = np.zeros((height, width, 3), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            original_x = int(x / scale_x)
            original_y = int(y / scale_y)
            scaled_image[y, x] = resized_image[original_y, original_x]

    #Cropped
    cropped_image= np.zeros((height, width, channels), dtype=np.uint8)
    cropped_image[20:334,112:434] = image[20:334,112:434]
    
    # Hiển thị
    cv2.imshow('Original Channel', image)
    cv2.imshow('Red Channel', red_channel)
    cv2.imshow('Blue Channel', blue_channel)
    cv2.imshow('Green Channel', green_channel)
    #cv2.imshow('Resized Image', resized_image)
    cv2.imshow('Cropped Image', cropped_image)
    cv2.imshow('DeRes Image', scaled_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


else:
    print("Không thể đọc hình ảnh.")
