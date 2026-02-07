"""
Helper utilities for GenAI4Humanists notebooks.

This module provides utility functions for:
- Environment variable loading
- API client initialization (OpenAI, MultiOn)
- Course data visualization
"""

import os
from typing import Optional, Any
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from multion.client import MultiOn
import base64
from io import BytesIO
from PIL import Image
from IPython.display import display, HTML, Markdown


def load_env() -> None:
    """
    Load environment variables from .env file.

    Searches for .env file in current and parent directories and loads
    variables into the environment.
    """
    _ = load_dotenv(find_dotenv())


def get_openai_api_key() -> Optional[str]:
    """
    Retrieve OpenAI API key from environment variables.

    Returns:
        OpenAI API key string if set, None otherwise.
    """
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key


def get_openai_client() -> OpenAI:
    """
    Create and return an initialized OpenAI client.

    Returns:
        OpenAI: Configured OpenAI client instance.

    Raises:
        ValueError: If OPENAI_API_KEY is not set in environment.
    """
    openai_api_key = get_openai_api_key()
    return OpenAI(api_key=openai_api_key)


def get_multi_on_api_key() -> Optional[str]:
    """
    Retrieve MultiOn API key from environment variables.

    Returns:
        MultiOn API key string if set, None otherwise.
    """
    load_env()
    multi_on_api_key = os.getenv("MULTION_API_KEY")
    return multi_on_api_key


def get_multi_on_client() -> MultiOn:
    """
    Create and return an initialized MultiOn client.

    Returns:
        MultiOn: Configured MultiOn client instance for browser automation.

    Raises:
        ValueError: If MULTION_API_KEY is not set in environment.
    """
    multi_on_api_key = get_multi_on_api_key()
    return MultiOn(api_key=multi_on_api_key)


async def visualizeCourses(
    result: Any,
    screenshot: bytes,
    target_url: str,
    instructions: str,
    base_url: str
) -> None:
    """
    Display scraped course data and screenshots in Jupyter notebook.

    This function renders course information as an HTML table and displays
    a screenshot of the source website. It's designed for use in Jupyter
    notebooks with IPython.display.

    Args:
        result: Object containing courses attribute with course data.
               Expected to have courses with model_dump() method (Pydantic models).
        screenshot: Screenshot image data as bytes.
        target_url: The target URL that was scraped.
        instructions: Instructions used for scraping.
        base_url: Base URL for constructing course links.

    Note:
        This function displays output directly in Jupyter notebook and
        returns None. It handles both course data table rendering and
        screenshot visualization.
    """
    if result:
        # Convert each course to a dict (using model_dump from Pydantic v2)
        courses_data = [course.model_dump() for course in result.courses]

        for course in courses_data:
            if course.get('courseURL'):
                course['courseURL'] = (
                    f'<a href="{base_url}{course["courseURL"]}" '
                    f'target="_blank">{course["title"]}</a>'
                )

        # Build an HTML table if course data is available
        if courses_data:
            # Extract headers from the first course
            headers = courses_data[0].keys()
            table_html = '<table style="border-collapse: collapse; width: 100%;">'
            table_html += '<thead><tr>'
            for header in headers:
                table_html += (
                    f'<th style="border: 1px solid #dddddd; text-align: left; padding: 8px;">'
                    f'{header}</th>'
                )
            table_html += '</tr></thead>'
            table_html += '<tbody>'
            for course in courses_data:
                table_html += '<tr>'
                for header in headers:
                    value = course[header]
                    # If the field is "imageUrl", embed the image in the table cell
                    if header == "imageUrl":
                        value = (
                            f'<img src="{value}" alt="Course Image" '
                            f'style="max-width:100px; height:auto;">'
                        )
                    elif isinstance(value, list):
                        value = ', '.join(value)
                    table_html += (
                        f'<td style="border: 1px solid #dddddd; text-align: left; padding: 8px;">'
                        f'{value}</td>'
                    )
                table_html += '</tr>'
            table_html += '</tbody></table>'
        else:
            table_html = "<p>No course data available.</p>"

        # Display the course data table
        display(Markdown("### Scraped Course Data:"))
        display(HTML(table_html))

        # Convert the screenshot bytes into a base64 string and embed it in an <img> tag
        img_b64 = base64.b64encode(screenshot).decode('utf-8')
        img_html = (
            f'<img src="data:image/png;base64,{img_b64}" '
            f'alt="Website Screenshot" style="max-width:100%; height:auto;">'
        )
        display(Markdown("### Website Screenshot:"))
        display(HTML(img_html))
