class SpreadifyApp {
    constructor() {
        this.currentFile = null;
        this.currentData = null;
        this.initializeEventListeners();
    }

    initializeEventListeners() {
        const fileInput = document.getElementById('fileInput');
        const analyzeBtn = document.getElementById('analyzeBtn');
        const queryInput = document.getElementById('queryInput');

        fileInput.addEventListener('change', this.handleFileUpload.bind(this));
        analyzeBtn.addEventListener('click', this.handleAnalyze.bind(this));
        queryInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.handleAnalyze();
            }
        });

        // Drag and drop functionality
        const uploadArea = fileInput.parentElement;
        uploadArea.addEventListener('dragover', this.handleDragOver.bind(this));
        uploadArea.addEventListener('drop', this.handleDrop.bind(this));
    }

    handleDragOver(e) {
        e.preventDefault();
        e.stopPropagation();
        e.target.classList.add('border-blue-500', 'bg-blue-50');
    }

    handleDrop(e) {
        e.preventDefault();
        e.stopPropagation();
        e.target.classList.remove('border-blue-500', 'bg-blue-50');

        const files = e.dataTransfer.files;
        if (files.length > 0) {
            this.processFile(files[0]);
        }
    }

    handleFileUpload(e) {
        const file = e.target.files[0];
        if (file) {
            this.processFile(file);
        }
    }

    processFile(file) {
        this.currentFile = file;
        const fileName = document.getElementById('fileName');
        const fileInfo = document.getElementById('fileInfo');

        fileName.textContent = file.name;
        fileInfo.classList.remove('hidden');

        // Read file content
        const reader = new FileReader();
        reader.onload = (e) => {
            this.currentData = e.target.result;
            console.log('File loaded successfully');
        };
        reader.readAsText(file);
    }

    async handleAnalyze() {
        const query = document.getElementById('queryInput').value.trim();

        if (!this.currentFile) {
            this.showError('Please upload a file first');
            return;
        }

        if (!query) {
            this.showError('Please enter a question');
            return;
        }

        this.showLoading();

        try {
            const formData = new FormData();
            formData.append('file', this.currentFile);
            formData.append('query', query);

            const response = await fetch('/.netlify/functions/openai', {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const result = await response.json();
            this.displayResults(result);

        } catch (error) {
            console.error('Analysis error:', error);
            this.showError('Failed to analyze the data. Please try again.');
        }
    }

    showLoading() {
        const resultsSection = document.getElementById('resultsSection');
        const loading = document.getElementById('loading');
        const results = document.getElementById('results');
        const error = document.getElementById('error');

        resultsSection.classList.remove('hidden');
        loading.classList.remove('hidden');
        results.classList.add('hidden');
        error.classList.add('hidden');
    }

    displayResults(result) {
        const loading = document.getElementById('loading');
        const results = document.getElementById('results');
        const textResults = document.getElementById('textResults');
        const chartContainer = document.getElementById('chartContainer');

        loading.classList.add('hidden');
        results.classList.remove('hidden');

        // Display text results
        textResults.innerHTML = `
            <div class="prose max-w-none">
                <h3 class="text-lg font-semibold mb-2">Analysis Results:</h3>
                <p class="text-gray-700 mb-4">${result.analysis || 'Analysis completed successfully.'}</p>
                ${result.summary ? `<div class="bg-blue-50 p-4 rounded-lg"><strong>Summary:</strong> ${result.summary}</div>` : ''}
            </div>
        `;

        // Display chart if data is provided
        if (result.chartData) {
            this.renderChart(result.chartData);
        }
    }

    renderChart(chartData) {
        const chartContainer = document.getElementById('chartContainer');
        const canvas = document.getElementById('resultChart');

        chartContainer.classList.remove('hidden');

        // Clear previous chart
        if (this.currentChart) {
            this.currentChart.destroy();
        }

        const ctx = canvas.getContext('2d');
        this.currentChart = new Chart(ctx, {
            type: chartData.type || 'bar',
            data: chartData.data,
            options: {
                responsive: true,
                plugins: {
                    title: {
                        display: true,
                        text: chartData.title || 'Data Visualization'
                    }
                }
            }
        });
    }

    showError(message) {
        const resultsSection = document.getElementById('resultsSection');
        const loading = document.getElementById('loading');
        const results = document.getElementById('results');
        const error = document.getElementById('error');

        resultsSection.classList.remove('hidden');
        loading.classList.add('hidden');
        results.classList.add('hidden');
        error.classList.remove('hidden');
        error.textContent = message;
    }
}

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new SpreadifyApp();
});