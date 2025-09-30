# Oversight AI - 3-Step Artificial Intelligence System

**Discerning Eye | OpenAI-powered artificial intelligence system for creating comprehensive reports with structured 3-section format and markdown export.**

## Overview

Oversight AI is a sophisticated 3-step artificial intelligence system powered by OpenAI's GPT models, designed to analyze topics comprehensively and generate detailed informative reports. The system employs OpenAI API integration with a systematic approach to information processing, categorization, and professional report generation in markdown format.

## 3-Step Process

### Step 1: Topic Input
- **Purpose**: Validate and prepare user-provided topics for analysis
- **Process**: Input validation, topic normalization, and preparation for processing
- **Output**: Validated and formatted topic ready for research

### Step 2: Information Processing
#### Step 2a: Compile Information (OpenAI-Powered)
- **Purpose**: Conduct in-depth AI-powered research on the provided topic
- **Process**: Multi-angle research approach using OpenAI GPT models covering:
  - Definitions and comprehensive overviews
  - Key concepts and fundamental principles
  - Real-world applications and use cases
  - Benefits, advantages, and opportunities
  - Challenges, limitations, and risks
  - Current trends and market developments
  - Future outlook and predictions
  - Technical specifications and implementation details
- **Output**: AI-generated comprehensive research data with timing metrics

#### Step 2b: Categorize Text
- **Purpose**: Systematically categorize information by importance
- **Process**: Information architect analyzes content using:
  - Keyword-based importance scoring
  - Content angle assessment
  - Length and comprehensiveness evaluation
  - Hybrid scoring algorithm
- **Output**: Categorized information with importance levels:
  - High Priority (Critical Information)
  - Medium Priority (Important Information)
  - Low Priority (Supporting Information)
  - Supplementary (Background Information)

### Step 3: Output Generation (Structured 3-Section Format)
- **Purpose**: Generate comprehensive informative reports in structured markdown format
- **Process**: Professional report creation with 3-section structure and multiple format options
- **Output**: Professional reports with structured sections:
  
  **Section 1: Sources Used**
  - OpenAI GPT model information and confidence levels
  - Research methodology and data quality indicators
  - Processing metrics and reliability scores
  
  **Section 2: Speed & Performance Metrics**
  - Processing speed and loading time/ETA
  - Content generation rate (words per second)
  - Quality assurance and coverage completeness
  
  **Section 3: Document Content** (varies by type)
  - Executive summaries with strategic insights
  - Detailed analysis with comprehensive categorization
  - Technical specifications with implementation details
  - Quick summaries with key highlights
  - Categorized insights by priority levels
  - Actionable recommendations and conclusions

## Features

### Report Types
1. **Executive Summary**: High-level strategic insights and recommendations
2. **Detailed Report**: Comprehensive analysis with all categorized information
3. **Technical Report**: In-depth technical analysis with methodology details
4. **Quick Summary**: Concise overview with key highlights

### Key Capabilities
- **OpenAI Integration**: Powered by GPT-3.5-turbo, GPT-4, and other OpenAI models
- **Multi-angle Research**: AI-driven systematic exploration from various perspectives
- **Intelligent Categorization**: Advanced importance assessment and priority categorization
- **Structured 3-Section Format**: Consistent Sources, Performance, and Content sections
- **Markdown Export**: Professional markdown (.md) file generation and download
- **Flexible Reporting**: Multiple report formats for different audiences and use cases
- **Performance Metrics**: Real-time processing speed, timing, and quality indicators
- **Quality Assurance**: Confidence scoring, reliability assessment, and validation
- **Session Management**: Track and manage multiple analysis sessions with history
- **Dual Export Options**: Download reports in both markdown (.md) and text (.txt) formats

## Installation

### Prerequisites

**All Platforms:**
- Python 3.8 or higher
- pip package manager
- OpenAI API key (required for AI functionality)

