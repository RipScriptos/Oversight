# Oversight AI - 3-Step Artificial Intelligence System

**Discerning Eye | Artificial Intelligence tailored for creating comprehensive reports on topics with categorized important and key information.**

## Overview

Oversight AI is a sophisticated 3-step artificial intelligence system designed to analyze topics comprehensively and generate detailed informative reports. The system employs a systematic approach to information processing, categorization, and report generation.

## 3-Step Process

### Step 1: Topic Input
- **Purpose**: Validate and prepare user-provided topics for analysis
- **Process**: Input validation, topic normalization, and preparation for processing
- **Output**: Validated and formatted topic ready for research

### Step 2: Information Processing
#### Step 2a: Compile Information
- **Purpose**: Conduct in-depth research on the provided topic
- **Process**: Multi-angle research approach covering:
  - Definitions and overviews
  - Key concepts and principles
  - Applications and use cases
  - Benefits and advantages
  - Challenges and limitations
  - Current trends and developments
  - Future outlook and predictions
- **Output**: Comprehensive research data from multiple perspectives

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

### Step 3: Output Generation
- **Purpose**: Generate comprehensive informative reports
- **Process**: Structured report creation with multiple format options
- **Output**: Professional reports with:
  - Executive summaries
  - Detailed analysis
  - Technical specifications
  - Quick summaries
  - Categorized insights
  - Actionable recommendations

## Features

### Report Types
1. **Executive Summary**: High-level strategic insights and recommendations
2. **Detailed Report**: Comprehensive analysis with all categorized information
3. **Technical Report**: In-depth technical analysis with methodology details
4. **Quick Summary**: Concise overview with key highlights

### Key Capabilities
- **Multi-angle Research**: Systematic exploration of topics from various perspectives
- **Intelligent Categorization**: AI-powered importance assessment and categorization
- **Flexible Reporting**: Multiple report formats for different audiences
- **Quality Metrics**: Confidence scoring and reliability assessment
- **Session Management**: Track and manage multiple analysis sessions
- **Export Functionality**: Download reports in text format

## Installation

### Prerequisites

**All Platforms:**
- Python 3.8 or higher
- pip package manager

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

#### 1. Clone the repository:
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

#### 4. Configure environment variables (Optional):

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

### Dependencies
The project requires the following Python packages:
- **Flask** (2.3.3) - Web framework for the API and web interface
- **Flask-CORS** (4.0.0) - Cross-Origin Resource Sharing support for embedding
- **python-dotenv** (1.0.0) - Environment variable management
- **requests** (2.31.0) - HTTP library for web scraping and API calls
- **beautifulsoup4** (4.12.2) - HTML/XML parsing for web content extraction
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

### Pip Install
```bash
pip3 install flask
```
```bash
pip3 install flask_cors
```
```bash
pip3 install dotenv
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
    print(result['text_report'])
else:
    print(f"Error: {result['error']}")
```

### API Endpoints
- `POST /api/analyze` - Analyze a topic
- `GET /api/status/<session_id>` - Get processing status
- `GET /api/results/<session_id>` - Get session results
- `GET /api/download/<session_id>` - Download report
- `GET /api/history` - Get processing history
- `GET /api/statistics` - Get system statistics

## System Architecture

### Core Components

#### 1. Research Engine (`src/research_engine.py`)
- Conducts multi-angle research on topics
- Generates comprehensive information from various perspectives
- Provides research summaries and metadata

#### 2. Information Architect (`src/information_architect.py`)
- Analyzes content importance using hybrid scoring
- Categorizes information into priority levels
- Provides confidence metrics and reasoning

#### 3. Report Generator (`src/report_generator.py`)
- Creates professional reports in multiple formats
- Structures information hierarchically
- Generates actionable insights and recommendations

#### 4. Oversight AI Controller (`src/oversight_ai.py`)
- Orchestrates the 3-step process
- Manages sessions and processing history
- Provides system statistics and monitoring

### Web Application (`app.py`)
- Flask-based web interface
- RESTful API for programmatic access
- Real-time processing status updates
- Report download functionality

## Testing

Run comprehensive system tests:
```bash
python test_system.py
```

This will test:
- Individual component functionality
- End-to-end processing pipeline
- Multiple topic and report type combinations
- System statistics and performance metrics

## Configuration

### Environment Variables
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

The system tracks various performance metrics:
- Processing time per session
- Success/failure rates
- Topic diversity analysis
- Categorization confidence scores
- System usage statistics

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
- Enhanced web scraping capabilities
- Integration with external APIs
- Advanced natural language processing
- Machine learning-based categorization
- Multi-language support
- Collaborative analysis features

### Performance Improvements
- Caching mechanisms
- Parallel processing
- Database integration
- Advanced analytics
- Real-time collaboration

---

**Oversight AI** - Transforming information into actionable intelligence through systematic analysis and intelligent categorization.
