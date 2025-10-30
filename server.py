#!/usr/bin/env python3
"""
Simple HTTP server for serving the SRS documentation static website.
Configured to run on port 5000 with proper cache control headers.
"""

import http.server
import socketserver
from functools import partial

class NoCacheHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP request handler with cache control disabled."""
    
    def end_headers(self):
        """Add cache control headers to prevent caching issues."""
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Log messages in a clean format."""
        print(f"[{self.log_date_time_string()}] {format % args}")

def run_server(port=5000, host="0.0.0.0"):
    """Run the HTTP server on specified port and host."""
    handler = NoCacheHTTPRequestHandler
    
    with socketserver.TCPServer((host, port), handler) as httpd:
        print(f"Server running at http://{host}:{port}/")
        print("Serving SRS Documentation for Soryouth Solar CRM")
        print("Press Ctrl+C to stop the server")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()
