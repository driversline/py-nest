import http.server
import socketserver
import requests

class Proxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        url = self.path[1:]
        print(f"Proxying request to: {url} | Проксирование запроса к: {url}")

        try:
            response = requests.get(url)

            self.send_response(response.status_code)
            for key, value in response.headers.items():
                self.send_header(key, value)
            self.end_headers()

            self.wfile.write(response.content)
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Error: " + str(e).encode() + b" | Ошибка: " + str(e).encode())

if __name__ == "__main__":
    PORT = 1080
    with socketserver.TCPServer(("127.0.0.1", PORT), Proxy) as httpd:
        print(f"Proxy running on http://127.0.0.1:{PORT} | Прокси запущен на http://127.0.0.1:{PORT}")
        httpd.serve_forever()
