# Spreadify - Agentic AI Spreadsheet Assistant

A powerful AI-driven web application that helps you analyze and understand your spreadsheet data through natural language queries.

## 🌟 Features

- **File Upload**: Support for CSV and Excel files (.csv, .xlsx, .xls)
- **Natural Language Queries**: Ask questions about your data in plain English
- **AI Analysis**: Powered by OpenAI for intelligent data insights
- **Interactive Charts**: Visualize your data with dynamic charts
- **Responsive Design**: Modern, mobile-friendly interface
- **Serverless Architecture**: Built for Netlify with edge functions

## 🚀 Live Demo

Visit the live application: [https://spreadify-agentic-ai.netlify.app](https://spreadify-agentic-ai.netlify.app)

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3 (Tailwind CSS), Vanilla JavaScript
- **Backend**: Netlify Functions (Node.js serverless)
- **AI Integration**: OpenAI API
- **Charts**: Chart.js
- **Hosting**: Netlify

## 📁 Project Structure

```
├── public/
│   ├── index.html          # Main HTML file
│   └── js/
│       └── app.js          # Frontend JavaScript
├── netlify/
│   └── functions/
│       └── openai.js       # Serverless API function
├── netlify.toml            # Netlify configuration
├── package.json            # Dependencies and scripts
├── README.md               # Project documentation
└── .gitignore             # Git ignore rules
```

## 🔧 Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Imole-cloud/Spreadify_Agentic_AI.git
   cd Spreadify_Agentic_AI
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run locally with Netlify CLI**
   ```bash
   npm run dev
   ```

## 🚀 Deployment

### Automatic Deployment (Recommended)

1. Fork this repository
2. Connect your GitHub repository to Netlify
3. Set the following build settings:
   - **Build command**: `npm run build`
   - **Publish directory**: `public`
4. Add environment variables in Netlify dashboard:
   - `OPENAI_API_KEY`: Your OpenAI API key

### Manual Deployment

```bash
npm run deploy
```

## 📋 Usage

1. **Upload Your File**: Click the upload area or drag and drop your CSV/Excel file
2. **Ask a Question**: Type your question about the data in natural language
3. **Get Insights**: The AI will analyze your data and provide insights
4. **View Results**: See text analysis and interactive charts

### Example Queries

- "What are the top 5 highest values in this dataset?"
- "Show me a summary of sales by region"
- "What patterns do you see in the data?"
- "Create a chart showing monthly trends"

## 🔐 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for providing the AI capabilities
- Netlify for hosting and serverless functions
- Chart.js for data visualization
- Tailwind CSS for styling

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the [Issues](https://github.com/Imole-cloud/Spreadify_Agentic_AI/issues) page
2. Create a new issue if your problem isn't already documented
3. Provide detailed information about your environment and the issue

---

**Built with ❤️ by [Imole-cloud](https://github.com/Imole-cloud)**