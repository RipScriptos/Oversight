# Oversight AI - Web App Embedding Guide

## Overview

Oversight AI has been enhanced to support easy embedding into any website as a web application. This allows you to integrate the powerful 3-step AI analysis system directly into your own websites, blogs, or applications.

## 🚀 Quick Start

### Basic Embedding

Add this iframe to your HTML to embed Oversight AI:

```html
<iframe 
    src="https://your-oversight-ai-server.com/embed" 
    width="600" 
    height="500" 
    frameborder="0"
    style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
</iframe>
```

### Minimal Version (for smaller spaces)

```html
<iframe 
    src="https://your-oversight-ai-server.com/embed/minimal" 
    width="400" 
    height="400" 
    frameborder="0"
    style="border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
</iframe>
```

## 📋 Available Embedding Options

| Version | URL | Recommended Size | Best For |
|---------|-----|------------------|----------|
| **Full Interface** | `/` | 800x600px+ | Dedicated pages, large sidebars |
| **Embeddable** | `/embed` | 600x500px+ | Blog posts, content pages |
| **Minimal** | `/embed/minimal` | 400x400px+ | Small widgets, mobile views |

## 🛠 Features Added for Embedding

### 1. CORS Support
- Configured to allow embedding from any origin
- Proper cross-origin resource sharing headers
- Support for iframe embedding from external domains

### 2. Iframe-Friendly Headers
- `X-Frame-Options: ALLOWALL` to allow iframe embedding
- Proper security headers for cross-origin embedding
- Content Security Policy configured for embedding

### 3. Responsive Design
- All embedded versions are fully responsive
- Optimized for different screen sizes
- Mobile-friendly interfaces

### 4. Multiple Interface Options
- **Standard Embed**: Full-featured interface for comprehensive use
- **Minimal Embed**: Compact version for space-constrained areas
- **Responsive**: Automatically adapts to container size

## 🎨 Customization

### Custom Styling Container

Wrap the iframe in a custom container for branded styling:

```html
<div style="
    border: 2px solid #667eea;
    border-radius: 12px;
    padding: 10px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
">
    <iframe 
        src="https://your-oversight-ai-server.com/embed" 
        width="600" 
        height="500" 
        frameborder="0"
        style="border-radius: 8px; width: 100%;">
    </iframe>
</div>
```

### Responsive Embedding

For responsive design that adapts to different screen sizes:

```html
<style>
.oversight-ai-container {
    position: relative;
    width: 100%;
    max-width: 800px;
    height: 0;
    padding-bottom: 75%; /* 4:3 Aspect Ratio */
    margin: 20px auto;
}

.oversight-ai-iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: none;
    border-radius: 8px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}
</style>

<div class="oversight-ai-container">
    <iframe 
        class="oversight-ai-iframe"
        src="https://your-oversight-ai-server.com/embed">
    </iframe>
</div>
```

## 🔧 Technical Implementation

### Server Configuration

The Flask application has been modified to support embedding:

1. **CORS Configuration**: Allows cross-origin requests from any domain
2. **Security Headers**: Proper headers for iframe embedding
3. **Multiple Routes**: Different embedding options available
4. **API Access**: Full API functionality available for embedded versions

### New Routes Added

- `/embed` - Standard embeddable interface
- `/embed/minimal` - Minimal embeddable interface
- `/embed/guide` - Comprehensive embedding documentation

### API Endpoints

All existing API endpoints work with embedded versions:

- `POST /api/analyze` - Start analysis
- `GET /api/status/{session_id}` - Get processing status
- `GET /api/results/{session_id}` - Get results
- `GET /api/download/{session_id}` - Download report
- `GET /api/report-types` - Get available report types

## 🔒 Security Considerations

### Production Deployment

When deploying to production:

1. **Use HTTPS**: Ensure both your site and Oversight AI server use HTTPS
2. **Configure CORS**: Restrict CORS to specific domains if needed
3. **CSP Headers**: Implement Content Security Policy headers
4. **Domain Validation**: Validate iframe source domains

### Recommended Security Settings

```python
# Example Flask configuration for production
CORS(app, origins=["https://yourdomain.com", "https://www.yourdomain.com"])

@app.after_request
def after_request(response):
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'  # Restrict to same origin
    response.headers['Content-Security-Policy'] = "frame-ancestors 'self' https://yourdomain.com;"
    return response
```

## 📱 Mobile Optimization

All embedded versions are optimized for mobile devices:

- Responsive design that adapts to screen size
- Touch-friendly interface elements
- Optimized for mobile browsers
- Minimal version specifically designed for small screens

## 🧪 Testing Your Integration

### Local Testing

1. Start the Oversight AI server:
   ```bash
   cd /path/to/oversight
   python app.py
   ```

2. Create a test HTML file with the iframe code
3. Open in your browser to test the embedding

### Live Example

Check out the live embedding guide at:
`https://your-oversight-ai-server.com/embed/guide`

## 📚 Examples

### Blog Post Integration

```html
<article>
    <h2>AI Analysis Tool</h2>
    <p>Use our embedded AI tool to analyze any topic:</p>
    
    <iframe 
        src="https://your-oversight-ai-server.com/embed" 
        width="100%" 
        height="500"
        style="border: none; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
    </iframe>
</article>
```

### Sidebar Widget

```html
<aside class="sidebar">
    <h3>Quick AI Analysis</h3>
    <iframe 
        src="https://your-oversight-ai-server.com/embed/minimal" 
        width="100%" 
        height="400"
        style="border: none; border-radius: 8px;">
    </iframe>
</aside>
```

## 🆘 Troubleshooting

### Common Issues

1. **Iframe not loading**
   - Check CORS settings
   - Ensure server is running
   - Verify URL is correct

2. **Styling issues**
   - Check iframe dimensions
   - Verify CSS conflicts
   - Test responsive behavior

3. **API errors**
   - Check network connectivity
   - Verify API endpoints
   - Check browser console for errors

4. **Cross-origin issues**
   - Ensure proper CORS configuration
   - Check security headers
   - Verify domain permissions

### Debug Mode

Enable debug mode for troubleshooting:

```python
app.run(debug=True, host='0.0.0.0', port=12000)
```

## 📞 Support

For additional support or custom integration requirements:

1. Check the comprehensive embedding guide: `/embed/guide`
2. Review the example implementation: `example_embedding.html`
3. Consult the main project documentation
4. Contact the development team for custom solutions

## 🔄 Updates and Maintenance

### Version Compatibility

- All embedding features are backward compatible
- API endpoints maintain consistent interfaces
- New features are added without breaking existing integrations

### Update Notifications

When updating your Oversight AI server:

1. Test embedded versions after updates
2. Check for any new embedding features
3. Update iframe URLs if server location changes
4. Verify CORS settings remain correct

---

**Ready to embed Oversight AI into your website?** Start with the basic iframe code above and customize as needed for your specific use case!