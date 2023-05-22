
import os
os.system("pip install pillow")
os.system("pip install numpy")
from PIL import Image
import numpy as np

def benzerlik_hesapla(img1, img2):
    gri_img1 = np.mean(img1, axis=2)#resimlerin gri tona dönüştürülmesi
    gri_img2 = np.mean(img2, axis=2)
    normalize_img1 = (gri_img1 - np.mean(gri_img1)) / np.std(gri_img1)#verilerin numpy dizisinde saklanması
    normalize_img2 = (gri_img2 - np.mean(gri_img2)) / np.std(gri_img2)
    korelasyon = np.sum(normalize_img1 * normalize_img2) / (normalize_img1.shape[0] * normalize_img1.shape[1])#korelasyon işlemi
    return korelasyon

def find_similar_images(image_paths):
    images = [] # 1 kere tekrar eder
    for path in image_paths:# n kere tekrar eder
        image = np.array(Image.open(path)) # n * 1 kere tekrar eder
        images.append(image)# n * 1 kere tekrar eder
    benzerlik_skorlari = np.zeros((len(images), len(images))) # 1 kere tekrar eder
    for i in range(len(images)):#n kere tekrar eder
        for j in range(i+1, len(images)):# n * (n-1) kere tekrar eder
            skor = benzerlik_hesapla(images[i], images[j]) # n * (n-1) * 1 kere tekrar eder
            benzerlik_skorlari[i, j] = skor# n * (n-1) * 1 kere tekrar eder
            benzerlik_skorlari[j, i] = skor# n * (n-1) * 1 kere tekrar eder

    en_cok_benzeyen_gorseller = []# 1 kere tekrar eder
    for i in range(len(images)):#n kere tekrar eder
        most_similar_index = np.argmax(benzerlik_skorlari[i])# n * 1 kere tekrar eder
        en_cok_benzeyen_gorseller.append((i, most_similar_index, benzerlik_skorlari[i, most_similar_index]))#n * 1 kere tekrar eder

    en_cok_benzeyen_gorseller.sort(key=lambda x: x[2], reverse=True)#n kere tekrar eder

    for image_pair in en_cok_benzeyen_gorseller:#n kere tekrar eder
        image1_path = image_paths[image_pair[0]]#n * 1 kere tekrar eder
        image2_path = image_paths[image_pair[1]]# n * 1 kere tekrar eder
        benzerlik_skoru = image_pair[2]

        if benzerlik_skoru == 1.0:# n * 1 kere tekrar eder
            print("iki görsel de aynı:", image1_path, image2_path)# n * 1 kere tekrar eder
        print("birinci görsel: {}, ikinci görsel: {}, benzerlik oranı: %{}".format(image1_path, image2_path, 100*benzerlik_skoru))#n * 1 kere tekrar eder

"""
algoritmadaki iterasyonun hesaplanması:
    T(n) = 4n^2 - 4n  + 7n * 1 + 6n + 3
        = 4n^2 + 9n + 3 olarak hesaplanır dolayısıyla big o notasyonu:
        O(n^2) şeklindedir.
"""


def get_image_paths():
    path  = os.listdir()
    for i in path:
        if i == "ALGORTIMA_ANALIZI_ODEV_SOURCES-20230520T204113Z-001":
            os.chdir(i)
    img_path = os.listdir()
    return img_path

def main():
    image_paths = get_image_paths()
    find_similar_images(image_paths)

main()