**macOS:**
- Xcode Command Line Tools (for some dependencies): `xcode-select --install`
- Homebrew (recommended): [Install Homebrew](https://brew.sh/)

**Windows:**
- Microsoft Visual C++ 14.0 or greater (usually included with Visual Studio)
- Windows 10/11 or Windows Server 2016+

**Linux (Ubuntu/Debian):**
- `python3-dev` and `python3-venv` packages:
  ```bash
  sudo apt-get update
  sudo apt-get install python3-dev python3-venv python3-pip
  ```

**Linux (CentOS/RHEL/Fedora):**
- Development tools:
  ```bash
  sudo yum groupinstall "Development Tools"  # CentOS/RHEL
  sudo dnf groupinstall "Development Tools"  # Fedora
  ```

### Setup

#### 1. Clone the repository: (Also remove Oversight that is already on PC if needing update.)
```bash
rm -rf Oversight
```

```bash
git clone https://github.com/RipScriptos/Oversight.git
cd Oversight
```

#### 2. Create and activate a virtual environment (Recommended):

**macOS/Linux:**
```bash
python3 -m venv oversight_env
source oversight_env/bin/activate
```

**Windows (Command Prompt):**
```cmd
python -m venv oversight_env
oversight_env\Scripts\activate
```

**Windows (PowerShell):**
```powershell
python -m venv oversight_env
oversight_env\Scripts\Activate.ps1
```

#### 3. Install dependencies:

**All platforms:**
```bash
pip install -r requirements.txt
```

**Alternative for macOS (if you encounter issues):**
```bash
pip3 install -r requirements.txt
```

#### 4. Configure environment variables (Required for OpenAI):

**macOS/Linux:**
```bash
cp .env.example .env
nano .env  # or use your preferred editor
```

**Windows:**
```cmd
copy .env.example .env
notepad .env
```

**Required Configuration:**
Add your OpenAI API key to the `.env` file:
```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
OPENAI_MAX_TOKENS=2000
OPENAI_TEMPERATURE=0.7
```

### Dependencies
The project requires the following Python packages:
- **Flask** (2.3.3) - Web framework for the API and web interface
- **Flask-CORS** (4.0.0) - Cross-Origin Resource Sharing support for embedding
- **python-dotenv** (1.0.0) - Environment variable management
- **openai** (>=1.0.0) - OpenAI API client for GPT model integration
- **requests** (2.31.0) - HTTP library for API calls and web requests
- **beautifulsoup4** (4.12.2) - HTML/XML parsing for web content extraction (legacy support)
- **lxml** (4.9.3) - XML and HTML parser (optional, for better performance)
- **urllib3** (2.0.4) - HTTP client library (optional, for enhanced session handling)

## Usage

### Command Line Demo
Run the interactive demo to test the system:

**macOS/Linux:**
```bash
python3 run_demo.py
```

**Windows:**
```cmd
python run_demo.py
```

### Web Interface
Start the web application:

**macOS/Linux:**
```bash
python3 app.py
```

**Windows:**
```cmd
python app.py
```

### Pip Install (macOS Terminal Commands)
For macOS users, you can install dependencies individually using these Terminal commands:

```bash
pip3 install flask
```
```bash
pip3 install flask_cors
```
```bash
pip3 install python-dotenv
```
```bash
pip3 install beautifulsoup4
```
```bash
pip3 install openai
```
```bash
pip3 install requests
```

**Note:** It's recommended to use `pip install -r requirements.txt` instead for automatic dependency management.

Access the web interface at: `http://localhost:12001`

### Programmatic Usage
```python
from src.oversight_ai import OversightAI

# Initialize the system
oversight_ai = OversightAI()

# Process a topic
result = oversight_ai.process_topic("Artificial Intelligence", "detailed")

if result['success']:
    print(f"Report generated: {result['session_id']}")
    print(f"Processing time: {result['processing_time']:.2f} seconds")
    
    # Access markdown report
    print("Markdown Report:")
    print(result['markdown_report'])
    
    # Or access text report
    print("Text Report:")
    print(result['text_report'])
else:
    print(f"Error: {result['error']}")
```

### API Endpoints
- `POST /api/analyze` - Analyze a topic with OpenAI integration
- `GET /api/status/<session_id>` - Get processing status and progress
- `GET /api/results/<session_id>` - Get session results with performance metrics
- `GET /api/download/<session_id>` - Download report as markdown (.md) by default
- `GET /api/download/<session_id>/markdown` - Download report as markdown (.md)
- `GET /api/download/<session_id>/text` - Download report as text (.txt)
- `GET /api/history` - Get processing history with timing data
- `GET /api/statistics` - Get system statistics and performance metrics

## System Architecture

### Core Components

#### 1. Research Engine (`src/research_engine.py`) - OpenAI Powered
- Conducts AI-powered multi-angle research using OpenAI GPT models
- Generates comprehensive information from 8+ different research perspectives
- Provides research summaries with performance metrics and timing data
- Includes fallback mechanisms and error handling for API reliability

#### 2. Information Architect (`src/information_architect.py`)
- Analyzes content importance using hybrid scoring
- Categorizes information into priority levels
- Provides confidence metrics and reasoning

#### 3. Report Generator (`src/report_generator.py`) - Enhanced with Markdown
- Creates professional reports in structured 3-section format
- Generates both markdown (.md) and text (.txt) export formats
- Structures information hierarchically with proper markdown formatting
- Includes performance metrics, timing data, and quality indicators
- Generates actionable insights and recommendations with source attribution

#### 4. Oversight AI Controller (`src/oversight_ai.py`) - Enhanced Integration
- Orchestrates the 3-step process with OpenAI integration
- Manages sessions with comprehensive processing history and timing data
- Provides system statistics, performance monitoring, and quality metrics
- Handles both markdown and text report generation and export

### Web Application (`app.py`) - Enhanced with Dual Format Support
- Flask-based web interface with OpenAI integration
- RESTful API for programmatic access with enhanced endpoints
- Real-time processing status updates with performance metrics
- Dual format report download functionality (markdown and text)
- Enhanced error handling and API key validation

## Testing

### Component Tests (No API Key Required)
Run component tests to verify core functionality:
```bash
python test_simple.py
```

This will test:
- Configuration structure and validation
- Markdown export functionality
- Report formatting and structure
- Core system components

### Integration Tests (Mocked OpenAI)
Run integration tests with mocked OpenAI calls:
```bash
python test_integration.py
```

This will test:
- OpenAI integration with mocked responses
- Complete 3-step processing pipeline
- Markdown and text report generation
- Performance metrics and timing data
- Error handling and fallback mechanisms

## Configuration

### Environment Variables

#### Required (OpenAI Integration)
- `OPENAI_API_KEY`: Your OpenAI API key (required for AI functionality)
- `OPENAI_MODEL`: OpenAI model to use (default: gpt-3.5-turbo)
- `OPENAI_MAX_TOKENS`: Maximum tokens per API request (default: 2000)
- `OPENAI_TEMPERATURE`: Response creativity level (default: 0.7)

#### Optional (Flask Configuration)
- `SECRET_KEY`: Flask application secret key
- `DEBUG`: Enable/disable debug mode (default: True)
- `PORT`: Server port (default: 12001)
- `HOST`: Server host (default: 0.0.0.0)

### Report Types Configuration
The system supports four report types, each optimized for different use cases:
- **Executive**: Strategic decision-makers
- **Detailed**: Comprehensive analysis needs
- **Technical**: Technical teams and developers
- **Summary**: Quick overview requirements

## Performance Metrics

The system tracks comprehensive performance metrics:
- **Processing Speed**: Total time for complete analysis with OpenAI API calls
- **Loading Time/ETA**: Individual research angle processing times
- **Content Generation Rate**: Words generated per second by AI models
- **API Response Times**: OpenAI API call durations and success rates
- **Quality Scores**: Confidence levels and reliability indicators
- **Success/Failure Rates**: System reliability and error tracking
- **Topic Diversity Analysis**: Coverage and categorization effectiveness
- **System Usage Statistics**: Session history and performance trends

## Quality Assurance

### Confidence Scoring
- Overall categorization confidence
- Distribution balance assessment
- Content quality indicators
- Processing reliability metrics

### Validation
- Input topic validation
- Report type verification
- Content categorization accuracy
- Output format consistency

## Use Cases

### Business Intelligence
- Market research analysis
- Competitive intelligence
- Strategic planning support
- Industry trend analysis

### Academic Research
- Literature review assistance
- Topic exploration
- Research methodology guidance
- Knowledge synthesis

### Technical Documentation
- Technology assessment
- Implementation planning
- Risk analysis
- Best practices compilation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the Unlicense License - see the [LICENSE](LICENSE) file for details.

## Support

For questions, issues, or feature requests, please:
1. Check the existing documentation
2. Search for existing issues
3. Create a new issue with detailed information
4. Provide system information and error logs

## Troubleshooting

### OpenAI Integration Issues

#### Missing API Key
```
Error: OPENAI_API_KEY environment variable is required
```
**Solution**: Add your OpenAI API key to the `.env` file:
```env
OPENAI_API_KEY=your_actual_api_key_here
```

#### API Rate Limits
```
Error: Rate limit exceeded for requests
```
**Solution**: Wait and retry, or upgrade your OpenAI plan for higher rate limits.

#### Invalid Model
```
Error: The model 'gpt-4' does not exist
```
**Solution**: Check your OpenAI plan and use an available model like `gpt-3.5-turbo`.

### Common Issues

#### Python Command Not Found
**macOS/Linux:**
- Try using `python3` instead of `python`
- Install Python 3.8+ from [python.org](https://python.org) or use Homebrew: `brew install python3`

**Windows:**
- Install Python from [python.org](https://python.org) and make sure to check "Add Python to PATH"
- Try using `py` instead of `python`

#### Virtual Environment Issues
**macOS/Linux:**
```bash
# If python3-venv is not installed (Ubuntu/Debian)
sudo apt-get install python3-venv

# Alternative virtual environment creation
python3 -m virtualenv oversight_env
```

**Windows PowerShell Execution Policy:**
```powershell
# If you get execution policy errors
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Permission Errors
**macOS/Linux:**
```bash
# If you get permission errors with pip
pip install --user -r requirements.txt
```

**Windows:**
```cmd
# Run Command Prompt as Administrator if needed
```

#### Port Already in Use
If port 12001 is already in use, you can change it in your `.env` file:
```
PORT=8080
```

### Getting Help
- Check the [Issues](https://github.com/RipScriptos/Oversight/issues) page for known problems
- Create a new issue if you encounter a bug or need help

## Roadmap

### Planned Features
- **Multi-Model Support**: Integration with Claude, Gemini, and other AI models
- **Advanced Caching**: Intelligent caching for improved performance and cost efficiency
- **Batch Processing**: Multiple topic analysis in single requests
- **Custom Templates**: User-defined report templates and formatting options
- **Real-time Collaboration**: Multi-user analysis and report sharing
- **Enhanced Analytics**: Advanced performance metrics and usage insights
- **API Integrations**: External data source connections and enrichment

### Performance Improvements
- **Intelligent Caching**: Redis-based caching for API responses and processed data
- **Parallel Processing**: Concurrent API calls and multi-threaded analysis
- **Database Integration**: PostgreSQL/MongoDB for persistent storage and analytics
- **Advanced Analytics**: Machine learning-based performance optimization
- **Stream Processing**: Real-time analysis and progressive report generation

---

**Oversight AI** - Transforming information into actionable intelligence through OpenAI-powered systematic analysis, intelligent categorization, and professional markdown reporting.
