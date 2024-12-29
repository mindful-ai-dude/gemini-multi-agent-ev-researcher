"""Base agent class for the EV Research application."""

import google.generativeai as genai
from typing import Any, Dict
from ..config.settings import GEMINI_MODEL, GEMINI_FALLBACK_MODEL, DEFAULT_TEMPERATURE

class BaseAgent:
    """Base agent class with common Gemini AI functionality."""
    
    def __init__(self, api_key: str, model_name: str = GEMINI_MODEL, temperature: float = DEFAULT_TEMPERATURE):
        """Initialize the base agent."""
        self.api_key = api_key
        self.model_name = model_name
        self.temperature = temperature
        self.fallback_model = GEMINI_FALLBACK_MODEL
        
        # Configure the Gemini API
        genai.configure(api_key=self.api_key)
        
    async def generate_content_async(self, prompt: str) -> str:
        """
        Generate content using Gemini AI with fallback support.
        
        Args:
            prompt: The prompt to send to the model
            
        Returns:
            Generated content as string
        """
        try:
            # Try with primary model
            model = genai.GenerativeModel(self.model_name)
            response = await model.generate_content_async(
                prompt,
                generation_config={"temperature": self.temperature}
            )
            return response.text
            
        except Exception as e:
            print(f"Warning: Primary model failed ({str(e)}), falling back to {self.fallback_model}")
            try:
                # Fallback to secondary model
                model = genai.GenerativeModel(self.fallback_model)
                response = await model.generate_content_async(
                    prompt,
                    generation_config={"temperature": self.temperature}
                )
                return response.text
                
            except Exception as e2:
                raise Exception(f"Both primary and fallback models failed. Primary: {str(e)}, Fallback: {str(e2)}")
    
    def _format_data_for_prompt(self, data: Dict[str, Any]) -> str:
        """Format data dictionary into a string for prompts."""
        return "\n".join(f"{key}: {value}" for key, value in data.items())
