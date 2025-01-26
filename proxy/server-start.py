import http.server
import socketserver
import requests

class Proxy(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Получаем URL, на который нужно сделать запрос
        url = self.path[1:]  # Убираем начальный слэш
        print(f"Proxying request to: {url}")

        # Выполняем запрос к целевому URL
        try:
            response = requests.get(url)

            # Устанавливаем заголовки ответа
            self.send_response(response.status_code)
            for key, value in response.headers.items():
                self.send_header(key, value)
            self.end_headers()

            # Отправляем содержимое ответа
            self.wfile.write(response.content)
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b"Error: " + str(e).encode())

if __name__ == "__main__":
    PORT = 1080
    # Используем локальный IP-адрес
    with socketserver.TCPServer(("127.0.0.1", PORT), Proxy) as httpd:
        print(f"Proxy running on http://127.0.0.1:{PORT}")
        httpd.serve_forever()
