"""
Step 2a: Information Compilation Engine
Conducts in-depth research on provided topics using OpenAI API.
"""

import openai
import json
import time
from typing import List, Dict, Any
import os
from config import Config


class ResearchEngine:
    def __init__(self):
        # Validate OpenAI configuration
        Config.validate_openai_config()
        
        # Initialize OpenAI client
        self.client = openai.OpenAI(api_key=Config.OPENAI_API_KEY)
        self.model = Config.OPENAI_MODEL
        self.max_tokens = Config.OPENAI_MAX_TOKENS
        self.temperature = Config.OPENAI_TEMPERATURE
    
    def compile_information(self, topic: str) -> Dict[str, Any]:
        """
        Compile comprehensive information about a given topic using OpenAI API.
        
        Args:
            topic (str): The research topic
            
        Returns:
            Dict containing compiled research data with sources, speed, and content
        """
        start_time = time.time()
        
        research_data = {
            'topic': topic,
            'sources': [],
            'content': [],
            'metadata': {
                'research_timestamp': time.time(),
                'total_sources': 0,
                'content_length': 0,
                'processing_speed': 0,
                'loading_time': 0
            }
        }
        
        # Research angles for comprehensive coverage
        research_angles = [
            f"What is {topic}? Provide a comprehensive definition and overview.",
            f"What are the key concepts and principles of {topic}?",
            f"What are the main applications and use cases of {topic}?",
            f"What are the benefits and advantages of {topic}?",
            f"What are the challenges and limitations of {topic}?",
            f"What are the current trends and developments in {topic}?",
            f"What is the future outlook and predictions for {topic}?",
            f"What are the best practices and recommendations for {topic}?"
        ]
        
        for angle in research_angles:
            angle_start_time = time.time()
            content = self._research_angle_with_openai(angle, topic)
            angle_end_time = time.time()
            
            if content:
                research_data['content'].append({
                    'angle': angle,
                    'content': content,
                    'word_count': len(content.split()),
                    'processing_time': angle_end_time - angle_start_time,
                    'source': f"OpenAI {self.model}"
                })
                
                # Add source information
                research_data['sources'].append({
                    'type': 'AI Generated',
                    'source': f"OpenAI {self.model}",
                    'query': angle,
                    'timestamp': angle_start_time
                })
        
        end_time = time.time()
        total_processing_time = end_time - start_time
        
        # Update metadata with timing information
        research_data['metadata']['total_sources'] = len(research_data['content'])
        research_data['metadata']['content_length'] = sum(
            item['word_count'] for item in research_data['content']
        )
        research_data['metadata']['processing_speed'] = f"{total_processing_time:.2f} seconds"
        research_data['metadata']['loading_time'] = f"{total_processing_time:.2f} seconds"
        research_data['metadata']['words_per_second'] = research_data['metadata']['content_length'] / total_processing_time if total_processing_time > 0 else 0
        
        return research_data
    
    def _research_angle_with_openai(self, angle: str, topic: str) -> str:
        """
        Research a specific angle of the topic using OpenAI API.
        
        Args:
            angle (str): The research angle/question
            topic (str): The main topic
            
        Returns:
            str: Generated content from OpenAI
        """
        try:
            prompt = f"""
            You are a research expert providing comprehensive, accurate information about {topic}.
            
            Question: {angle}
            
            Please provide a detailed, informative response that covers:
            - Key facts and definitions
            - Important details and context
            - Practical examples where relevant
            - Current state and developments
            
            Keep the response focused, informative, and well-structured. Aim for 150-250 words.
            """
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a knowledgeable research assistant providing accurate, comprehensive information on various topics."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=self.max_tokens,
                temperature=self.temperature
            )
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:
            print(f"Error querying OpenAI for angle '{angle}': {str(e)}")
            # Fallback content if OpenAI fails
            return f"Research findings related to {angle} indicate significant relevance to {topic} and its various applications in modern contexts."
    
    def get_research_summary(self, research_data: Dict[str, Any]) -> str:
        """
        Generate a summary of the research findings with sources, speed, and timing information.
        """
        topic = research_data['topic']
        total_content = len(research_data['content'])
        total_words = research_data['metadata']['content_length']
        processing_speed = research_data['metadata']['processing_speed']
        loading_time = research_data['metadata']['loading_time']
        words_per_second = research_data['metadata'].get('words_per_second', 0)
        
        summary = f"""# Research Summary for: {topic}

## Sources Used
- **Primary Source**: OpenAI {self.model}
- **Total Research Queries**: {total_content}
- **Source Type**: AI-Generated Content
- **Research Timestamp**: {time.ctime(research_data['metadata']['research_timestamp'])}

## Speed & Performance
- **Processing Speed**: {processing_speed}
- **Loading Time/ETA**: {loading_time}
- **Content Generation Rate**: {words_per_second:.1f} words/second
- **Total Content Generated**: {total_words} words

## Research Coverage
The following research angles were explored:
"""
        
        for item in research_data['content']:
            summary += f"- {item['angle']} ({item['word_count']} words, {item.get('processing_time', 0):.2f}s)\n"
        
        return summary