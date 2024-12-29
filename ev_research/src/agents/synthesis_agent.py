"""Agent for converting reports between different formats."""

import os
import subprocess
from typing import Optional
from .base_agent import BaseAgent
from ..models.data_models import ResearchReport

class SynthesisAgent(BaseAgent):
    """Agent for converting reports between different formats."""
    
    def __init__(self, gemini_api_key: str, model_name: str, temperature: float = 0.7):
        """Initialize the synthesis agent."""
        super().__init__(gemini_api_key, model_name, temperature)
        self.pdflatex_path = "/Library/TeX/texbin/pdflatex"
    
    async def convert_report(self, report: ResearchReport, output_path: str, format: str = "markdown") -> Optional[str]:
        """
        Convert a report to different formats.
        
        Args:
            report: ResearchReport object to convert
            output_path: Path to save the converted file
            format: Target format (markdown, pdf, or docx)
            
        Returns:
            Error message if conversion fails, None otherwise
        """
        # First save as markdown
        md_path = output_path.replace(f".{format}", ".md")
        with open(md_path, "w") as f:
            f.write(report.to_markdown())
            
        # If target format is markdown, we're done
        if format == "markdown":
            return None
            
        # Convert to target format
        result = await self.convert_format(md_path, output_path, format)
        
        # Clean up markdown file if it was temporary
        if format != "markdown":
            os.remove(md_path)
            
        return result
    
    async def convert_format(self, input_path: str, output_path: str, output_format: str) -> Optional[str]:
        """
        Convert a file from markdown to the specified format.
        
        Args:
            input_path: Path to input markdown file
            output_path: Path to save the converted file
            output_format: Target format (pdf or docx)
            
        Returns:
            Error message if conversion fails, None otherwise
        """
        try:
            # Check if pandoc is installed
            try:
                subprocess.run(['pandoc', '--version'], check=True, capture_output=True)
            except (subprocess.CalledProcessError, FileNotFoundError):
                return "Error: pandoc is not installed. Please install pandoc to enable format conversion."
            
            # For PDF, check if LaTeX is installed
            if output_format == 'pdf':
                try:
                    subprocess.run([self.pdflatex_path, '--version'], check=True, capture_output=True)
                except (subprocess.CalledProcessError, FileNotFoundError):
                    return "Error: LaTeX is not installed. Please install MacTeX for PDF generation."
            
            # Build the pandoc command
            cmd = [
                'pandoc',
                input_path,
                '-o', output_path,
                '--from=markdown',
                f'--to={output_format}'
            ]
            
            # Add PDF-specific options
            if output_format == 'pdf':
                cmd.extend([
                    '--pdf-engine=' + self.pdflatex_path,
                    '--variable=geometry:margin=1in'
                ])
            
            # Run the conversion
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            
            # Check if output file was created
            if not os.path.exists(output_path):
                return f"Error: Failed to create {output_format.upper()} file. Pandoc completed but output file is missing."
                
            return None
            
        except subprocess.CalledProcessError as e:
            return f"Error during conversion: {e.stderr}"
        except Exception as e:
            return f"Unexpected error during conversion: {str(e)}"
