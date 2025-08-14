const multiparty = require('multiparty');

exports.handler = async (event, context) => {
    // Set CORS headers
    const headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST, GET, OPTIONS',
    };

    if (event.httpMethod === 'OPTIONS') {
        return {
            statusCode: 200,
            headers,
            body: '',
        };
    }

    if (event.httpMethod !== 'POST') {
        return {
            statusCode: 405,
            headers,
            body: JSON.stringify({ error: 'Method not allowed' }),
        };
    }

    try {
        // Parse form data
        const form = new multiparty.Form();
        const formData = await new Promise((resolve, reject) => {
            form.parse(event.body, (err, fields, files) => {
                if (err) reject(err);
                else resolve({ fields, files });
            });
        });

        const query = formData.fields.query ? formData.fields.query[0] : '';
        const file = formData.files.file ? formData.files.file[0] : null;

        if (!file) {
            return {
                statusCode: 400,
                headers,
                body: JSON.stringify({ error: 'No file uploaded' }),
            };
        }

        if (!query) {
            return {
                statusCode: 400,
                headers,
                body: JSON.stringify({ error: 'No query provided' }),
            };
        }

        // Read file content
        const fs = require('fs');
        const fileContent = fs.readFileSync(file.path, 'utf8');

        // Here you would typically call OpenAI API
        // For now, return a mock response
        const mockResponse = {
            analysis: `Based on your query "${query}", I've analyzed the uploaded file "${file.originalFilename}". The data shows interesting patterns that could be valuable for your analysis.`,
            summary: 'The spreadsheet contains structured data suitable for various analytical operations.',
            chartData: null // Would contain actual chart data in production
        };

        return {
            statusCode: 200,
            headers,
            body: JSON.stringify(mockResponse),
        };

    } catch (error) {
        console.error('Function error:', error);
        return {
            statusCode: 500,
            headers,
            body: JSON.stringify({ error: 'Internal server error' }),
        };
    }
};