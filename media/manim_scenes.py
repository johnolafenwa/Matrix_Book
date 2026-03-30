from manim import *
import numpy as np

config.background_color = "#FCFAF4"

INK = "#1F2623"
TEAL = "#0F766E"
TEAL_LIGHT = "#CBEDEA"
GOLD = "#D39534"
RED = "#D95D5D"
BLUE = "#3C6E8F"
GREEN = "#2F9E7C"
PURPLE = "#7C5C99"
GRID = "#BFD4CE"


def make_title(title: str, subtitle: str | None = None):
    headline = Text(title, color=INK, font_size=40, weight=BOLD).to_edge(UP)
    if subtitle is None:
        return VGroup(headline)

    deck = Text(subtitle, color=TEAL, font_size=24).next_to(headline, DOWN, buff=0.18)
    return VGroup(headline, deck)


def make_plane():
    return NumberPlane(
        x_range=[-4, 4, 1],
        y_range=[-3, 3, 1],
        background_line_style={
            "stroke_color": GRID,
            "stroke_opacity": 0.55,
            "stroke_width": 1.6,
        },
        axis_config={
            "stroke_color": "#7E948E",
            "stroke_width": 2,
        },
    )


def rotation_matrix(theta: float):
    return np.array(
        [
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)],
        ]
    )


class BasisVectorsTransform(Scene):
    def construct(self):
        title = make_title("A Matrix Moves The Basis Vectors", "The columns of A are the moved basis arrows.")
        plane = make_plane()

        square = Square(
            side_length=1,
            stroke_color=TEAL,
            stroke_width=4,
            fill_color=TEAL_LIGHT,
            fill_opacity=0.6,
        ).move_to([0.5, 0.5, 0])
        e1 = Arrow(ORIGIN, RIGHT, buff=0, color=RED, stroke_width=8)
        e2 = Arrow(ORIGIN, UP, buff=0, color=GREEN, stroke_width=8)
        transform_group = VGroup(plane, square, e1, e2)

        label_e1 = Text("e1", color=RED, font_size=24).next_to(e1.get_end(), DOWN, buff=0.18)
        label_e2 = Text("e2", color=GREEN, font_size=24).next_to(e2.get_end(), LEFT, buff=0.18)
        caption = Text("Start with the two basic arrows.", color=INK, font_size=24).to_edge(DOWN)

        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(Create(plane), DrawBorderThenFill(square), GrowArrow(e1), GrowArrow(e2))
        self.play(FadeIn(label_e1), FadeIn(label_e2), FadeIn(caption))

        self.play(FadeOut(label_e1), FadeOut(label_e2), Transform(caption, Text("Apply A = [[2, 1], [0, 1]].", color=INK, font_size=24).to_edge(DOWN)))
        self.play(ApplyMatrix([[2, 1], [0, 1]], transform_group), run_time=3)

        moved_label_1 = Text("A e1", color=RED, font_size=24).next_to(e1.get_end(), DOWN, buff=0.18)
        moved_label_2 = Text("A e2", color=GREEN, font_size=24).next_to(e2.get_end(), LEFT, buff=0.18)
        end_caption = Text("Those moved arrows are the columns of A.", color=TEAL, font_size=24).to_edge(DOWN)
        self.play(FadeIn(moved_label_1), FadeIn(moved_label_2), Transform(caption, end_caption))
        self.wait(1.2)


class DeterminantAreaScale(Scene):
    def construct(self):
        title = make_title("Determinant As Area Scale", "The unit square turns into a new shape.")
        plane = make_plane()
        square = Square(
            side_length=1,
            stroke_color=GOLD,
            stroke_width=4,
            fill_color=GOLD,
            fill_opacity=0.35,
        ).move_to([0.5, 0.5, 0])
        e1 = Arrow(ORIGIN, RIGHT, buff=0, color=RED, stroke_width=7)
        e2 = Arrow(ORIGIN, UP, buff=0, color=GREEN, stroke_width=7)
        group = VGroup(plane, square, e1, e2)

        caption = Text("Area = 1", color=INK, font_size=26).to_edge(DOWN)

        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(Create(plane), DrawBorderThenFill(square), GrowArrow(e1), GrowArrow(e2))
        self.play(FadeIn(caption))
        self.play(Transform(caption, Text("Apply A = [[2, 1], [0, 1.5]].", color=INK, font_size=26).to_edge(DOWN)))
        self.play(ApplyMatrix([[2, 1], [0, 1.5]], group), run_time=3)
        self.play(Transform(caption, Text("det(A) = 3, so the area triples.", color=GOLD, font_size=26).to_edge(DOWN)))
        self.wait(1.2)


