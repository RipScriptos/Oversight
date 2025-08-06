#!/usr/bin/env python3
"""
Test script for Oversight AI System
Tests the 3-step AI process with various topics and report types.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.oversight_ai import OversightAI
import json


def test_system():
    """Test the Oversight AI system with different scenarios."""
    
    print("="*80)
    print("OVERSIGHT AI SYSTEM - COMPREHENSIVE TEST")
    print("="*80)
    
    # Initialize the system
    oversight_ai = OversightAI()
    
    # Test scenarios
    test_cases = [
        {"topic": "Artificial Intelligence", "report_type": "summary"},
        {"topic": "Climate Change", "report_type": "executive"},
        {"topic": "Digital Marketing", "report_type": "detailed"},
        {"topic": "Cybersecurity", "report_type": "technical"}
    ]
    
    results = []
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n{'='*60}")
        print(f"TEST CASE {i}: {test_case['topic']} ({test_case['report_type']})")
        print(f"{'='*60}")
        
        try:
            result = oversight_ai.process_topic(
                test_case['topic'], 
                test_case['report_type']
            )
            
            if result['success']:
                print(f"✅ SUCCESS - Session: {result['session_id']}")
                print(f"   Processing time: {result['processing_time']:.2f}s")
                print(f"   Report type: {result['report_type']}")
                
                # Save brief summary
                results.append({
                    'test_case': i,
                    'topic': test_case['topic'],
                    'report_type': test_case['report_type'],
                    'success': True,
                    'session_id': result['session_id'],
                    'processing_time': result['processing_time']
                })
                
                # Show brief excerpt from report
                text_report = result['text_report']
                lines = text_report.split('\n')
                excerpt_lines = [line for line in lines[:20] if line.strip()]
                print(f"   Report excerpt:")
                for line in excerpt_lines[:5]:
                    print(f"   {line}")
                print("   ...")
                
            else:
                print(f"❌ FAILED - {result['error']}")
                results.append({
                    'test_case': i,
                    'topic': test_case['topic'],
                    'report_type': test_case['report_type'],
                    'success': False,
                    'error': result['error']
                })
                
        except Exception as e:
            print(f"❌ EXCEPTION - {str(e)}")
            results.append({
                'test_case': i,
                'topic': test_case['topic'],
                'report_type': test_case['report_type'],
                'success': False,
                'error': str(e)
            })
    
    # Summary
    print(f"\n{'='*80}")
    print("TEST SUMMARY")
    print(f"{'='*80}")
    
    successful_tests = sum(1 for r in results if r['success'])
    total_tests = len(results)
    
    print(f"Total tests: {total_tests}")
    print(f"Successful: {successful_tests}")
    print(f"Failed: {total_tests - successful_tests}")
    print(f"Success rate: {(successful_tests/total_tests)*100:.1f}%")
    
    if successful_tests > 0:
        avg_time = sum(r.get('processing_time', 0) for r in results if r['success']) / successful_tests
        print(f"Average processing time: {avg_time:.2f}s")
    
    # System statistics
    stats = oversight_ai.get_system_statistics()
    print(f"\nSystem Statistics:")
    print(f"- Total sessions: {stats['total_sessions']}")
    print(f"- Success rate: {stats['success_rate']:.1f}%")
    print(f"- Unique topics: {stats['unique_topics_processed']}")
    
    # Available features
    print(f"\nAvailable Features:")
    print(f"- Report types: {', '.join(oversight_ai.get_available_report_types())}")
    
    return results


def test_individual_components():
    """Test individual components of the system."""
    
    print(f"\n{'='*80}")
    print("COMPONENT TESTING")
    print(f"{'='*80}")
    
    from src.research_engine import ResearchEngine
    from src.information_architect import InformationArchitect
    from src.report_generator import ReportGenerator
    
    # Test Research Engine
    print("\n1. Testing Research Engine...")
    research_engine = ResearchEngine()
    research_data = research_engine.compile_information("Machine Learning")
    print(f"   ✅ Research completed: {len(research_data['content'])} angles explored")
    
    # Test Information Architect
    print("\n2. Testing Information Architect...")
    info_architect = InformationArchitect()
    categorized_data = info_architect.categorize_information(research_data)
    high_priority = len(categorized_data['important_information']['high_priority'])
    medium_priority = len(categorized_data['important_information']['medium_priority'])
    print(f"   ✅ Categorization completed: {high_priority} high, {medium_priority} medium priority items")
    
    # Test Report Generator
    print("\n3. Testing Report Generator...")
    report_generator = ReportGenerator()
    final_report = report_generator.generate_report(categorized_data, 'summary')
    print(f"   ✅ Report generated: {final_report['metadata']['report_type']} type")
    
    print("\n✅ All components working correctly!")


if __name__ == "__main__":
    try:
        # Test individual components first
        test_individual_components()
        
        # Then test the full system
        results = test_system()
        
        print(f"\n{'='*80}")
        print("ALL TESTS COMPLETED")
        print(f"{'='*80}")
        
    except KeyboardInterrupt:
        print("\n\nTesting interrupted by user.")
    except Exception as e:
        print(f"\nError during testing: {str(e)}")
        import traceback
        traceback.print_exc()