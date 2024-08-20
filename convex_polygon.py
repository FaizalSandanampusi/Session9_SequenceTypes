from math import sin, pi, cos

class ConvexPolygon:
    """
    A class to represent a regular strictly convex polygon.

    edges : int
        The number of edges (and vertices) of the polygon.
    circumradius : float
        The circumradius of the polygon (distance from the center to a vertex).
    """

    def __init__(self, edges: int, circumradius: float) -> None:
        """
        Initializes a ConvexPolygon with a given number of edges and circumradius.
        edges : int
            The number of edges (and vertices) of the polygon.
        circumradius : float
            The circumradius of the polygon.
        """
        if edges < 3:
            raise ValueError("A polygon must have at least 3 edges.")
        self._edges = edges
        self._circumradius = circumradius

    @property
    def edges(self) -> int:
        """Returns the number of edges of the polygon."""
        return self._edges

    @property
    def circumradius(self) -> float:
        """Returns the circumradius of the polygon."""
        return self._circumradius

    @property
    def interior_angle(self) -> float:
        """Returns the interior angle of the polygon."""
        return round((self.edges - 2) * (180 / self.edges), 2)

    @property
    def edge_length(self) -> float:
        """Returns the length of each edge of the polygon."""
        return round(2 * self.circumradius * sin(pi / self.edges), 2)

    @property
    def apothem(self) -> float:
        """Returns the apothem (distance from the center to the midpoint of an edge) of the polygon."""
        return round(self.circumradius * cos(pi / self.edges), 2)

    @property
    def area(self) -> float:
        """Returns the area of the polygon."""
        return round(0.5 * self.edges * self.edge_length * self.apothem, 2)

    @property
    def perimeter(self) -> float:
        """Returns the perimeter of the polygon."""
        return round(self.edges * self.edge_length, 2)

    def __repr__(self) -> str:
        """
        Returns a string representation of the ConvexPolygon object.
        """
        return (f"For the given Edges = {self.edges} and Circumradius = {self.circumradius}\n"
                f"Interior Angle = {self.interior_angle}\n"
                f"Edge Length = {self.edge_length}\n"
                f"Apothem = {self.apothem}\n"
                f"Area = {self.area}\n"
                f"Perimeter = {self.perimeter}\n")
