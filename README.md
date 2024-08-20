# Polygon and Polygon Sequence 

## Overview

This repository contains two modules:
1. `ConvexPolygon`: A class representing a regular convex polygon.
2. `PolygonSequence`: A sequence class for polygons with a common circumradius.

## ConvexPolygon Class

The `ConvexPolygon` class can calculate various properties of a regular polygon including:
- Number of edges
- Circumradius
- Interior angle
- Edge length
- Apothem
- Area
- Perimeter

The class also supports comparison based on the number of edges and circumradius.

### Usage
```python
from convex_polygon import ConvexPolygon

polygon = ConvexPolygon(5, 10)
print(polygon)
```
Output:
For the given Edges = 5 and Circumradius = 10
- Interior Angle = 108.0
- Edge Length = 11.76
- Apothem = 8.09
- Area = 237.26
- Perimeter = 58.8


## PolygonSequence Class

The `PolygonSequence` class allows creating a sequence of polygons with a common circumradius and provides functionalities such as:
- Retrieving polygons by index
- Finding the polygon with the highest area-to-perimeter ratio

### Usage
```python
from polygon_sequence import PolygonSequence

polygons = PolygonSequence(25, 10)
print(f"Most efficient polygon: {polygons.max_efficiency_polygon}")
```

Output:
Most efficient polygon: For the given Edges = 25 and Circumradius = 10
- Interior Angle = 165.6
- Edge Length = 2.48
- Apothem = 9.89
- Area = 307.73
- Perimeter = 62.0
