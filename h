(7)(deck@steamdeck ~)$ curl -x socks5h://127.0.0.1:10808 https://google.com -I
HTTP/2 301 
location: https://www.google.com/
content-type: text/html; charset=UTF-8
content-security-policy-report-only: object-src 'none';base-uri 'self';script-src 'nonce-Xx9uZLeHn-zVDz-vjHHIhQ' 'strict-dynamic' 'report-sample' 'unsafe-eval' 'unsafe-inline' https: http:;report-uri https://csp.withgoogle.com/csp/gws/other-hp
date: Mon, 26 Jan 2026 17:21:06 GMT
expires: Wed, 25 Feb 2026 17:21:06 GMT
cache-control: public, max-age=2592000
server: gws
content-length: 220
x-xss-protection: 0
x-frame-options: SAMEORIGIN
alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000

(deck@steamdeck ~)$ 
