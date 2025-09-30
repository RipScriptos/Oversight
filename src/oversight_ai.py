"""
Oversight AI System - Main Controller
Orchestrates the 3-step AI process for topic research and report generation.
"""

from typing import Dict, Any, Optional, List
import json
import time
from .research_engine import ResearchEngine
from .information_architect import InformationArchitect
from .report_generator import ReportGenerator


class OversightAI:
    """
    Main controller for the 3-Step Artificial Intelligence system.
    
    Process Flow:
    1. Topic Input: User provides a topic for research
    2. Information Processing:
       a. Compile Information: In-depth research on the topic
       b. Categorize Text: Information architect categorizes importance
    3. Output Generation: Generate final informative report
    """
    
    def __init__(self):
        self.research_engine = ResearchEngine()
        self.information_architect = InformationArchitect()
        self.report_generator = ReportGenerator()
        
        self.processing_history = []
        self.current_session = None
    
    def process_topic(self, topic: str, report_type: str = 'detailed') -> Dict[str, Any]:
        """
        Execute the complete 3-step AI process for a given topic.
        
        Args:
            topic (str): The research topic
            report_type (str): Type of report to generate
            
        Returns:
            Dict containing the complete processing results
        """
        session_id = f"session_{int(time.time())}"
        
        # Initialize session
        session_data = {
            'session_id': session_id,
            'topic': topic,
            'report_type': report_type,
            'start_time': time.time(),
            'steps_completed': [],
            'results': {}
        }
        
        self.current_session = session_data
        
        try:
            # Step 1: Topic Input (validation and preparation)
            print(f"Step 1: Processing topic input - '{topic}'")
            validated_topic = self._validate_and_prepare_topic(topic)
            session_data['steps_completed'].append('topic_input')
            session_data['results']['validated_topic'] = validated_topic
            
            # Step 2a: Compile Information
            print("Step 2a: Compiling information...")
            research_data = self.research_engine.compile_information(validated_topic)
            session_data['steps_completed'].append('information_compilation')
            session_data['results']['research_data'] = research_data
            
            # Step 2b: Categorize Information
            print("Step 2b: Categorizing information...")
            categorized_data = self.information_architect.categorize_information(research_data)
            session_data['steps_completed'].append('information_categorization')
            session_data['results']['categorized_data'] = categorized_data
            
            # Step 3: Generate Report
            print("Step 3: Generating final report...")
            final_report = self.report_generator.generate_report(categorized_data, report_type)
            session_data['steps_completed'].append('report_generation')
            session_data['results']['final_report'] = final_report
            
            # Complete session
            session_data['end_time'] = time.time()
            session_data['processing_time'] = session_data['end_time'] - session_data['start_time']
            session_data['status'] = 'completed'
            
            # Add to history
            self.processing_history.append(session_data)
            
            print(f"Processing completed in {session_data['processing_time']:.2f} seconds")
            
            return {
                'success': True,
                'session_id': session_id,
                'topic': topic,
                'report_type': report_type,
                'processing_time': session_data['processing_time'],
                'research_summary': self.research_engine.get_research_summary(research_data),
                'categorization_summary': self.information_architect.get_categorization_summary(categorized_data),
                'final_report': final_report,
                'text_report': self.report_generator.export_report_as_text(final_report),
                'markdown_report': self.report_generator.export_report_as_markdown(final_report)
            }
            
        except Exception as e:
            session_data['status'] = 'failed'
            session_data['error'] = str(e)
            session_data['end_time'] = time.time()
            
            print(f"Processing failed: {str(e)}")
            
            return {
                'success': False,
                'session_id': session_id,
                'error': str(e),
                'steps_completed': session_data['steps_completed']
            }
    
    def _validate_and_prepare_topic(self, topic: str) -> str:
        """
        Validate and prepare the input topic for processing.
        """
        if not topic or not topic.strip():
            raise ValueError("Topic cannot be empty")
        
        # Clean and normalize the topic
        cleaned_topic = topic.strip()
        
        # Basic validation
        if len(cleaned_topic) < 2:
            raise ValueError("Topic must be at least 2 characters long")
        
        if len(cleaned_topic) > 200:
            raise ValueError("Topic must be less than 200 characters")
        
        return cleaned_topic
    
    def get_processing_status(self, session_id: str) -> Optional[Dict[str, Any]]:
        """
        Get the processing status for a specific session.
        """
        for session in self.processing_history:
            if session['session_id'] == session_id:
                return {
                    'session_id': session_id,
                    'topic': session['topic'],
                    'status': session.get('status', 'processing'),
                    'steps_completed': session['steps_completed'],
                    'processing_time': session.get('processing_time', 0)
                }
        return None
    
    def get_session_results(self, session_id: str) -> Optional[Dict[str, Any]]:
        """
        Get the complete results for a specific session.
        """
        for session in self.processing_history:
            if session['session_id'] == session_id:
                return session['results']
        return None
    
    def list_processing_history(self) -> List[Dict[str, Any]]:
        """
        Get a list of all processing sessions.
        """
        history_summary = []
        for session in self.processing_history:
            summary = {
                'session_id': session['session_id'],
                'topic': session['topic'],
                'report_type': session.get('report_type', 'detailed'),
                'status': session.get('status', 'unknown'),
                'processing_time': session.get('processing_time', 0),
                'timestamp': session['start_time']
            }
            history_summary.append(summary)
        
        return history_summary
    
    def export_session_data(self, session_id: str, format: str = 'json') -> Optional[str]:
        """
        Export session data in the specified format.
        """
        session_data = None
        for session in self.processing_history:
            if session['session_id'] == session_id:
                session_data = session
                break
        
        if not session_data:
            return None
        
        if format.lower() == 'json':
            return json.dumps(session_data, indent=2, default=str)
        elif format.lower() == 'text' and 'final_report' in session_data.get('results', {}):
            return self.report_generator.export_report_as_text(
                session_data['results']['final_report']
            )
        elif format.lower() == 'markdown' and 'final_report' in session_data.get('results', {}):
            return self.report_generator.export_report_as_markdown(
                session_data['results']['final_report']
            )
        else:
            return str(session_data)
    
    def get_system_statistics(self) -> Dict[str, Any]:
        """
        Get system usage statistics.
        """
        total_sessions = len(self.processing_history)
        successful_sessions = sum(1 for s in self.processing_history if s.get('status') == 'completed')
        failed_sessions = total_sessions - successful_sessions
        
        if total_sessions > 0:
            avg_processing_time = sum(
                s.get('processing_time', 0) for s in self.processing_history
            ) / total_sessions
        else:
            avg_processing_time = 0
        
        # Topic analysis
        topics_processed = [s['topic'] for s in self.processing_history]
        unique_topics = len(set(topics_processed))
        
        return {
            'total_sessions': total_sessions,
            'successful_sessions': successful_sessions,
            'failed_sessions': failed_sessions,
            'success_rate': (successful_sessions / total_sessions * 100) if total_sessions > 0 else 0,
            'average_processing_time': avg_processing_time,
            'unique_topics_processed': unique_topics,
            'total_topics_processed': len(topics_processed)
        }
    
    def clear_history(self) -> None:
        """
        Clear the processing history.
        """
        self.processing_history = []
        self.current_session = None
    
    def get_available_report_types(self) -> List[str]:
        """
        Get list of available report types.
        """
        return list(self.report_generator.report_templates.keys())
    
    def validate_report_type(self, report_type: str) -> bool:
        """
        Validate if the report type is supported.
        """
        return report_type in self.report_generator.report_templates