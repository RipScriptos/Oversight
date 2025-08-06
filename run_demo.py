#!/usr/bin/env python3
"""
Demo script for Oversight AI System
Demonstrates the 3-step AI process with example topics.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.oversight_ai import OversightAI
import json


def run_demo():
    """Run a demonstration of the Oversight AI system."""
    
    print("="*80)
    print("OVERSIGHT AI SYSTEM - DEMONSTRATION")
    print("3-Step Artificial Intelligence for Topic Analysis")
    print("="*80)
    
    # Initialize the system
    oversight_ai = OversightAI()
    
    # Demo topics
    demo_topics = [
        "Artificial Intelligence",
        "Climate Change",
        "Digital Marketing",
        "Renewable Energy",
        "Cybersecurity"
    ]
    
    print("\nAvailable demo topics:")
    for i, topic in enumerate(demo_topics, 1):
        print(f"{i}. {topic}")
    
    print("\nChoose a topic (1-5) or enter your own topic:")
    user_input = input("> ").strip()
    
    # Determine the topic
    if user_input.isdigit() and 1 <= int(user_input) <= len(demo_topics):
        topic = demo_topics[int(user_input) - 1]
    elif user_input:
        topic = user_input
    else:
        topic = demo_topics[0]  # Default to first topic
    
    print(f"\nSelected topic: {topic}")
    
    # Choose report type
    report_types = oversight_ai.get_available_report_types()
    print(f"\nAvailable report types: {', '.join(report_types)}")
    print("Choose report type (or press Enter for 'detailed'):")
    try:
        report_type = input("> ").strip().lower()
    except EOFError:
        report_type = 'detailed'
    
    if report_type not in report_types:
        report_type = 'detailed'
    
    print(f"Selected report type: {report_type}")
    
    print("\n" + "="*80)
    print("STARTING 3-STEP AI PROCESS")
    print("="*80)
    
    # Process the topic
    result = oversight_ai.process_topic(topic, report_type)
    
    if result['success']:
        print(f"\n✅ Analysis completed successfully!")
        print(f"Session ID: {result['session_id']}")
        print(f"Processing time: {result['processing_time']:.2f} seconds")
        
        print("\n" + "-"*60)
        print("RESEARCH SUMMARY")
        print("-"*60)
        print(result['research_summary'])
        
        print("\n" + "-"*60)
        print("CATEGORIZATION SUMMARY")
        print("-"*60)
        print(result['categorization_summary'])
        
        print("\n" + "-"*60)
        print("FINAL REPORT")
        print("-"*60)
        print(result['text_report'])
        
        # Save report to file
        filename = f"oversight_report_{topic.replace(' ', '_')}_{result['session_id']}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(result['text_report'])
        
        print(f"\n📄 Report saved to: {filename}")
        
    else:
        print(f"\n❌ Analysis failed: {result['error']}")
    
    # Show system statistics
    stats = oversight_ai.get_system_statistics()
    print("\n" + "-"*60)
    print("SYSTEM STATISTICS")
    print("-"*60)
    print(f"Total sessions: {stats['total_sessions']}")
    print(f"Successful sessions: {stats['successful_sessions']}")
    print(f"Success rate: {stats['success_rate']:.1f}%")
    print(f"Average processing time: {stats['average_processing_time']:.2f} seconds")
    print(f"Unique topics processed: {stats['unique_topics_processed']}")


if __name__ == "__main__":
    try:
        run_demo()
    except KeyboardInterrupt:
        print("\n\nDemo interrupted by user.")
    except Exception as e:
        print(f"\nError running demo: {str(e)}")
        import traceback
        traceback.print_exc()