import json
import os

def convert_for_deck(input_file, output_file="config.json"):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # 1. Настройка логирования
        config['log'] = {
            "level": "info",
            "timestamp": True
        }

        # 2. Добавление TUN интерфейса для работы всей системы через VPN
        config['inbounds'] = [
            {
                "type": "tun",
                "tag": "tun-in",
                "interface_name": "tun0",
                "address": ["172.19.0.1/30"],
                "auto_route": True,
                "strict_route": True,
                "stack": "system",
                "sniff": True
            }
        ]

        # 3. Настройка DNS (исправленный вариант для SteamOS)
        config['dns'] = {
            "servers": [
                {
                    "tag": "dns-remote",
                    "address": "8.8.8.8",
                    "detour": "proxy"
                },
                {
                    "tag": "dns-direct",
                    "address": "1.1.1.1",
                    "detour": "direct"
                }
            ],
            "rules": [
                {"outbound": "any", "server": "dns-direct"}
            ],
            "final": "dns-remote"
        }

        # 4. Настройка маршрутизации (Routing)
        config['route'] = {
            "auto_detect_interface": True,
            "rules": [
                {
                    "protocol": "dns",
                    "action": "hijack-dns"
                },
                {
                    "ip_is_private": True,
                    "outbound": "direct"
                }
            ]
        }

        # 5. Очистка outbounds (убеждаемся, что теги совпадают)
        # Ищем основной прокси-исход в конфиге пользователя
        for outbound in config.get('outbounds', []):
            if outbound.get('type') not in ['direct', 'dns', 'block']:
                outbound['tag'] = 'proxy' # Принудительно ставим тег для работы правил

        # Добавляем прямой выход, если его нет
        if not any(o.get('tag') == 'direct' for o in config['outbounds']):
            config['outbounds'].append({"type": "direct", "tag": "direct"})

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Готово! Файл сохранен как: {output_file}")
        print("Теперь скопируй его в /home/deck/sing-box/ и перезапусти сервис.")

    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    filename = input("Введите имя вашего исходного JSON файла (например, my_server.json): ")
    convert_for_deck(filename)
