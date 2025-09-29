"""
Flask Web Application for Oversight AI System
Provides web interface for the 3-step AI process.
"""

from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import json
import io
import os
from datetime import datetime
from config import Config
from src.oversight_ai import OversightAI

app = Flask(__name__)
app.config.from_object(Config)

# Configure CORS for embedding
CORS(app, 
     origins="*",  # Allow all origins for embedding
     allow_headers=["Content-Type", "Authorization"],
     methods=["GET", "POST", "OPTIONS"])

# Add security headers for iframe embedding
@app.after_request
def after_request(response):
    # Allow iframe embedding from any origin
    response.headers['X-Frame-Options'] = 'ALLOWALL'
    # Alternative: Use Content-Security-Policy for more control
    # response.headers['Content-Security-Policy'] = "frame-ancestors *;"
    
    # Enable cross-origin resource sharing
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    
    return response

# Initialize the Oversight AI system
oversight_ai = OversightAI()

@app.route('/')
def index():
    """Main page with the web interface."""
    return render_template('index.html')

@app.route('/embed')
def embed():
    """Embeddable version of the web interface."""
    return render_template('embed.html')

@app.route('/embed/minimal')
def embed_minimal():
    """Minimal embeddable version for small iframes."""
    return render_template('embed_minimal.html')

@app.route('/embed/guide')
def embed_guide():
    """Embedding guide and documentation."""
    return send_file('embedding_guide.html')

@app.route('/api/analyze', methods=['POST'])
def analyze_topic():
    """
    API endpoint to analyze a topic using the 3-step AI process.
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400
        
        topic = data.get('topic', '').strip()
        report_type = data.get('report_type', 'detailed')
        
        if not topic:
            return jsonify({
                'success': False,
                'error': 'Topic is required'
            }), 400
        
        # Validate report type
        if not oversight_ai.validate_report_type(report_type):
            return jsonify({
                'success': False,
                'error': f'Invalid report type. Available types: {oversight_ai.get_available_report_types()}'
            }), 400
        
        # Process the topic through the 3-step AI system
        result = oversight_ai.process_topic(topic, report_type)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/status/<session_id>')
def get_status(session_id):
    """
    Get the processing status for a specific session.
    """
    try:
        status = oversight_ai.get_processing_status(session_id)
        
        if status:
            return jsonify({
                'success': True,
                'status': status
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Session not found'
            }), 404
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/results/<session_id>')
def get_results(session_id):
    """
    Get the complete results for a specific session.
    """
    try:
        results = oversight_ai.get_session_results(session_id)
        
        if results:
            return jsonify({
                'success': True,
                'results': results
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Session not found'
            }), 404
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/download/<session_id>')
def download_report(session_id):
    """
    Download the report for a specific session as a text file.
    """
    try:
        report_text = oversight_ai.export_session_data(session_id, format='text')
        
        if report_text:
            # Create a file-like object
            report_file = io.StringIO(report_text)
            report_bytes = io.BytesIO(report_file.getvalue().encode('utf-8'))
            
            # Get session data for filename
            results = oversight_ai.get_session_results(session_id)
            topic = results.get('final_report', {}).get('metadata', {}).get('topic', 'report')
            filename = f"oversight_ai_report_{topic.replace(' ', '_')}_{session_id}.txt"
            
            return send_file(
                report_bytes,
                as_attachment=True,
                download_name=filename,
                mimetype='text/plain'
            )
        else:
            return jsonify({
                'success': False,
                'error': 'Session not found or no report available'
            }), 404
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/history')
def get_history():
    """
    Get the processing history.
    """
    try:
        history = oversight_ai.list_processing_history()
        return jsonify({
            'success': True,
            'history': history
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/statistics')
def get_statistics():
    """
    Get system usage statistics.
    """
    try:
        stats = oversight_ai.get_system_statistics()
        return jsonify({
            'success': True,
            'statistics': stats
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/report-types')
def get_report_types():
    """
    Get available report types.
    """
    try:
        report_types = oversight_ai.get_available_report_types()
        return jsonify({
            'success': True,
            'report_types': report_types
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/clear-history', methods=['POST'])
def clear_history():
    """
    Clear the processing history.
    """
    try:
        oversight_ai.clear_history()
        return jsonify({
            'success': True,
            'message': 'History cleared successfully'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500

if __name__ == '__main__':
    print("Starting Oversight AI System...")
    print(f"Available report types: {oversight_ai.get_available_report_types()}")
    print(f"Server will run on {Config.HOST}:{Config.PORT}")
    print(f"Access the web interface at: http://localhost:{Config.PORT}")
    
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )