import cv2

#讀入圖片
img = cv2.imread('..\PythonOpencvNotes\Tools\img\img-test.jpg')
#進行灰階
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#將圖片化為線條
canny_img = cv2.Canny(gray_img, 100, 100)

#類型
print(type(img))
#高度、寬度、通道數
print(f'width: {img.shape[1]} pixels')
print(f'height: {img.shape[0]} pixels')
print(f'channels: {img.shape[2]}')

#可以自由縮放式窗大小
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)

#顯示圖片
cv2.imshow("Image", img)
cv2.imshow("gray_img", gray_img)
cv2.imshow("canny_img", canny_img)

#輸出圖片(會輸出在與本程式相同資料夾中，會在同一層)
cv2.imwrite('output.jpg', gray_img)
cv2.imwrite('output.png', gray_img)
cv2.imwrite('output.tiff', gray_img)
# 設定 JPEG 圖片品質為 90（可用值為 0 ~ 100）
cv2.imwrite('output1.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])
# 設定 PNG 壓縮層級為 5（可用值為 0 ~ 9）
cv2.imwrite('output2.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 5])

#按下任意鍵，關閉所有視窗
cv2.waitKey(0)
cv2.destroyAllWindows()