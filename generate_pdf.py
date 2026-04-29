"""
Script para converter OVERVIEW.md em PDF
"""
import markdown
import pdfkit
from pathlib import Path

def markdown_to_pdf(md_file, pdf_file):
    """Converte arquivo Markdown para PDF"""
    
    # Lê o arquivo Markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Converte Markdown para HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'codehilite']
    )
    
    # CSS para estilizar o PDF
    css = """
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
        }
        h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }
        h2 { color: #34495e; margin-top: 30px; }
        h3 { color: #7f8c8d; }
        code {
            background: #f4f4f4;
            padding: 2px 6px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
        pre {
            background: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        th {
            background: #3498db;
            color: white;
        }
        tr:nth-child(even) {
            background: #f9f9f9;
        }
        blockquote {
            border-left: 4px solid #3498db;
            margin-left: 0;
            padding-left: 20px;
            color: #7f8c8d;
        }
    </style>
    """
    
    # HTML completo
    html_full = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        {css}
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    # Configurações do PDF
    options = {
        'page-size': 'A4',
        'margin-top': '20mm',
        'margin-right': '20mm',
        'margin-bottom': '20mm',
        'margin-left': '20mm',
        'encoding': 'UTF-8',
        'enable-local-file-access': None
    }
    
    try:
        # Gera o PDF
        pdfkit.from_string(html_full, pdf_file, options=options)
        print(f"✅ PDF gerado com sucesso: {pdf_file}")
    except Exception as e:
        print(f"❌ Erro ao gerar PDF: {e}")
        print("\n💡 Certifique-se de ter o wkhtmltopdf instalado:")
        print("   Windows: choco install wkhtmltopdf")
        print("   ou baixe em: https://wkhtmltopdf.org/downloads.html")

if __name__ == '__main__':
    md_file = Path(__file__).parent / 'OVERVIEW.md'
    pdf_file = Path(__file__).parent / 'OVERVIEW.pdf'
    
    markdown_to_pdf(md_file, pdf_file)
