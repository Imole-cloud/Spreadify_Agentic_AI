import sys
import os
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

try:
    from spreadify_agent import app
    from werkzeug.serving import WSGIRequestHandler
    import json

    def handler(event, context):
        """
        Netlify serverless function handler for Flask 2.3.3
        """
        try:
            # Extract HTTP method and path
            http_method = event.get('httpMethod', 'GET')
            path = event.get('path', '/')

            # Handle query parameters
            query_params = event.get('queryStringParameters') or {}

            # Handle request body
            body = event.get('body', '')
            if body and event.get('isBase64Encoded'):
                import base64
                body = base64.b64decode(body).decode('utf-8')

            # Create WSGI environment
            environ = {
                'REQUEST_METHOD': http_method,
                'PATH_INFO': path,
                'QUERY_STRING': '&'.join([f"{k}={v}" for k, v in query_params.items()]),
                'CONTENT_TYPE': event.get('headers', {}).get('content-type', ''),
                'CONTENT_LENGTH': str(len(body)) if body else '0',
                'wsgi.input': body,
                'wsgi.version': (1, 0),
                'wsgi.url_scheme': 'https',
                'wsgi.errors': sys.stderr,
                'wsgi.multithread': False,
                'wsgi.multiprocess': True,
                'wsgi.run_once': False
            }

            # Add headers to environ
            for key, value in event.get('headers', {}).items():
                key = key.upper().replace('-', '_')
                if key not in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
                    key = f'HTTP_{key}'
                environ[key] = value

            # Use Flask app's test client for processing
            with app.test_client() as client:
                if http_method == 'POST':
                    response = client.post(path, data=body, 
                                         headers=event.get('headers', {}))
                elif http_method == 'GET':
                    response = client.get(path, query_string=query_params)
                else:
                    response = client.open(path, method=http_method, 
                                         data=body, headers=event.get('headers', {}))

                # Format response for Netlify
                return {
                    'statusCode': response.status_code,
                    'headers': dict(response.headers),
                    'body': response.get_data(as_text=True),
                    'isBase64Encoded': False
                }

        except Exception as e:
            print(f"Error in serverless function: {str(e)}")
            return {
                'statusCode': 500,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps({'error': str(e)}),
                'isBase64Encoded': False
            }

    # For local testing
    if __name__ == '__main__':
        # Test the handler locally
        test_event = {
            'httpMethod': 'GET',
            'path': '/',
            'headers': {},
            'queryStringParameters': None,
            'body': None,
            'isBase64Encoded': False
        }
        result = handler(test_event, {})
        print(json.dumps(result, indent=2))

except ImportError as e:
    print(f"Import error: {e}")
    def handler(event, context):
        return {
            'statusCode': 500,
            'headers': {'Content-Type': 'application/json'},
            'body': json.dumps({'error': f'Import error: {str(e)}'}),
            'isBase64Encoded': False
        }
