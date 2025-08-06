"""
Step 2b: Information Architect
Categorizes compiled information into important and minorly important information.
"""

import re
from typing import Dict, List, Any, Tuple


class InformationArchitect:
    def __init__(self):
        self.importance_keywords = {
            'high': [
                'fundamental', 'essential', 'critical', 'key', 'primary', 'main', 'core',
                'significant', 'major', 'important', 'crucial', 'vital', 'central',
                'principal', 'basic', 'foundation', 'framework', 'strategy', 'approach',
                'methodology', 'system', 'process', 'implementation', 'benefits',
                'advantages', 'impact', 'results', 'outcomes', 'effectiveness'
            ],
            'medium': [
                'relevant', 'useful', 'helpful', 'applicable', 'practical', 'common',
                'typical', 'standard', 'regular', 'normal', 'general', 'broad',
                'wide', 'extensive', 'comprehensive', 'detailed', 'specific',
                'particular', 'individual', 'unique', 'special', 'notable'
            ],
            'low': [
                'minor', 'small', 'limited', 'restricted', 'narrow', 'simple',
                'basic', 'elementary', 'preliminary', 'initial', 'introductory',
                'supplementary', 'additional', 'extra', 'optional', 'alternative',
                'secondary', 'supporting', 'background', 'contextual', 'historical'
            ]
        }
    
    def categorize_information(self, research_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Categorize research information into important and minorly important categories.
        
        Args:
            research_data: Output from ResearchEngine.compile_information()
            
        Returns:
            Dict containing categorized information
        """
        categorized_data = {
            'topic': research_data['topic'],
            'important_information': {
                'high_priority': [],
                'medium_priority': []
            },
            'minor_information': {
                'low_priority': [],
                'supplementary': []
            },
            'categorization_metadata': {
                'total_items_processed': len(research_data['content']),
                'categorization_method': 'hybrid_scoring',
                'confidence_scores': {}
            }
        }
        
        # Process each content item
        for item in research_data['content']:
            category_info = self._analyze_content_importance(item)
            
            # Categorize based on importance score
            if category_info['importance_score'] >= 0.7:
                categorized_data['important_information']['high_priority'].append({
                    'content': item,
                    'importance_score': category_info['importance_score'],
                    'reasoning': category_info['reasoning'],
                    'key_indicators': category_info['key_indicators']
                })
            elif category_info['importance_score'] >= 0.4:
                categorized_data['important_information']['medium_priority'].append({
                    'content': item,
                    'importance_score': category_info['importance_score'],
                    'reasoning': category_info['reasoning'],
                    'key_indicators': category_info['key_indicators']
                })
            elif category_info['importance_score'] >= 0.2:
                categorized_data['minor_information']['low_priority'].append({
                    'content': item,
                    'importance_score': category_info['importance_score'],
                    'reasoning': category_info['reasoning'],
                    'key_indicators': category_info['key_indicators']
                })
            else:
                categorized_data['minor_information']['supplementary'].append({
                    'content': item,
                    'importance_score': category_info['importance_score'],
                    'reasoning': category_info['reasoning'],
                    'key_indicators': category_info['key_indicators']
                })
        
        # Calculate confidence scores
        self._calculate_confidence_scores(categorized_data)
        
        return categorized_data
    
    def _analyze_content_importance(self, content_item: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze the importance of a single content item.
        """
        text = content_item['content'].lower()
        angle = content_item['angle'].lower()
        
        # Initialize scoring components
        keyword_score = 0
        position_score = 0
        length_score = 0
        angle_score = 0
        
        # Keyword-based scoring
        high_count = sum(1 for keyword in self.importance_keywords['high'] if keyword in text)
        medium_count = sum(1 for keyword in self.importance_keywords['medium'] if keyword in text)
        low_count = sum(1 for keyword in self.importance_keywords['low'] if keyword in text)
        
        keyword_score = (high_count * 1.0 + medium_count * 0.6 + low_count * 0.2) / 10
        
        # Angle-based scoring (certain research angles are inherently more important)
        important_angles = ['definition', 'key concepts', 'principles', 'benefits', 'applications']
        angle_score = 0.8 if any(important_angle in angle for important_angle in important_angles) else 0.3
        
        # Length-based scoring (longer content might be more comprehensive)
        word_count = content_item['word_count']
        if word_count > 100:
            length_score = 0.8
        elif word_count > 50:
            length_score = 0.5
        else:
            length_score = 0.2
        
        # Combine scores with weights
        importance_score = (
            keyword_score * 0.4 +
            angle_score * 0.4 +
            length_score * 0.2
        )
        
        # Normalize to 0-1 range
        importance_score = min(1.0, max(0.0, importance_score))
        
        # Generate reasoning
        reasoning = self._generate_importance_reasoning(
            keyword_score, angle_score, length_score, importance_score
        )
        
        # Identify key indicators
        key_indicators = []
        if high_count > 0:
            key_indicators.append(f"Contains {high_count} high-importance keywords")
        if any(important_angle in angle for important_angle in ['definition', 'key concepts', 'principles']):
            key_indicators.append("Covers fundamental concepts")
        if word_count > 100:
            key_indicators.append("Comprehensive content length")
        
        return {
            'importance_score': importance_score,
            'reasoning': reasoning,
            'key_indicators': key_indicators,
            'score_breakdown': {
                'keyword_score': keyword_score,
                'angle_score': angle_score,
                'length_score': length_score
            }
        }
    
    def _generate_importance_reasoning(self, keyword_score: float, angle_score: float, 
                                     length_score: float, final_score: float) -> str:
        """
        Generate human-readable reasoning for the importance categorization.
        """
        if final_score >= 0.7:
            return "High importance due to strong keyword relevance and fundamental topic coverage."
        elif final_score >= 0.4:
            return "Medium importance with good keyword coverage and relevant content angle."
        elif final_score >= 0.2:
            return "Lower importance but still relevant for comprehensive understanding."
        else:
            return "Supplementary information that provides additional context."
    
    def _calculate_confidence_scores(self, categorized_data: Dict[str, Any]) -> None:
        """
        Calculate confidence scores for the categorization process.
        """
        total_items = categorized_data['categorization_metadata']['total_items_processed']
        
        high_priority_count = len(categorized_data['important_information']['high_priority'])
        medium_priority_count = len(categorized_data['important_information']['medium_priority'])
        low_priority_count = len(categorized_data['minor_information']['low_priority'])
        supplementary_count = len(categorized_data['minor_information']['supplementary'])
        
        # Calculate distribution confidence (good distribution indicates reliable categorization)
        distribution_balance = 1.0 - abs(0.25 - (high_priority_count / total_items)) * 2
        distribution_balance = max(0.0, min(1.0, distribution_balance))
        
        categorized_data['categorization_metadata']['confidence_scores'] = {
            'overall_confidence': distribution_balance,
            'distribution': {
                'high_priority': high_priority_count / total_items,
                'medium_priority': medium_priority_count / total_items,
                'low_priority': low_priority_count / total_items,
                'supplementary': supplementary_count / total_items
            }
        }
    
    def get_categorization_summary(self, categorized_data: Dict[str, Any]) -> str:
        """
        Generate a summary of the categorization results.
        """
        topic = categorized_data['topic']
        high_count = len(categorized_data['important_information']['high_priority'])
        medium_count = len(categorized_data['important_information']['medium_priority'])
        low_count = len(categorized_data['minor_information']['low_priority'])
        supp_count = len(categorized_data['minor_information']['supplementary'])
        
        confidence = categorized_data['categorization_metadata']['confidence_scores']['overall_confidence']
        
        summary = f"""
Information Categorization Summary for: {topic}

Categorization Results:
- High Priority Information: {high_count} items
- Medium Priority Information: {medium_count} items
- Low Priority Information: {low_count} items
- Supplementary Information: {supp_count} items

Overall Categorization Confidence: {confidence:.2%}

Distribution Analysis:
- Important Information: {high_count + medium_count} items ({((high_count + medium_count) / (high_count + medium_count + low_count + supp_count) * 100):.1f}%)
- Minor Information: {low_count + supp_count} items ({((low_count + supp_count) / (high_count + medium_count + low_count + supp_count) * 100):.1f}%)
"""
        
        return summary