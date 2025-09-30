# Oversight AI - OpenAI Integration & Markdown Export

## Overview

The Oversight AI system has been successfully updated to integrate with OpenAI's API and generate reports in markdown format with a structured 3-section layout.

## Key Changes Made

### 1. OpenAI API Integration

- **Added OpenAI SDK**: Updated `requirements.txt` to include `openai>=1.0.0`
- **Enhanced Configuration**: Extended `config.py` with OpenAI-specific settings
- **Research Engine Overhaul**: Completely rewrote `src/research_engine.py` to use OpenAI API instead of web scraping
- **API Key Validation**: Added proper validation and error handling for OpenAI configuration

### 2. Structured 3-Section Report Format

All reports now follow a consistent 3-section structure:

#### Section 1: Sources Used
- Primary source information (OpenAI GPT Model)
- Total sources analyzed
- Source type and confidence level
- Research methodology details
- Data quality indicators

#### Section 2: Speed & Performance Metrics
- Processing speed and timing information
- Loading time/ETA details
- Content generation rate (words per second)
- Quality assurance metrics
- Coverage completeness

#### Section 3: Document Content
- Varies by document type (executive, detailed, technical, summary)
- Structured content based on research findings
- Categorized information by priority
- Comprehensive analysis and conclusions

### 3. Markdown File Export

- **New Export Method**: Added `export_report_as_markdown()` to `ReportGenerator`
- **Updated Download API**: Modified `/api/download/<session_id>/<format_type>` to support both markdown and text
- **Demo Script Enhancement**: Updated `run_demo.py` to save reports as `.md` files by default
- **Proper Markdown Formatting**: Structured headers, lists, and emphasis for readability

## Configuration Setup

### 1. Environment Variables

Copy the example environment file and configure your settings:

```bash
cp .env.example .env
```

Edit `.env` with your OpenAI API key:

```env
# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_MAX_TOKENS=2000
OPENAI_TEMPERATURE=0.7

# Flask Configuration
SECRET_KEY=your_secret_key_here
DEBUG=True
PORT=12001
```

### 2. Required Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `OPENAI_MODEL`: Model to use (default: gpt-3.5-turbo)
- `OPENAI_MAX_TOKENS`: Maximum tokens per request (default: 2000)
- `OPENAI_TEMPERATURE`: Response creativity (default: 0.7)

## Usage

### Web Interface

Start the Flask web application:

```bash
python app.py
```

Access the interface at: `http://localhost:12001`

### Command Line Demo

Run the interactive demo:

```bash
python run_demo.py
```

### API Endpoints

#### Analyze Topic
```
POST /api/analyze
Content-Type: application/json

{
    "topic": "Artificial Intelligence",
    "report_type": "detailed"
}
```

#### Download Report
```
GET /api/download/<session_id>          # Downloads as markdown (.md)
GET /api/download/<session_id>/markdown # Downloads as markdown (.md)
GET /api/download/<session_id>/text     # Downloads as text (.txt)
```

## Report Types

The system supports four report types:

1. **Executive**: High-level strategic insights and recommendations
2. **Detailed**: Comprehensive analysis with all categorized information
3. **Technical**: In-depth technical analysis with methodology details
4. **Summary**: Concise overview with key highlights

## File Structure

```
Oversight/
├── src/
│   ├── oversight_ai.py          # Main controller (updated)
│   ├── research_engine.py       # OpenAI integration (rewritten)
│   ├── report_generator.py      # Markdown export (enhanced)
│   └── information_architect.py # Categorization logic
├── config.py                    # Configuration (enhanced)
├── app.py                       # Flask web app (updated)
├── run_demo.py                  # Demo script (updated)
├── requirements.txt             # Dependencies (updated)
├── .env.example                 # Environment template (new)
└── test_simple.py               # Component tests (new)
```

## Testing

Run the component tests to verify functionality:

```bash
python test_simple.py
```

This will test:
- Configuration structure
- Markdown export functionality
- Report formatting

## Sample Output

### Markdown Report Structure

```markdown
# Topic Name - Report Type Report

*Generated on timestamp*

---

## 1. Sources Used

- **Primary Source**: OpenAI GPT Model
- **Total Sources Analyzed**: 8
- **Source Type**: AI-Generated Research Content
- **Confidence Level**: 87.00%
- **Research Method**: Multi-angle systematic analysis

---

## 2. Speed & Performance Metrics

- **Processing Speed**: 15.23 seconds
- **Loading Time/ETA**: 15.23 seconds
- **Content Generation Rate**: 156.2 words/second
- **Quality Assurance**: Multi-criteria assessment

---

## 3. Document Content

### Introduction
[Comprehensive analysis content...]

### Critical Information
[High-priority findings...]

### Important Information
[Medium-priority findings...]

## Appendices
[Additional technical details...]
```

## Error Handling

The system includes comprehensive error handling:

- **API Key Validation**: Checks for valid OpenAI API key on startup
- **Rate Limiting**: Handles OpenAI API rate limits gracefully
- **Fallback Content**: Provides fallback content if API calls fail
- **Configuration Validation**: Validates all required configuration parameters

## Performance Metrics

The system now tracks and reports:

- **Processing Speed**: Total time for complete analysis
- **Loading Time**: Time for each research angle
- **Content Generation Rate**: Words generated per second
- **API Response Times**: Individual OpenAI API call durations
- **Quality Scores**: Confidence levels and reliability metrics

## Troubleshooting

### Common Issues

1. **Missing OpenAI API Key**
   ```
   Error: OPENAI_API_KEY environment variable is required
   ```
   Solution: Add your API key to the `.env` file

2. **API Rate Limits**
   ```
   Error: Rate limit exceeded
   ```
   Solution: Wait and retry, or upgrade your OpenAI plan

3. **Invalid Model**
   ```
   Error: Model not found
   ```
   Solution: Check your model name in the configuration

### Debug Mode

Enable debug mode for detailed logging:

```env
DEBUG=True
```

## Migration Notes

If upgrading from the previous version:

1. **Backup existing reports**: The new system generates different output formats
2. **Update configuration**: Add OpenAI-specific environment variables
3. **Install dependencies**: Run `pip install -r requirements.txt`
4. **Test integration**: Run `python test_simple.py` to verify setup

## Security Considerations

- **API Key Protection**: Never commit API keys to version control
- **Environment Variables**: Use `.env` files for sensitive configuration
- **Rate Limiting**: Implement appropriate rate limiting for production use
- **Input Validation**: All user inputs are validated and sanitized

## Future Enhancements

Potential improvements for future versions:

- Support for additional AI models (Claude, Gemini, etc.)
- Batch processing for multiple topics
- Advanced caching mechanisms
- Real-time progress tracking
- Custom report templates
- Integration with external data sources

## Support

For issues or questions:

1. Check the troubleshooting section above
2. Review the test output from `python test_simple.py`
3. Verify your OpenAI API key and configuration
4. Check the Flask application logs for detailed error messages