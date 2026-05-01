"""Convert scanned PDFs to markdown using OCR."""
import sys
import os
from pathlib import Path


def try_import(name):
    try:
        __import__(name)
        return name
    except ImportError:
        return None


def extract_with_pdf_oxide(pdf_path):
    """Extract text using pdf_oxide with PaddleOCR."""
    from pdf_oxide import PdfDocument
    
    text_parts = []
    with PdfDocument(pdf_path) as doc:
        page_count = doc.page_count()
        for page_num in range(page_count):
            page_text = doc.extract_text(page_num)
            
            if not page_text or not page_text.strip():
                page_text = doc.extract_text_ocr(page_num)
            
            if page_text:
                text_parts.append(page_text)
    
    return '\n\n---\n\n'.join(text_parts)


def extract_with_pdfplumber(pdf_path):
    """Extract text using pdfplumber."""
    import pdfplumber
    text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text.append(page_text)
    return '\n\n'.join(text)


def extract_with_pymupdf(pdf_path):
    """Extract text using pymupdf (basic, for comparison)."""
    import pymupdf
    doc = pymupdf.open(pdf_path)
    text = []
    for page in doc:
        page_text = page.get_text()
        if page_text.strip():
            text.append(page_text)
    return '\n\n'.join(text)


def convert_pdf(pdf_path, library):
    """Convert a single PDF using the specified library."""
    if library == 'pdf_oxide':
        return extract_with_pdf_oxide(str(pdf_path))
    elif library == 'pdfplumber':
        return extract_with_pdfplumber(str(pdf_path))
    elif library == 'pymupdf':
        return extract_with_pymupdf(str(pdf_path))
    raise ValueError(f"Unknown library: {library}")


def main():
    """Convert all PDFs in docs/00-research/ to markdown."""
    script_dir = Path(__file__).parent.resolve()
    repo_root = script_dir.parent.parent
    research_dir = repo_root / 'docs' / '00-research'
    
    if not research_dir.exists():
        print(f"Directory not found: {research_dir}")
        sys.exit(1)
    
    pdf_files = list(research_dir.glob('*.pdf'))
    
    if not pdf_files:
        print("No PDF files found")
        return

    library = None
    for lib_name in ['pdf_oxide', 'pdfplumber', 'pymupdf']:
        lib = try_import(lib_name)
        if lib:
            library = lib
            print(f"Using library: {lib_name}")
            break

    if library is None:
        print("Error: No PDF library available.")
        print("Install one of: pdf_oxide, pdfplumber, pymupdf")
        sys.exit(1)

    for pdf_path in pdf_files:
        output_path = pdf_path.with_suffix('.md')

        if output_path.exists() and output_path.stat().st_mtime > pdf_path.stat().st_mtime:
            print(f"Skipping (already converted): {pdf_path.name}")
            continue

        try:
            text = convert_pdf(pdf_path, library)

            if text and text.strip():
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(text)
                print(f"Converted: {pdf_path.name} -> {output_path.name} ({len(text)} chars)")
            else:
                print(f"Empty content (scanned?): {pdf_path.name}")
        except Exception as e:
            print(f"Failed: {pdf_path.name} - {e}")


if __name__ == '__main__':
    main()