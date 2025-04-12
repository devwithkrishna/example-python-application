"""
This module defines the data models used in the application.

Classes:
    UserColorEntry: A Pydantic model representing a user's name and their favorite color.
"""

from pydantic import BaseModel

class UserColorEntry(BaseModel):
    """
    Represents a user's name and their favorite color.

    Attributes:
        name (str): The name of the user.
        favorite_color (str): The user's favorite color.
    """
    name: str
    favorite_color: str
