## GEOIP

Terminalden ip öğrenme ve ip sorgulamak için yazılmış basit bir bash kodudur. Curl ile web servis kullanımını bash ile harmanlar.

####  Özetle: Atla (:horse:) deve (:dromedary_camel:) değildir.

Konsol'da kullanım:

```Bash
$ geoip my_ip
# Ekran çıktısı
  <ReturnCode>1</ReturnCode>
  <IP>193.xxx.xx.xx</IP>
  <ReturnCodeDetails>Success</ReturnCodeDetails>
  <CountryName>Turkey</CountryName>
  <CountryCode>TUR</CountryCode>
```

```Bash
$ geoip get_ip 195.xxx.xx.xx
# Ekran çıktısı
  <ReturnCode>1</ReturnCode>
  <IP>195.140.28.51</IP>
  <ReturnCodeDetails>Success</ReturnCodeDetails>
  <CountryName>Germany</CountryName>
  <CountryCode>DEU</CountryCode>
```
