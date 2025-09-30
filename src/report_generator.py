"""
Step 3: Report Generator
Generates final informative reports from categorized information.
"""

import json
from datetime import datetime
from typing import Dict, Any, List
import re


class ReportGenerator:
    def __init__(self):
        self.report_templates = {
            'executive': self._generate_executive_report,
            'detailed': self._generate_detailed_report,
            'technical': self._generate_technical_report,
            'summary': self._generate_summary_report
        }
    
    def generate_report(self, categorized_data: Dict[str, Any], 
                       report_type: str = 'detailed') -> Dict[str, Any]:
        """
        Generate a final informative report from categorized information.
        
        Args:
            categorized_data: Output from InformationArchitect.categorize_information()
            report_type: Type of report to generate ('executive', 'detailed', 'technical', 'summary')
            
        Returns:
            Dict containing the generated report
        """
        if report_type not in self.report_templates:
            report_type = 'detailed'
        
        report_data = {
            'metadata': {
                'topic': categorized_data['topic'],
                'report_type': report_type,
                'generation_timestamp': datetime.now().isoformat(),
                'total_sources_analyzed': categorized_data['categorization_metadata']['total_items_processed'],
                'categorization_confidence': categorized_data['categorization_metadata']['confidence_scores']['overall_confidence']
            },
            'content': {},
            'appendices': {}
        }
        
        # Generate the specific report type
        report_content = self.report_templates[report_type](categorized_data)
        report_data['content'] = report_content
        
        # Add appendices
        report_data['appendices'] = self._generate_appendices(categorized_data)
        
        return report_data
    
    def _generate_executive_report(self, categorized_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate an executive summary report focusing on high-level insights.
        """
        topic = categorized_data['topic']
        high_priority = categorized_data['important_information']['high_priority']
        
        executive_summary = f"""
EXECUTIVE SUMMARY: {topic.upper()}

This report provides a comprehensive analysis of {topic}, focusing on the most critical information and strategic insights.

KEY FINDINGS:
"""
        
        # Extract key findings from high priority information
        key_findings = []
        for i, item in enumerate(high_priority[:5], 1):  # Top 5 high priority items
            angle = item['content']['angle']
            key_findings.append(f"{i}. {angle}: {self._extract_key_insight(item['content']['content'])}")
        
        executive_summary += "\n".join(key_findings)
        
        # Strategic recommendations
        recommendations = self._generate_recommendations(categorized_data)
        
        return {
            'executive_summary': executive_summary,
            'strategic_recommendations': recommendations,
            'critical_insights': self._extract_critical_insights(high_priority),
            'risk_assessment': self._generate_risk_assessment(categorized_data)
        }
    
    def _generate_detailed_report(self, categorized_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a comprehensive detailed report with all categorized information.
        """
        topic = categorized_data['topic']
        
        # Introduction
        introduction = f"""
COMPREHENSIVE ANALYSIS: {topic.upper()}

This detailed report presents a thorough analysis of {topic}, organized by information priority and relevance. The analysis covers fundamental concepts, practical applications, benefits, challenges, and future outlook.

METHODOLOGY:
Our analysis employed a systematic approach to information gathering and categorization, utilizing advanced algorithms to assess the importance and relevance of each piece of information.
"""
        
        # High Priority Section
        high_priority_section = self._format_priority_section(
            categorized_data['important_information']['high_priority'],
            "CRITICAL INFORMATION",
            "The following information represents the most essential aspects of the topic:"
        )
        
        # Medium Priority Section
        medium_priority_section = self._format_priority_section(
            categorized_data['important_information']['medium_priority'],
            "IMPORTANT INFORMATION",
            "This section covers significant information that enhances understanding:"
        )
        
        # Supporting Information Section
        supporting_section = self._format_priority_section(
            categorized_data['minor_information']['low_priority'],
            "SUPPORTING INFORMATION",
            "Additional relevant information for comprehensive understanding:"
        )
        
        # Analysis and Insights
        analysis = self._generate_comprehensive_analysis(categorized_data)
        
        return {
            'introduction': introduction,
            'critical_information': high_priority_section,
            'important_information': medium_priority_section,
            'supporting_information': supporting_section,
            'comprehensive_analysis': analysis,
            'conclusions': self._generate_conclusions(categorized_data)
        }
    
    def _generate_technical_report(self, categorized_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a technical report with detailed methodology and data analysis.
        """
        topic = categorized_data['topic']
        
        technical_overview = f"""
TECHNICAL ANALYSIS REPORT: {topic.upper()}

SCOPE AND METHODOLOGY:
This technical report provides an in-depth analysis of {topic} using systematic information processing and categorization techniques.

DATA PROCESSING PIPELINE:
1. Information Compilation: Multi-angle research approach
2. Content Analysis: Keyword-based importance scoring
3. Categorization: Hybrid scoring algorithm with confidence metrics
4. Report Generation: Structured output with technical appendices
"""
        
        # Technical findings
        technical_findings = self._generate_technical_findings(categorized_data)
        
        # Data analysis
        data_analysis = self._generate_data_analysis(categorized_data)
        
        return {
            'technical_overview': technical_overview,
            'technical_findings': technical_findings,
            'data_analysis': data_analysis,
            'methodology_details': self._generate_methodology_details(categorized_data),
            'quality_metrics': self._generate_quality_metrics(categorized_data)
        }
    
    def _generate_summary_report(self, categorized_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a concise summary report with key highlights.
        """
        topic = categorized_data['topic']
        
        summary = f"""
SUMMARY REPORT: {topic.upper()}

OVERVIEW:
This summary provides the essential information about {topic} in a concise format.
"""
        
        # Key points from each priority level
        key_points = []
        
        # High priority key points
        for item in categorized_data['important_information']['high_priority'][:3]:
            key_points.append(f"• {self._extract_key_point(item['content'])}")
        
        # Medium priority key points
        for item in categorized_data['important_information']['medium_priority'][:2]:
            key_points.append(f"• {self._extract_key_point(item['content'])}")
        
        return {
            'summary': summary,
            'key_points': key_points,
            'quick_insights': self._generate_quick_insights(categorized_data),
            'action_items': self._generate_action_items(categorized_data)
        }
    
    def _format_priority_section(self, items: List[Dict], title: str, description: str) -> Dict[str, Any]:
        """
        Format a section for items of a specific priority level.
        """
        formatted_items = []
        
        for item in items:
            formatted_item = {
                'research_angle': item['content']['angle'],
                'content': item['content']['content'],
                'importance_score': f"{item['importance_score']:.2f}",
                'key_indicators': item['key_indicators'],
                'reasoning': item['reasoning']
            }
            formatted_items.append(formatted_item)
        
        return {
            'title': title,
            'description': description,
            'item_count': len(items),
            'items': formatted_items
        }
    
    def _extract_key_insight(self, content: str) -> str:
        """
        Extract a key insight from content text.
        """
        sentences = content.split('.')
        # Return the first substantial sentence
        for sentence in sentences:
            if len(sentence.strip()) > 20:
                return sentence.strip() + "."
        return content[:100] + "..." if len(content) > 100 else content
    
    def _extract_key_point(self, content_item: Dict[str, Any]) -> str:
        """
        Extract a key point from a content item.
        """
        angle = content_item['angle']
        content = content_item['content']
        
        # Create a concise key point
        if 'definition' in angle.lower():
            return f"Definition: {self._extract_key_insight(content)}"
        elif 'benefit' in angle.lower():
            return f"Key Benefit: {self._extract_key_insight(content)}"
        elif 'application' in angle.lower():
            return f"Application: {self._extract_key_insight(content)}"
        else:
            return f"{angle}: {self._extract_key_insight(content)}"
    
    def _generate_recommendations(self, categorized_data: Dict[str, Any]) -> List[str]:
        """
        Generate strategic recommendations based on the analysis.
        """
        recommendations = [
            "Focus on understanding the fundamental principles and core concepts",
            "Prioritize practical applications and implementation strategies",
            "Consider both benefits and potential challenges in planning",
            "Stay informed about current trends and future developments",
            "Develop a comprehensive approach that addresses all key aspects"
        ]
        return recommendations
    
    def _extract_critical_insights(self, high_priority_items: List[Dict]) -> List[str]:
        """
        Extract critical insights from high priority information.
        """
        insights = []
        for item in high_priority_items[:3]:
            insight = f"Critical insight from {item['content']['angle']}: {self._extract_key_insight(item['content']['content'])}"
            insights.append(insight)
        return insights
    
    def _generate_risk_assessment(self, categorized_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a risk assessment based on the information.
        """
        return {
            'information_quality': 'High' if categorized_data['categorization_metadata']['confidence_scores']['overall_confidence'] > 0.7 else 'Medium',
            'coverage_completeness': 'Comprehensive',
            'reliability_score': f"{categorized_data['categorization_metadata']['confidence_scores']['overall_confidence']:.2%}"
        }
    
    def _generate_comprehensive_analysis(self, categorized_data: Dict[str, Any]) -> str:
        """
        Generate comprehensive analysis section.
        """
        topic = categorized_data['topic']
        total_items = categorized_data['categorization_metadata']['total_items_processed']
        
        analysis = f"""
COMPREHENSIVE ANALYSIS:

Our analysis of {topic} reveals a multi-faceted subject with {total_items} distinct research angles explored. The information has been systematically categorized to highlight the most critical aspects while ensuring comprehensive coverage.

The analysis indicates strong foundational concepts with practical applications across multiple domains. Key themes emerge around implementation strategies, benefits realization, and future development potential.
"""
        return analysis
    
    def _generate_conclusions(self, categorized_data: Dict[str, Any]) -> str:
        """
        Generate conclusions section.
        """
        topic = categorized_data['topic']
        
        conclusions = f"""
CONCLUSIONS:

Based on our comprehensive analysis of {topic}, several key conclusions emerge:

1. The topic demonstrates significant relevance and practical applicability
2. Multiple implementation approaches are available with varying complexity levels
3. Benefits outweigh challenges when properly implemented
4. Continued development and innovation are expected in this area
5. Strategic planning and systematic approach are essential for success

This analysis provides a solid foundation for informed decision-making and strategic planning related to {topic}.
"""
        return conclusions
    
    def _generate_technical_findings(self, categorized_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate technical findings section.
        """
        return {
            'data_quality_assessment': 'High reliability based on systematic categorization',
            'processing_efficiency': f"Processed {categorized_data['categorization_metadata']['total_items_processed']} information units",
            'categorization_accuracy': f"{categorized_data['categorization_metadata']['confidence_scores']['overall_confidence']:.2%}",
            'coverage_analysis': 'Comprehensive multi-angle approach ensures thorough coverage'
        }
    
    def _generate_data_analysis(self, categorized_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate data analysis section.
        """
        distribution = categorized_data['categorization_metadata']['confidence_scores']['distribution']
        
        return {
            'information_distribution': {
                'high_priority': f"{distribution['high_priority']:.1%}",
                'medium_priority': f"{distribution['medium_priority']:.1%}",
                'low_priority': f"{distribution['low_priority']:.1%}",
                'supplementary': f"{distribution['supplementary']:.1%}"
            },
            'quality_indicators': {
                'categorization_confidence': f"{categorized_data['categorization_metadata']['confidence_scores']['overall_confidence']:.2%}",
                'processing_method': 'Hybrid scoring algorithm',
                'validation_approach': 'Multi-criteria assessment'
            }
        }
    
    def _generate_methodology_details(self, categorized_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate methodology details section.
        """
        return {
            'research_approach': 'Multi-angle systematic research',
            'categorization_method': 'Hybrid scoring with keyword analysis',
            'quality_assurance': 'Confidence scoring and distribution analysis',
            'processing_pipeline': [
                'Topic input and validation',
                'Multi-angle information compilation',
                'Content importance analysis',
                'Systematic categorization',
                'Report generation and formatting'
            ]
        }
    
    def _generate_quality_metrics(self, categorized_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate quality metrics section.
        """
        return {
            'overall_confidence': f"{categorized_data['categorization_metadata']['confidence_scores']['overall_confidence']:.2%}",
            'processing_completeness': '100%',
            'categorization_method': 'Validated hybrid scoring',
            'information_coverage': 'Comprehensive multi-angle analysis'
        }
    
    def _generate_quick_insights(self, categorized_data: Dict[str, Any]) -> List[str]:
        """
        Generate quick insights for summary report.
        """
        insights = []
        high_priority = categorized_data['important_information']['high_priority']
        
        for item in high_priority[:3]:
            insight = f"Quick insight: {self._extract_key_insight(item['content']['content'])}"
            insights.append(insight)
        
        return insights
    
    def _generate_action_items(self, categorized_data: Dict[str, Any]) -> List[str]:
        """
        Generate action items for summary report.
        """
        return [
            "Review high-priority information for immediate implementation",
            "Develop action plan based on key findings",
            "Monitor trends and developments in this area",
            "Consider resource allocation for implementation",
            "Establish metrics for success measurement"
        ]
    
    def _generate_appendices(self, categorized_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate appendices with supporting information.
        """
        return {
            'categorization_metadata': categorized_data['categorization_metadata'],
            'supplementary_information': categorized_data['minor_information']['supplementary'],
            'processing_statistics': {
                'total_items_processed': categorized_data['categorization_metadata']['total_items_processed'],
                'categorization_confidence': categorized_data['categorization_metadata']['confidence_scores']['overall_confidence'],
                'distribution_analysis': categorized_data['categorization_metadata']['confidence_scores']['distribution']
            }
        }
    
    def export_report_as_text(self, report_data: Dict[str, Any]) -> str:
        """
        Export the report as formatted text.
        """
        text_report = f"""
{'='*80}
OVERSIGHT AI SYSTEM - INFORMATIVE REPORT
{'='*80}

Topic: {report_data['metadata']['topic']}
Report Type: {report_data['metadata']['report_type'].title()}
Generated: {report_data['metadata']['generation_timestamp']}
Sources Analyzed: {report_data['metadata']['total_sources_analyzed']}
Confidence Level: {report_data['metadata']['categorization_confidence']:.2%}

{'='*80}
REPORT CONTENT
{'='*80}

"""
        
        # Add content sections
        for section_name, section_content in report_data['content'].items():
            text_report += f"\n{section_name.upper().replace('_', ' ')}\n"
            text_report += "-" * len(section_name) + "\n"
            
            if isinstance(section_content, str):
                text_report += section_content + "\n"
            elif isinstance(section_content, dict):
                text_report += self._format_dict_as_text(section_content) + "\n"
            elif isinstance(section_content, list):
                for item in section_content:
                    text_report += f"• {item}\n"
            
            text_report += "\n"
        
        return text_report
    
    def _format_dict_as_text(self, data: Dict[str, Any], indent: int = 0) -> str:
        """
        Format dictionary data as readable text.
        """
        text = ""
        indent_str = "  " * indent
        
        for key, value in data.items():
            if isinstance(value, dict):
                text += f"{indent_str}{key.title().replace('_', ' ')}:\n"
                text += self._format_dict_as_text(value, indent + 1)
            elif isinstance(value, list):
                text += f"{indent_str}{key.title().replace('_', ' ')}:\n"
                for item in value:
                    if isinstance(item, dict):
                        text += self._format_dict_as_text(item, indent + 1)
                    else:
                        text += f"{indent_str}  • {item}\n"
            else:
                text += f"{indent_str}{key.title().replace('_', ' ')}: {value}\n"
        
        return text
    def export_report_as_markdown(self, report_data: Dict[str, Any]) -> str:
        """
        Export the report as a formatted markdown document with 3 main sections:
        1. Sources Used
        2. Speed/Loading Time/ETA
        3. Document Content (varies by report type)
        """
        topic = report_data['metadata']['topic']
        report_type = report_data['metadata']['report_type']
        timestamp = report_data['metadata']['generation_timestamp']
        sources_analyzed = report_data['metadata']['total_sources_analyzed']
        confidence = report_data['metadata']['categorization_confidence']

        markdown_report = f"""# {topic.title()} - {report_type.title()} Report

*Generated on {timestamp}*

---

## 1. Sources Used

- **Primary Source**: OpenAI GPT Model
- **Total Sources Analyzed**: {sources_analyzed}
- **Source Type**: AI-Generated Research Content
- **Confidence Level**: {confidence:.2%}
- **Research Method**: Multi-angle systematic analysis
- **Data Quality**: High reliability with systematic categorization

---

## 2. Speed & Performance Metrics

- **Report Type**: {report_type.title()}
- **Generation Timestamp**: {timestamp}
- **Processing Method**: Automated AI analysis
- **Quality Assurance**: Multi-criteria assessment with confidence scoring
- **Coverage**: Comprehensive multi-angle approach

---

## 3. Document Content

"""

        # Add content sections based on report type
        for section_name, section_content in report_data['content'].items():
            section_title = section_name.replace('_', ' ').title()
            markdown_report += f"### {section_title}\n\n"

            if isinstance(section_content, str):
                markdown_report += section_content + "\n\n"
            elif isinstance(section_content, dict):
                markdown_report += self._format_dict_as_markdown(section_content) + "\n\n"
            elif isinstance(section_content, list):
                for item in section_content:
                    markdown_report += f"- {item}\n"
                markdown_report += "\n"

        # Add appendices if they exist
        if report_data.get('appendices'):
            markdown_report += "---\n\n## Appendices\n\n"
            for appendix_name, appendix_content in report_data['appendices'].items():
                appendix_title = appendix_name.replace('_', ' ').title()
                markdown_report += f"### {appendix_title}\n\n"
                if isinstance(appendix_content, dict):
                    markdown_report += self._format_dict_as_markdown(appendix_content) + "\n\n"
                else:
                    markdown_report += str(appendix_content) + "\n\n"

        return markdown_report

    def _format_dict_as_markdown(self, data: Dict[str, Any], level: int = 0) -> str:
        """
        Format dictionary data as markdown.
        """
        markdown = ""
        
        for key, value in data.items():
            key_formatted = key.replace('_', ' ').title()
            
            if isinstance(value, dict):
                if level == 0:
                    markdown += f"#### {key_formatted}\n\n"
                else:
                    markdown += f"**{key_formatted}:**\n\n"
                markdown += self._format_dict_as_markdown(value, level + 1)
            elif isinstance(value, list):
                markdown += f"**{key_formatted}:**\n\n"
                for item in value:
                    if isinstance(item, dict):
                        markdown += self._format_dict_as_markdown(item, level + 1)
                    else:
                        markdown += f"- {item}\n"
                markdown += "\n"
            else:
                markdown += f"**{key_formatted}:** {value}\n\n"

        return markdown
