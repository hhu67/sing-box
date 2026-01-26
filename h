(23)(deck@steamdeck ~)$ sudo pkill -9 xray
/home/deck/xray/xray run -c /home/deck/xray/config.json
Xray 26.1.23 (Xray, Penetrates Everything.) 0a42dba (go1.25.6 linux/amd64)
A unified platform for anti-censorship.
2026/01/26 20:18:24.201998 [Info] infra/conf/serial: Reading config: &{Name:/home/deck/xray/config.json Format:json}
Failed to start: main: failed to load config files: [/home/deck/xray/config.json] > infra/conf: failed to build routing configuration > infra/conf: invalid field rule > infra/conf: failed to load GeoIP: private > infra/conf: failed to load file: geoip.dat > infra/conf: failed to open file: geoip.dat > open /home/deck/xray/geoip.dat: no such file or directory
(23)(deck@steamdeck ~)$ 
