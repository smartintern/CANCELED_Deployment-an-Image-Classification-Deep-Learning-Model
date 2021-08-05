# misclassification
## Project Name: Misclassification 

## Sorun ne?
Kamera, görüntüyü sınıflandırırken hatalı sınıflandırıyor. 

## Görüntüler nasıl elde ediliyor?
Tesise kameralar yerleştiriliyor. Kameralar, ürünü 8 farklı açıdan çekiyor.  Çekilen görüntüye göre kamera, bir sonuç veriyor.

## Hata yapılan yer neresi?
Kamera, sınıflandırma yaparken karşılaştığı en zor hata gevşek teldir. Yani hata, kamerada gerçekleşiyor. 

## Neden hatalı sınıflandırma olasılığı var?
Bobinlerde bulunan çapaklar nedeniyle, görüntüde gevşek tel olmamasına rağmen, kamera gevşek tel olarak sınıflandırabiliyor. Kamera bu yüzden hatalı sınıflandırma yapabiliyor.

## Nasıl bir çözüm uygulanmalı?
Kameranın gevşek tel olarak sınıflandırdığı görüntüler bir havuzda toplanıyor. Havuzdaki çoğu görüntü aslında kabul edilebilir çapaklar oluyor. Bu havuzda bulunan görsellerin hatalı olup olmadığını bulmak için derin öğrenme kullanıyoruz. Derin öğrenme ile kameraya destek oluyoruz. 
