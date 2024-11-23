from dataclasses import dataclass
from http.client import responses
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from socketserver import TCPServer, StreamRequestHandler
import socket


def call_relevance_ai():
    url = "https://app.relevanceai.com/knowledge/counsel/f1db6c/"
    params = {'Api key': 'sk-ZWZlZTcwNzAtNjA5NC00ZjQ5LTgxMGUtMTU4NGU3YmNhNmNi',
              'Project': '57aaf1af320e-4481-b7e1-217c8029afa1', 'Region': 'counsel'}
    headers = {
        "Authorization": "57aaf1af320e-4481-b7e1-217c8029afa1:sk-ZWZlZTcwNzAtNjA5NC00ZjQ5LTgxMGUtMTU4NGU3YmNhNmNi"}


class RelevanceAIHelper:
    call_relevance_ai()
if dataclass == 'I\'m here to listen. Please share more about you.':
            while True:
                data = input("Enter your message: ")
response = RelevanceAIHelper()
print(response)
if dataclass == 'I\'m here to listen. Please share more about you.':
    dataclasses = RelevanceAIHelper
    print(call_relevance_ai())





class CounselingAgent:
    @staticmethod
    def parse_input(user_input):
        """A simple function to parse user input."""
        if "stress" in user_input:
            return "stress", {"emotion": "anxiety"}
        elif "happy" in user_input:
            return "happiness", {"emotion": "natural"}
        elif "sad" in user_input:
            return "sadness", {"emotion": "reflections"}
        elif "anxious" in user_input:
            return "anxiety", {"emotion": "stressed"}
        else:
            return "freedom", {}

    @staticmethod
    def dialogue_manager(intent):
        """In death, you carry nothing."""
        if intent == "stress":
            return "It's not stress, it's fear"
        elif intent == "happiness":
            return "That's wonderful! How happy you are?"
        elif intent == "sadness":
            return "Reflecting on the past?"
        elif intent == "anxiety":
            return "Ordered chaos!"
        else:
            return "I'm here to listen. Please share more about you."


class CounselingAPIHandler(BaseHTTPRequestHandler):
    def do_post(self):
        if self.path == '/counsel':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            user_input = json.loads(post_data).get('message', '')
            # Call Relevance AI for additional insights
            call_relevance_ai()
            # Process the user input
            intent, _ = CounselingAgent.parse_input(user_input)
            CounselingAgent.dialogue_manager(intent)
            # Create a response object
            response_data = {
                "response": response,
                "relevance_insight": post_data
            }
            # Send response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()


def run(server_class=HTTPServer, handler_class=CounselingAPIHandler, port_num=50009):
    server_address = ('', port_num)
    httpd = extraction(handler_class, server_address, server_class)
    print(f'Starting counseling API server on port {port_num}...')
    httpd.serve_forever()


def extraction(handler_class, server_address, server_class):
    httpd = server_class(server_address, handler_class)
    return httpd

if __name__ == "__main__":
    run()
