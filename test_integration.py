#!/usr/bin/env python3
"""
Test script for Oversight AI System with OpenAI integration
Tests the system without requiring an actual OpenAI API key by mocking the API calls.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import unittest
from unittest.mock import patch, MagicMock
from src.oversight_ai import OversightAI
from src.research_engine import ResearchEngine
from src.report_generator import ReportGenerator
from config import Config


class TestOversightAIIntegration(unittest.TestCase):
    """Test the integrated Oversight AI system with mocked OpenAI calls."""
    
    def setUp(self):
        """Set up test environment."""
        # Mock the OpenAI API key validation
        with patch.object(Config, 'validate_openai_config', return_value=True):
            with patch.object(Config, 'OPENAI_API_KEY', 'test_key'):
                self.oversight_ai = OversightAI()
    
    @patch('openai.OpenAI')
    def test_research_engine_with_mocked_openai(self, mock_openai_client):
        """Test the research engine with mocked OpenAI responses."""
        # Mock OpenAI response
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "This is a test response about artificial intelligence from OpenAI."
        
        mock_client_instance = MagicMock()
        mock_client_instance.chat.completions.create.return_value = mock_response
        mock_openai_client.return_value = mock_client_instance
        
        # Create research engine with mocked OpenAI
        with patch.object(Config, 'validate_openai_config', return_value=True):
            with patch.object(Config, 'OPENAI_API_KEY', 'test_key'):
                research_engine = ResearchEngine()
        
        # Test research compilation
        result = research_engine.compile_information("Artificial Intelligence")
        
        # Verify the structure
        self.assertIn('topic', result)
        self.assertIn('sources', result)
        self.assertIn('content', result)
        self.assertIn('metadata', result)
        
        # Verify metadata includes timing information
        self.assertIn('processing_speed', result['metadata'])
        self.assertIn('loading_time', result['metadata'])
        self.assertIn('words_per_second', result['metadata'])
        
        # Verify sources information
        self.assertTrue(len(result['sources']) > 0)
        self.assertEqual(result['sources'][0]['type'], 'AI Generated')
        
        print("✅ Research engine with OpenAI integration test passed")
    
    def test_report_generator_markdown_export(self):
        """Test the report generator's markdown export functionality."""
        # Create sample report data
        sample_report_data = {
            'metadata': {
                'topic': 'Test Topic',
                'report_type': 'detailed',
                'generation_timestamp': '2023-01-01T00:00:00',
                'total_sources_analyzed': 8,
                'categorization_confidence': 0.85
            },
            'content': {
                'introduction': 'This is a test introduction.',
                'key_findings': ['Finding 1', 'Finding 2', 'Finding 3'],
                'analysis': {
                    'summary': 'Test analysis summary',
                    'details': 'Detailed analysis information'
                }
            },
            'appendices': {
                'methodology': 'Test methodology information'
            }
        }
        
        report_generator = ReportGenerator()
        markdown_output = report_generator.export_report_as_markdown(sample_report_data)
        
        # Verify markdown structure
        self.assertIn('# Test Topic - Detailed Report', markdown_output)
        self.assertIn('## 1. Sources Used', markdown_output)
        self.assertIn('## 2. Speed & Performance Metrics', markdown_output)
        self.assertIn('## 3. Document Content', markdown_output)
        self.assertIn('### Introduction', markdown_output)
        self.assertIn('### Key Findings', markdown_output)
        self.assertIn('## Appendices', markdown_output)
        
        print("✅ Report generator markdown export test passed")
    
    @patch('openai.OpenAI')
    def test_full_system_integration(self, mock_openai_client):
        """Test the complete system integration with mocked OpenAI."""
        # Mock OpenAI response
        mock_response = MagicMock()
        mock_response.choices[0].message.content = "Comprehensive information about the test topic."
        
        mock_client_instance = MagicMock()
        mock_client_instance.chat.completions.create.return_value = mock_response
        mock_openai_client.return_value = mock_client_instance
        
        # Test the complete process
        with patch.object(Config, 'validate_openai_config', return_value=True):
            with patch.object(Config, 'OPENAI_API_KEY', 'test_key'):
                oversight_ai = OversightAI()
                result = oversight_ai.process_topic("Test Topic", "detailed")
        
        # Verify the result structure
        self.assertTrue(result['success'])
        self.assertIn('session_id', result)
        self.assertIn('processing_time', result)
        self.assertIn('research_summary', result)
        self.assertIn('categorization_summary', result)
        self.assertIn('final_report', result)
        self.assertIn('text_report', result)
        self.assertIn('markdown_report', result)
        
        # Verify markdown report contains the 3 sections
        markdown_report = result['markdown_report']
        self.assertIn('## 1. Sources Used', markdown_report)
        self.assertIn('## 2. Speed & Performance Metrics', markdown_report)
        self.assertIn('## 3. Document Content', markdown_report)
        
        print("✅ Full system integration test passed")
        print(f"   Session ID: {result['session_id']}")
        print(f"   Processing time: {result['processing_time']:.2f} seconds")


def run_tests():
    """Run all integration tests."""
    print("="*80)
    print("OVERSIGHT AI INTEGRATION TESTS")
    print("Testing OpenAI integration and markdown output functionality")
    print("="*80)
    
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestOversightAIIntegration)
    runner = unittest.TextTestRunner(verbosity=2)
    
    # Run tests
    result = runner.run(suite)
    
    if result.wasSuccessful():
        print("\n✅ All integration tests passed!")
        print("\nThe system is ready to use with OpenAI integration.")
        print("Make sure to:")
        print("1. Copy .env.example to .env")
        print("2. Add your OpenAI API key to the .env file")
        print("3. Run the system with: python app.py or python run_demo.py")
    else:
        print("\n❌ Some tests failed. Please check the output above.")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)