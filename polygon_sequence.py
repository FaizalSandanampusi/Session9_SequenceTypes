
from convex_polygon import ConvexPolygon

class PolygonSequence:
    """
    A class to represent a sequence of convex polygons with a common circumradius.
    """

    def __init__(self, max_edges: int, circumradius: float) -> None:
        """
        Initializes a PolygonSequence with the maximum number of edges and a common circumradius.

        Parameters:
        max_edges : int
            The number of edges in the largest polygon in the sequence.
        circumradius : float
            The circumradius common to all polygons in the sequence.
        """
        if max_edges < 3:
            raise ValueError("A sequence must have at least 3 edges.")
        self.max_edges = max_edges
        self.circumradius = circumradius

    def __len__(self) -> int:
        """
        Returns the number of polygons in the sequence.
        """
        return self.max_edges - 2

    def __getitem__(self, s):
        """
        Returns a polygon or a list of polygons from the sequence.
        """
        if isinstance(s, int):
            s = s + 3
            if s < 3 or s > self.max_edges:
                raise IndexError("Index out of range.")
            return ConvexPolygon(s, self.circumradius)
        else:
            indices = range(*s.indices(self.max_edges - 2))
            return [ConvexPolygon(i + 3, self.circumradius) for i in indices]

    @property
    def max_efficiency_polygon(self) -> ConvexPolygon:
        """
        Returns the polygon with the highest area-to-perimeter ratio in the sequence.
        """
        return max(self, key=lambda p: p.area / p.perimeter)

    def __repr__(self) -> str:
        """
        Returns a string representation of the PolygonSequence object.
        """
        return f"PolygonSequence(max_edges={self.max_edges}, circumradius={self.circumradius})"
