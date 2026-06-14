from http.server import HTTPServer, BaseHTTPRequestHandler
import json, os, datetime

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({
            "ok": True,
            "service": "csot-week2",
            "time": datetime.datetime.now().isoformat(),
            "path": self.path,
        }).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body)
    def log_message(self, fmt, *args):
        print(fmt % args, flush=True)

if __name__ == "__main__":
    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "8000"))
    print(f"listening on {host}:{port}", flush=True)
    HTTPServer((host, port), H).serve_forever()
