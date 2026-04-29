"""
Script para converter OVERVIEW.md em PDF usando WeasyPrint
"""
import markdown
from weasyprint import HTML, CSS
from pathlib import Path

def markdown_to_pdf(md_file, pdf_file):
    """Converte arquivo Markdown para PDF"""
    
    # Lê o arquivo Markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Converte Markdown para HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'codehilite', 'nl2br']
    )
    
    # CSS para estilizar o PDF
    css_content = """
    @page {
        size: A4;
        margin: 2cm;
    }
    
    body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        color: #333;
    }
    
    h1 {
        color: #2c3e50;
        border-bottom: 3px solid #3498db;
        padding-bottom: 10px;
        margin-top: 30px;
        page-break-after: avoid;
    }
    
    h2 {
        color: #34495e;
        margin-top: 25px;
        page-break-after: avoid;
    }
    
    h3 {
        color: #7f8c8d;
        page-break-after: avoid;
    }
    
    code {
        background: #f4f4f4;
        padding: 2px 6px;
        border-radius: 3px;
        font-family: 'Courier New', monospace;
        font-size: 0.9em;
    }
    
    pre {
        background: #f4f4f4;
        padding: 15px;
        border-radius: 5px;
        overflow-x: auto;
        page-break-inside: avoid;
    }
    
    pre code {
        background: none;
        padding: 0;
    }
    
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 20px 0;
        page-break-inside: avoid;
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
    
    hr {
        border: none;
        border-top: 2px solid #eee;
        margin: 30px 0;
    }
    
    ul, ol {
        margin: 15px 0;
    }
    
    li {
        margin: 5px 0;
    }
    """
    
    # HTML completo
    html_full = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>VISÃO GERAL DA PIPELINE CI/CD</title>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    
    try:
        # Gera o PDF
        HTML(string=html_full).write_pdf(
            pdf_file,
            stylesheets=[CSS(string=css_content)]
        )
        print(f"✅ PDF gerado com sucesso: {pdf_file}")
        return True
    except Exception as e:
        print(f"❌ Erro ao gerar PDF: {e}")
        return False

if __name__ == '__main__':
    md_file = Path(__file__).parent / 'OVERVIEW.md'
    pdf_file = Path(__file__).parent / 'OVERVIEW.pdf'
    
    print(f"📄 Convertendo {md_file.name} para PDF...")
    markdown_to_pdf(md_file, pdf_file)
