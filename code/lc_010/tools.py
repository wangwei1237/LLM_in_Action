# !/usr/bin/env python3
"""
@discribe: example for tools.
@author: wangwei1237@gmail.com
"""
from langchain.tools import BaseTool
from math import pi
from typing import Union
from typing import Optional
from math import sqrt, cos, sin
  

class CircumferenceTool(BaseTool):
    """CircumferenceTool"""

    name = "Circumference calculator"
    description = "use this tool when you need to calculate a circumference using the radius of a circle"

    def _run(self, radius: Union[int, float]):
        """run"""
        return float(radius) * 2.0 * pi

    def _arun(self, radius: int):
        """arun"""
        raise NotImplementedError("This tool does not support async")
    

desc = (
    "use this tool when you need to calculate the length of a hypotenuse"
    "given one or two sides of a triangle and/or an angle (in degrees). "
    "To use the tool, you must provide at least two of the following parameters "
    "['adjacent_side', 'opposite_side', 'angle']."
)

class PythagorasTool(BaseTool):
    """PythagorasTool"""
    name = "Hypotenuse calculator"
    description = desc
    
    def _run(
        self,
        adjacent_side: Optional[Union[int, float]] = None,
        opposite_side: Optional[Union[int, float]] = None,
        angle: Optional[Union[int, float]] = None
    ):
        """run"""
        # check for the values we have been given
        if adjacent_side and opposite_side:
            return sqrt(float(adjacent_side)**2 + float(opposite_side)**2)
        elif adjacent_side and angle:
            return float(adjacent_side) / cos(float(angle))
        elif opposite_side and angle:
            return float(opposite_side) / sin(float(angle))
        else:
            return "Could not calculate the hypotenuse of the triangle. "
    
    def _arun(self, query: str):
        """arun"""
        raise NotImplementedError("This tool does not support async")

if "__main__" == __name__:
    c =  CircumferenceTool()
    res = c.run({'radius': 1})
    print(res)

    c1 = PythagorasTool()
    res = c1.run({'adjacent_side': 3, 'opposite_side': 4})
    print(res)