class LeastSquaresProjection(Scene):
    def construct(self):
        title = make_title("Least Squares Is Projection", "Drop to the closest point on the line.")
        plane = make_plane()

        direction = np.array([3.0, 1.5, 0.0])
        direction_unit = direction / np.linalg.norm(direction)
        point = np.array([1.2, 2.7, 0.0])
        projection = (np.dot(point[:2], direction[:2]) / np.dot(direction[:2], direction[:2])) * direction

        line = Line(-4 * direction_unit, 4 * direction_unit, color=TEAL, stroke_width=6)
        point_arrow = Arrow(ORIGIN, point, buff=0, color=GOLD, stroke_width=8)
        proj_arrow = Arrow(ORIGIN, projection, buff=0, color=TEAL, stroke_width=8)
        residual = DashedLine(point, projection, dash_length=0.14, color=RED, stroke_width=5)
        point_dot = Dot(point, color=GOLD, radius=0.08)
        proj_dot = Dot(projection, color=TEAL, radius=0.08)
        right_angle = RightAngle(Line(projection, projection + direction_unit), Line(projection, point), length=0.2, color=INK)
        caption = Text("The best approximation is the perpendicular drop.", color=INK, font_size=24).to_edge(DOWN)

        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(Create(plane), Create(line))
        self.play(GrowArrow(point_arrow), FadeIn(point_dot))
        self.play(GrowArrow(proj_arrow), FadeIn(proj_dot), Create(residual), Create(right_angle))
        self.play(FadeIn(caption))
        self.wait(1.3)


class EigenvectorDirections(Scene):
    def construct(self):
        title = make_title("Eigenvectors Keep Their Lines", "Other arrows bend into new directions.")
        plane = make_plane()
        line_one = DashedLine([-3, -3, 0], [3, 3, 0], color=GOLD, dash_length=0.14)
        line_two = DashedLine([-3, 3, 0], [3, -3, 0], color=GOLD, dash_length=0.14)

        matrix = np.array([[2, 1], [1, 2]])
        seeds = [
            np.array([1.0, 1.0, 0.0]),
            np.array([1.0, -1.0, 0.0]),
            np.array([1.8, 0.4, 0.0]),
            np.array([0.6, 1.6, 0.0]),
            np.array([-1.5, 0.7, 0.0]),
            np.array([-0.5, -1.7, 0.0]),
        ]
        colors = [GOLD, GOLD, TEAL, BLUE, GREEN, PURPLE]
        arrows = VGroup()
        targets = VGroup()
        for vec, color in zip(seeds, colors):
            arrows.add(Arrow(ORIGIN, vec, buff=0, color=color, stroke_width=7))
            transformed = matrix @ vec[:2]
            targets.add(Arrow(ORIGIN, [transformed[0], transformed[1], 0], buff=0, color=color, stroke_width=7))

        caption = Text("The gold arrows stay on the same lines.", color=INK, font_size=24).to_edge(DOWN)

        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(Create(plane), Create(line_one), Create(line_two))
        self.play(*[GrowArrow(arrow) for arrow in arrows], FadeIn(caption))
        self.play(Transform(arrows, targets), run_time=3)
        self.wait(1.2)


class SVDRotateStretchRotate(Scene):
    def construct(self):
        title = make_title("SVD: Rotate, Stretch, Rotate", "A hard transformation becomes three simple moves.")
        circle = Circle(radius=1.05, stroke_color=BLUE, stroke_width=5, fill_color=BLUE, fill_opacity=0.16)
        axis_x = Arrow(ORIGIN, RIGHT, buff=0, color=RED, stroke_width=8)
        axis_y = Arrow(ORIGIN, UP, buff=0, color=GREEN, stroke_width=8)
        frame = VGroup(circle, axis_x, axis_y)
        caption = Text("1. Rotate", color=INK, font_size=24).to_edge(DOWN)

        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(Create(circle), GrowArrow(axis_x), GrowArrow(axis_y), FadeIn(caption))

        self.play(ApplyMatrix(rotation_matrix(np.deg2rad(35)), frame), run_time=2.4)
        self.play(Transform(caption, Text("2. Stretch along perpendicular directions", color=INK, font_size=24).to_edge(DOWN)))
        self.play(ApplyMatrix([[2.2, 0], [0, 0.8]], frame), run_time=2.6)
        self.play(Transform(caption, Text("3. Rotate again to get the final ellipse", color=INK, font_size=24).to_edge(DOWN)))
        self.play(ApplyMatrix(rotation_matrix(np.deg2rad(-25)), frame), run_time=2.4)
        self.play(Transform(caption, Text("That is the geometric heart of SVD.", color=TEAL, font_size=24).to_edge(DOWN)))
        self.wait(1.2)
