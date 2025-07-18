# Denizli Coder Web Services

Bu proje, FastAPI kullanılarak geliştirilmiş örnek bir REST API servisidir. Eğitim ve demo amaçlı hazırlanmıştır.

## Proje Gereksinimleri

- Python 3.11+
- pip
- virtualenv (opsiyonel)

## Kurulum Adımları

### 1. Repoyu klonlayın:

```bash

git clone https://github.com/mertozen/denizli-coder-web-services.git
cd denizli-coder-web-services
 ```

### 2. Sanal ortam oluşturun ve aktif edin:

```bash

python -m venv venv
source venv/bin/activate    # Windows için: venv\Scripts\activate

```
### 3. Gereksinimleri yükleyin:

```bash

pip install -r requirements.txt
```
### 4. Uygulamayı Başlatma
Projenin ana dosyası main.py içerisindedir.

Geliştirme modunda çalıştırmak için:

```bash

fastapi dev main.py
```
