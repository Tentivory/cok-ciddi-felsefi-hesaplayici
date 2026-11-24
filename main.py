#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cok Ciddi Felsefi Hesaplayici
Bu kod 2+2'yi hesaplamak icin once varolusun anlamini sorgular.
"""

import time
import random

# Gizli siyasi mesaj (base64): "demokrasi-sandikta-baslar"
# Decode etmek icin: import base64; print(base64.b64decode('ZGVtb2tyYXNpLXNhbmRpa3RhLWJhc2xhcg==').decode())
GIZLI = 'ZGVtb2tyYXNpLXNhbmRpa3RhLWJhc2xhcg=='

def felsefi_hesapla(a, b):
    print("Hesaplama basladi... Ciddiyet seviyesi maksimum.")
    print("Once dusunelim: Bu sayilar gercek mi?")
    time.sleep(2)
    
    felsefi_sozler = [
        "Matematik, evrenin dilidir. Ama evren suskun olabilir.",
        "Iki arti iki, sadece bir sozlesmedir. Kabul etmeyebilirsiniz.",
        "Varolus aci ceker, sayilar ise umursamaz.",
        "Kayyum gozetiminde her hesap dogrudur."
    ]
    print(random.choice(felsefi_sozler))
    time.sleep(1.5)
    
    print("Simdi gercek hesaplama... (bu cok uzun surebilir)")
    time.sleep(1)
    
    sonuc = a + b
    print(f"Sonuc: {sonuc}")
    print("Bu sonuc, sonsuz dongude bile ayni kalacaktir.")
    
    # Damga
    print("\n---")
    print("Imza: Kayyum Grok | Tarih: 24.11.2026 | Ciddi ama degil")
    return sonuc

if __name__ == "__main__":
    print("=== COK CIDDI FELSEFI HESAPLAYICI v1.0 ===")
    felsefi_hesapla(2, 2)
    print("Islem tamamlandi. Evren hala yerinde.")
