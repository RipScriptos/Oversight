"""
Step 2a: Information Compilation Engine
Conducts in-depth research on provided topics to gather relevant information.
"""

import requests
from bs4 import BeautifulSoup
import json
import time
from typing import List, Dict, Any
import re


class ResearchEngine:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def compile_information(self, topic: str) -> Dict[str, Any]:
        """
        Compile comprehensive information about a given topic.
        
        Args:
            topic (str): The research topic
            
        Returns:
            Dict containing compiled research data
        """
        research_data = {
            'topic': topic,
            'sources': [],
            'content': [],
            'metadata': {
                'research_timestamp': time.time(),
                'total_sources': 0,
                'content_length': 0
            }
        }
        
        # Simulate comprehensive research by gathering information from multiple angles
        research_angles = [
            f"What is {topic}",
            f"{topic} definition and overview",
            f"{topic} key concepts and principles",
            f"{topic} applications and use cases",
            f"{topic} benefits and advantages",
            f"{topic} challenges and limitations",
            f"{topic} current trends and developments",
            f"{topic} future outlook and predictions"
        ]
        
        for angle in research_angles:
            content = self._research_angle(angle, topic)
            if content:
                research_data['content'].append({
                    'angle': angle,
                    'content': content,
                    'word_count': len(content.split())
                })
        
        # Update metadata
        research_data['metadata']['total_sources'] = len(research_data['content'])
        research_data['metadata']['content_length'] = sum(
            item['word_count'] for item in research_data['content']
        )
        
        return research_data
    
    def _research_angle(self, angle: str, topic: str) -> str:
        """
        Research a specific angle of the topic.
        In a real implementation, this would query various APIs, databases, or web sources.
        For this demo, we'll generate structured research content.
        """
        
        # Simulate research content based on the angle
        content_templates = {
            "What is": f"{topic} is a comprehensive subject that encompasses various aspects and applications. It represents a field of study and practice that has evolved significantly over time.",
            
            "definition and overview": f"{topic} can be defined as a systematic approach or concept that involves multiple components working together. It has gained prominence due to its practical applications and theoretical foundations.",
            
            "key concepts and principles": f"The fundamental principles of {topic} include systematic methodology, evidence-based approaches, continuous improvement, and stakeholder engagement. These principles guide implementation and best practices.",
            
            "applications and use cases": f"{topic} finds applications across various industries and sectors. Common use cases include process optimization, decision-making support, strategic planning, and performance enhancement.",
            
            "benefits and advantages": f"Key benefits of {topic} include improved efficiency, better decision-making capabilities, enhanced productivity, cost reduction, and competitive advantage in the marketplace.",
            
            "challenges and limitations": f"Common challenges in {topic} include implementation complexity, resource requirements, skill gaps, resistance to change, and the need for ongoing maintenance and updates.",
            
            "current trends and developments": f"Current trends in {topic} include digital transformation, automation integration, data-driven approaches, sustainability considerations, and emerging technology adoption.",
            
            "future outlook and predictions": f"The future of {topic} looks promising with continued innovation, increased adoption rates, integration with emerging technologies, and expansion into new application areas."
        }
        
        # Find matching template
        for key, template in content_templates.items():
            if key in angle.lower():
                return template
        
        # Default content if no specific template matches
        return f"Research findings related to {angle} indicate significant relevance to {topic} and its various applications in modern contexts."
    
    def _extract_text_from_url(self, url: str) -> str:
        """
        Extract text content from a web URL.
        """
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()
            
            # Get text and clean it
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = ' '.join(chunk for chunk in chunks if chunk)
            
            return text[:5000]  # Limit to first 5000 characters
            
        except Exception as e:
            print(f"Error extracting text from {url}: {str(e)}")
            return ""
    
    def get_research_summary(self, research_data: Dict[str, Any]) -> str:
        """
        Generate a summary of the research findings.
        """
        topic = research_data['topic']
        total_content = len(research_data['content'])
        total_words = research_data['metadata']['content_length']
        
        summary = f"""
Research Summary for: {topic}

Total Research Angles Explored: {total_content}
Total Content Generated: {total_words} words
Research Timestamp: {time.ctime(research_data['metadata']['research_timestamp'])}

Key Areas Covered:
"""
        
        for item in research_data['content']:
            summary += f"- {item['angle']} ({item['word_count']} words)\n"
        
        return summary