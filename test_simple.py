#!/usr/bin/env python3
"""
Simple test script for Oversight AI System components
Tests individual components without requiring OpenAI API key.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.report_generator import ReportGenerator


def test_markdown_export():
    """Test the markdown export functionality."""
    print("Testing markdown export functionality...")
    
    # Create sample report data
    sample_report_data = {
        'metadata': {
            'topic': 'Artificial Intelligence',
            'report_type': 'detailed',
            'generation_timestamp': '2023-12-01T10:30:00',
            'total_sources_analyzed': 8,
            'categorization_confidence': 0.87
        },
        'content': {
            'introduction': """
COMPREHENSIVE ANALYSIS: ARTIFICIAL INTELLIGENCE

This detailed report presents a thorough analysis of Artificial Intelligence, organized by information priority and relevance. The analysis covers fundamental concepts, practical applications, benefits, challenges, and future outlook.

METHODOLOGY:
Our analysis employed a systematic approach to information gathering and categorization, utilizing advanced algorithms to assess the importance and relevance of each piece of information.
""",
            'critical_information': {
                'title': 'CRITICAL INFORMATION',
                'description': 'The following information represents the most essential aspects of the topic:',
                'item_count': 3,
                'items': [
                    {
                        'research_angle': 'What is Artificial Intelligence? Provide a comprehensive definition and overview.',
                        'content': 'Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn like humans. It encompasses various technologies including machine learning, natural language processing, computer vision, and robotics.',
                        'importance_score': '0.95',
                        'key_indicators': ['definition', 'overview', 'core concepts'],
                        'reasoning': 'Fundamental definition essential for understanding'
                    }
                ]
            },
            'important_information': {
                'title': 'IMPORTANT INFORMATION',
                'description': 'This section covers significant information that enhances understanding:',
                'item_count': 2,
                'items': [
                    {
                        'research_angle': 'What are the main applications and use cases of Artificial Intelligence?',
                        'content': 'AI applications span across healthcare (diagnosis, drug discovery), finance (fraud detection, algorithmic trading), transportation (autonomous vehicles), and entertainment (recommendation systems).',
                        'importance_score': '0.82',
                        'key_indicators': ['applications', 'use cases', 'practical'],
                        'reasoning': 'Real-world applications demonstrate practical value'
                    }
                ]
            }
        },
        'appendices': {
            'methodology': 'Multi-angle systematic research approach with AI-powered analysis',
            'quality_metrics': {
                'overall_confidence': '87%',
                'processing_completeness': '100%',
                'data_reliability': 'High'
            }
        }
    }
    
    # Test markdown export
    report_generator = ReportGenerator()
    markdown_output = report_generator.export_report_as_markdown(sample_report_data)
    
    # Verify structure
    required_sections = [
        '# Artificial Intelligence - Detailed Report',
        '## 1. Sources Used',
        '## 2. Speed & Performance Metrics', 
        '## 3. Document Content',
        '### Introduction',
        '### Critical Information',
        '### Important Information',
        '## Appendices'
    ]
    
    missing_sections = []
    for section in required_sections:
        if section not in markdown_output:
            missing_sections.append(section)
    
    if missing_sections:
        print(f"❌ Missing sections: {missing_sections}")
        return False
    
    # Save sample output
    with open('sample_markdown_report.md', 'w', encoding='utf-8') as f:
        f.write(markdown_output)
    
    print("✅ Markdown export test passed!")
    print("📄 Sample report saved as: sample_markdown_report.md")
    
    # Show preview
    print("\n" + "="*60)
    print("MARKDOWN REPORT PREVIEW (first 500 characters):")
    print("="*60)
    print(markdown_output[:500] + "...")
    
    return True


def test_config_structure():
    """Test configuration structure."""
    print("\nTesting configuration structure...")
    
    try:
        from config import Config
        
        # Check required attributes
        required_attrs = ['OPENAI_API_KEY', 'OPENAI_MODEL', 'OPENAI_MAX_TOKENS', 'OPENAI_TEMPERATURE']
        
        for attr in required_attrs:
            if not hasattr(Config, attr):
                print(f"❌ Missing config attribute: {attr}")
                return False
        
        print("✅ Configuration structure test passed!")
        print(f"   Default model: {Config.OPENAI_MODEL}")
        print(f"   Max tokens: {Config.OPENAI_MAX_TOKENS}")
        print(f"   Temperature: {Config.OPENAI_TEMPERATURE}")
        
        return True
        
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False


def main():
    """Run all simple tests."""
    print("="*80)
    print("OVERSIGHT AI - SIMPLE COMPONENT TESTS")
    print("Testing core functionality without OpenAI API requirements")
    print("="*80)
    
    tests = [
        test_config_structure,
        test_markdown_export
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test {test.__name__} failed with error: {e}")
    
    print("\n" + "="*80)
    print(f"TEST RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("✅ All tests passed! The system components are working correctly.")
        print("\nNext steps:")
        print("1. Copy .env.example to .env")
        print("2. Add your OpenAI API key to the .env file")
        print("3. Run: python app.py (for web interface)")
        print("4. Or run: python run_demo.py (for command line demo)")
    else:
        print("❌ Some tests failed. Please check the output above.")
    
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)