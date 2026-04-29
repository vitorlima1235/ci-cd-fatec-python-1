"""
Script para converter OVERVIEW.md em HTML estilizado
(Pode ser salvo como PDF pelo navegador: Ctrl+P -> Salvar como PDF)
"""
import markdown
from pathlib import Path

def markdown_to_html(md_file, html_file):
    """Converte arquivo Markdown para HTML"""
    
    # Lê o arquivo Markdown
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Converte Markdown para HTML
    html_content = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'codehilite', 'nl2br']
    )
    
    # HTML completo com CSS para impressão
    html_full = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>VISÃO GERAL DA PIPELINE CI/CD - FATEC</title>
    <style>
        @media print {
            @page {
                size: A4;
                margin: 2cm;
            }
            body {
                font-size: 11pt;
            }
            h1 { page-break-before: always; }
            h1:first-of-type { page-break-before: avoid; }
            h1, h2, h3 { page-break-after: avoid; }
            pre, table { page-break-inside: avoid; }
        }
        
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
            background: white;
        }
        
        h1 {
            color: #2c3e50;
            border-bottom: 4px solid #3498db;
            padding-bottom: 12px;
            margin-top: 40px;
            font-size: 2.2em;
        }
        
        h2 {
            color: #34495e;
            margin-top: 35px;
            font-size: 1.8em;
            border-left: 5px solid #3498db;
            padding-left: 15px;
        }
        
        h3 {
            color: #7f8c8d;
            margin-top: 25px;
            font-size: 1.4em;
        }
        
        code {
            background: #f4f4f4;
            padding: 3px 8px;
            border-radius: 4px;
            font-family: 'Courier New', 'Consolas', monospace;
            font-size: 0.9em;
            color: #e74c3c;
        }
        
        pre {
            background: #2c3e50;
            color: #ecf0f1;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            line-height: 1.5;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        pre code {
            background: none;
            padding: 0;
            color: #ecf0f1;
        }
        
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 25px 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        th, td {
            border: 1px solid #ddd;
            padding: 14px;
            text-align: left;
        }
        
        th {
            background: #3498db;
            color: white;
            font-weight: 600;
        }
        
        tr:nth-child(even) {
            background: #f9f9f9;
        }
        
        tr:hover {
            background: #e8f4f8;
        }
        
        blockquote {
            border-left: 5px solid #3498db;
            margin-left: 0;
            padding-left: 25px;
            color: #7f8c8d;
            font-style: italic;
        }
        
        hr {
            border: none;
            border-top: 3px solid #ecf0f1;
            margin: 40px 0;
        }
        
        ul, ol {
            margin: 20px 0;
            padding-left: 30px;
        }
        
        li {
            margin: 8px 0;
        }
        
        a {
            color: #3498db;
            text-decoration: none;
        }
        
        a:hover {
            text-decoration: underline;
        }
        
        .print-button {
            position: fixed;
            top: 20px;
            right: 20px;
            background: #3498db;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.2);
            z-index: 1000;
        }
        
        .print-button:hover {
            background: #2980b9;
        }
        
        @media print {
            .print-button {
                display: none;
            }
        }
        
        /* Emojis mantêm tamanho consistente */
        body {
            font-feature-settings: "emoji";
        }
    </style>
</head>
<body>
    <button class="print-button" onclick="window.print()">🖨️ Salvar como PDF</button>
    """ + html_content + """
    <script>
        // Adiciona suporte para imprimir com Ctrl+P
        document.addEventListener('keydown', function(e) {
            if ((e.ctrlKey || e.metaKey) && e.key === 'p') {
                e.preventDefault();
                window.print();
            }
        });
    </script>
</body>
</html>
"""
    
    # Salva o HTML
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_full)
    
    print(f"✅ HTML gerado com sucesso: {html_file}")
    print(f"\n📖 Como gerar o PDF:")
    print(f"   1. Abra o arquivo no navegador: {html_file}")
    print(f"   2. Pressione Ctrl+P ou clique no botão 'Salvar como PDF'")
    print(f"   3. Selecione 'Salvar como PDF' ou 'Microsoft Print to PDF'")
    print(f"   4. Salve como OVERVIEW.pdf")

if __name__ == '__main__':
    md_file = Path(__file__).parent / 'OVERVIEW.md'
    html_file = Path(__file__).parent / 'OVERVIEW.html'
    
    print(f"📄 Convertendo {md_file.name} para HTML...")
    markdown_to_html(md_file, html_file)
