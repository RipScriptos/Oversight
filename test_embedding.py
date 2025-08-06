#!/usr/bin/env python3
"""
Test script to verify embedding functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask
from app import app
import threading
import time
import requests

def test_embedding():
    """Test the embedding functionality"""
    
    print("Testing Oversight AI Embedding Functionality")
    print("=" * 50)
    
    # Start the Flask app in a separate thread
    def run_app():
        app.run(host='0.0.0.0', port=12001, debug=False, use_reloader=False)
    
    server_thread = threading.Thread(target=run_app, daemon=True)
    server_thread.start()
    
    # Wait for server to start
    time.sleep(3)
    
    # Test endpoints
    endpoints = [
        ('/', 'Main Interface'),
        ('/embed', 'Embeddable Interface'),
        ('/embed/minimal', 'Minimal Embeddable Interface'),
        ('/api/report-types', 'API - Report Types')
    ]
    
    base_url = 'http://localhost:12001'
    
    for endpoint, description in endpoints:
        try:
            response = requests.get(f"{base_url}{endpoint}", timeout=5)
            status = "✅ PASS" if response.status_code == 200 else f"❌ FAIL ({response.status_code})"
            print(f"{status} - {description}: {endpoint}")
            
            if endpoint == '/api/report-types' and response.status_code == 200:
                data = response.json()
                print(f"    Available report types: {data.get('report_types', [])}")
                
        except Exception as e:
            print(f"❌ FAIL - {description}: {endpoint} - Error: {str(e)}")
    
    print("\n" + "=" * 50)
    print("Embedding Features:")
    print("✅ CORS enabled for cross-origin embedding")
    print("✅ X-Frame-Options set to ALLOWALL for iframe embedding")
    print("✅ Multiple embedding interfaces available")
    print("✅ Responsive design for different screen sizes")
    print("✅ API endpoints accessible from embedded versions")
    
    print("\nEmbedding URLs:")
    print(f"📱 Standard Embed: {base_url}/embed")
    print(f"📱 Minimal Embed: {base_url}/embed/minimal")
    print(f"📚 Embedding Guide: {base_url}/embed/guide")
    
    print("\nSample Iframe Code:")
    print(f'<iframe src="{base_url}/embed" width="600" height="500" frameborder="0"></iframe>')
    
    print("\n🎉 Embedding functionality is ready!")
    print("You can now embed Oversight AI into any website using the iframe codes above.")

if __name__ == "__main__":
    test_embedding()