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
PACE = 1.6


def paced(seconds: float):
    return round(seconds * PACE, 2)


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


def make_caption(text: str, color: str = INK):
    return Text(text, color=color, font_size=24).to_edge(DOWN)


def make_text_matrix(data, font_size=34, cell_width=1.0, cell_height=0.76):
    rows = len(data)
    cols = len(data[0])
    entry_groups = []
    row_groups = []

    for i, row in enumerate(data):
        row_group = VGroup()
        for j, value in enumerate(row):
            box = RoundedRectangle(
                width=cell_width,
                height=cell_height,
                corner_radius=0.1,
                stroke_color=GRID,
                stroke_width=1.6,
                fill_opacity=0,
            )
            label = Text(str(value), color=INK, font_size=font_size)
            entry = VGroup(box, label)
            entry.move_to(
                np.array(
                    [
                        (j - (cols - 1) / 2) * cell_width * 1.12,
                        ((rows - 1) / 2 - i) * cell_height * 1.26,
                        0,
                    ]
                )
            )
            label.move_to(box.get_center())
            row_group.add(entry)
            entry_groups.append(entry)
        row_groups.append(row_group)

    column_groups = []
    for j in range(cols):
        column_groups.append(VGroup(*[row_groups[i][j] for i in range(rows)]))

    body = VGroup(*entry_groups)
    left_bracket = VMobject(color=INK, stroke_width=4)
    left_bracket.set_points_as_corners(
        [
            body.get_corner(UL) + LEFT * 0.34 + UP * 0.16,
            body.get_corner(UL) + LEFT * 0.16 + UP * 0.16,
            body.get_corner(DL) + LEFT * 0.16 + DOWN * 0.16,
            body.get_corner(DL) + LEFT * 0.34 + DOWN * 0.16,
        ]
    )
    right_bracket = VMobject(color=INK, stroke_width=4)
    right_bracket.set_points_as_corners(
        [
            body.get_corner(UR) + RIGHT * 0.34 + UP * 0.16,
            body.get_corner(UR) + RIGHT * 0.16 + UP * 0.16,
            body.get_corner(DR) + RIGHT * 0.16 + DOWN * 0.16,
            body.get_corner(DR) + RIGHT * 0.34 + DOWN * 0.16,
        ]
    )

    matrix_group = VGroup(left_bracket, body, right_bracket)
    return matrix_group, row_groups, column_groups, entry_groups


def line_from_slope_intercept(m: float, b: float, color: str):
    x1, x2 = -4.5, 4.5
    return Line(
        [x1, m * x1 + b, 0],
        [x2, m * x2 + b, 0],
        color=color,
        stroke_width=6,
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
        self.play(ApplyMatrix([[2, 1], [0, 1]], transform_group), run_time=paced(3))

        moved_label_1 = Text("A e1", color=RED, font_size=24).next_to(e1.get_end(), DOWN, buff=0.18)
        moved_label_2 = Text("A e2", color=GREEN, font_size=24).next_to(e2.get_end(), LEFT, buff=0.18)
        end_caption = Text("Those moved arrows are the columns of A.", color=TEAL, font_size=24).to_edge(DOWN)
        self.play(FadeIn(moved_label_1), FadeIn(moved_label_2), Transform(caption, end_caption))
        self.wait(paced(1.2))


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
        self.play(ApplyMatrix([[2, 1], [0, 1.5]], group), run_time=paced(3))
        self.play(Transform(caption, Text("det(A) = 3, so the area triples.", color=GOLD, font_size=26).to_edge(DOWN)))
        self.wait(paced(1.2))


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
        self.wait(paced(1.3))


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
        self.play(Transform(arrows, targets), run_time=paced(3))
        self.wait(paced(1.2))


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

        self.play(ApplyMatrix(rotation_matrix(np.deg2rad(35)), frame), run_time=paced(2.4))
        self.play(Transform(caption, Text("2. Stretch along perpendicular directions", color=INK, font_size=24).to_edge(DOWN)))
        self.play(ApplyMatrix([[2.2, 0], [0, 0.8]], frame), run_time=paced(2.6))
        self.play(Transform(caption, Text("3. Rotate again to get the final ellipse", color=INK, font_size=24).to_edge(DOWN)))
        self.play(ApplyMatrix(rotation_matrix(np.deg2rad(-25)), frame), run_time=paced(2.4))
        self.play(Transform(caption, Text("That is the geometric heart of SVD.", color=TEAL, font_size=24).to_edge(DOWN)))
        self.wait(paced(1.2))


class RowColumnStories(Scene):
    def construct(self):
        title = make_title("Rows And Columns Tell Different Stories", "One matrix can answer two different questions.")
        matrix, row_groups, column_groups, _ = make_text_matrix(
            [[78, 82, 91], [65, 70, 68], [88, 84, 90]],
            font_size=32,
            cell_width=1.1,
            cell_height=0.8,
        )
        matrix.scale(0.95)
        row_box = SurroundingRectangle(row_groups[0], color=GOLD, buff=0.14, corner_radius=0.08)
        col_box = SurroundingRectangle(column_groups[1], color=TEAL, buff=0.14, corner_radius=0.08)
        caption = make_caption("A row can mean one student's full profile.")

        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(FadeIn(matrix, shift=UP * 0.1))
        self.play(Create(row_box), FadeIn(caption))
        self.wait(paced(0.8))
        self.play(Transform(row_box, col_box), Transform(caption, make_caption("A column can mean one exam across all students.", TEAL)))
        self.wait(paced(1.1))


class MatrixProductColumns(Scene):
    def construct(self):
        title = make_title("Matrix Products Push Columns Through", "Each column of B is transformed by A.")
        plane = make_plane()
        b1 = np.array([1.2, 2.0, 0.0])
        b2 = np.array([2.2, 1.0, 0.0])
        matrix = np.array([[1.6, 0.7], [0.2, 1.3]])

        arrow1 = Arrow(ORIGIN, b1, buff=0, color=BLUE, stroke_width=8)
        arrow2 = Arrow(ORIGIN, b2, buff=0, color=PURPLE, stroke_width=8)
        target1 = Arrow(ORIGIN, [*(matrix @ b1[:2]), 0], buff=0, color=BLUE, stroke_width=8)
        target2 = Arrow(ORIGIN, [*(matrix @ b2[:2]), 0], buff=0, color=PURPLE, stroke_width=8)
        caption = make_caption("Start with the columns of B as input arrows.")

        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(Create(plane), GrowArrow(arrow1), GrowArrow(arrow2), FadeIn(caption))
        self.play(Transform(caption, make_caption("Now A pushes each column into a new column of AB.")))
        self.play(Transform(arrow1, target1), Transform(arrow2, target2), run_time=paced(2.8))
        self.play(Transform(caption, make_caption("That is the column-combination view of matrix multiplication.", TEAL)))
        self.wait(paced(1.1))


class SystemIntersectionCases(Scene):
    def construct(self):
        title = make_title("Systems As Intersections", "One crossing, none, or infinitely many.")
        plane = make_plane()
        line_a = line_from_slope_intercept(1, 1, TEAL)
        line_b = line_from_slope_intercept(-1, 1, GOLD)
        point = Dot([0, 1, 0], color=RED, radius=0.08)
        caption = make_caption("One intersection means one solution.")

        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(Create(plane), Create(line_a), Create(line_b), FadeIn(point), FadeIn(caption))
        self.wait(paced(0.8))

        parallel_a = line_from_slope_intercept(1, 1.2, TEAL)
        parallel_b = line_from_slope_intercept(1, -0.8, GOLD)
        self.play(
            Transform(line_a, parallel_a),
            Transform(line_b, parallel_b),
            FadeOut(point),
            Transform(caption, make_caption("Parallel lines mean no solution.", RED)),
        )
        self.wait(paced(0.8))

        same_line = line_from_slope_intercept(0.7, 0.4, TEAL)
        same_line_2 = line_from_slope_intercept(0.7, 0.4, GOLD)
        self.play(
            Transform(line_a, same_line),
            Transform(line_b, same_line_2),
            Transform(caption, make_caption("The same line means infinitely many solutions.", GOLD)),
        )
        self.wait(paced(1.1))


class PivotStaircase(Scene):
    def construct(self):
        title = make_title("Pivot Positions Form A Staircase", "Each pivot moves down and to the right.")
        matrix, _, _, entries = make_text_matrix(
            [[1, 2, -1, 4], [0, 3, 5, 7], [0, 0, 2, 6]],
            font_size=32,
            cell_width=0.95,
            cell_height=0.78,
        )
        matrix.scale(0.92)
        pivot_boxes = [
            SurroundingRectangle(entries[0], color=RED, buff=0.1, corner_radius=0.08),
            SurroundingRectangle(entries[5], color=GOLD, buff=0.1, corner_radius=0.08),
            SurroundingRectangle(entries[10], color=TEAL, buff=0.1, corner_radius=0.08),
        ]
        staircase = VMobject(color=PURPLE, stroke_width=5)
        staircase.set_points_as_corners(
            [
                pivot_boxes[0].get_center() + DOWN * 0.35,
                pivot_boxes[0].get_center() + RIGHT * 1.15 + DOWN * 0.35,
                pivot_boxes[1].get_center() + RIGHT * 0.3 + DOWN * 0.35,
                pivot_boxes[1].get_center() + RIGHT * 1.1 + DOWN * 0.35,
                pivot_boxes[2].get_center() + RIGHT * 0.3 + DOWN * 0.35,
            ]
        )
        caption = make_caption("Pivot positions create the staircase shape.")

        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(FadeIn(matrix))
        for box in pivot_boxes:
            self.play(Create(box))
        self.play(Create(staircase), FadeIn(caption))
        self.wait(paced(1.1))


class InverseUndo(Scene):
    def construct(self):
        title = make_title("An Inverse Undoes The Transformation", "Apply A, then apply A inverse, and you come back.")
        plane = make_plane()
        shape = Polygon(
            [0, 0, 0],
            [1.2, 0.2, 0],
            [0.7, 1.1, 0],
            color=TEAL,
            stroke_width=5,
            fill_color=TEAL_LIGHT,
            fill_opacity=0.55,
        )
        e1 = Arrow(ORIGIN, RIGHT, buff=0, color=RED, stroke_width=7)
        e2 = Arrow(ORIGIN, UP, buff=0, color=GREEN, stroke_width=7)
        group = VGroup(plane, shape, e1, e2)
        A = np.array([[1.5, 0.6], [0.2, 1.2]])
        A_inv = np.linalg.inv(A)
        caption = make_caption("First the grid and shape are transformed by A.")

        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(Create(plane), DrawBorderThenFill(shape), GrowArrow(e1), GrowArrow(e2), FadeIn(caption))
        self.play(ApplyMatrix(A, group), run_time=paced(2.8))
        self.play(Transform(caption, make_caption("Now A inverse reverses the move exactly.", TEAL)))
        self.play(ApplyMatrix(A_inv, group), run_time=paced(2.8))
        self.wait(paced(1.1))


class FactorizationSteps(Scene):
    def construct(self):
        title = make_title("Factorization Breaks A Big Move Into Small Moves", "Simple pieces are easier to understand and compute with.")
        plane = make_plane()
        square = Square(
            side_length=1.2,
            stroke_color=GOLD,
            stroke_width=5,
            fill_color=GOLD,
            fill_opacity=0.3,
        ).move_to([0.6, 0.6, 0])
        group = VGroup(plane, square)
        caption = make_caption("Start with one shape on the grid.")

        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(Create(plane), DrawBorderThenFill(square), FadeIn(caption))

        self.play(Transform(caption, make_caption("Step 1: a lower-triangular shear.")))
        self.play(ApplyMatrix([[1, 0], [0.7, 1]], group), run_time=paced(2.2))

        self.play(Transform(caption, make_caption("Step 2: an upper-triangular shear.")))
        self.play(ApplyMatrix([[1, 0.9], [0, 1]], group), run_time=paced(2.2))

        self.play(Transform(caption, make_caption("Step 3: a simple scaling.")))
        self.play(ApplyMatrix([[1.3, 0], [0, 0.85]], group), run_time=paced(2.2))
        self.play(Transform(caption, make_caption("Together, these simple pieces build the full transformation.", TEAL)))
        self.wait(paced(1.1))


class SpanToPlane(Scene):
    def construct(self):
        title = make_title("Span Grows From A Line To A Plane", "Independent vectors unlock more directions.")
        plane = make_plane()
        v1 = np.array([2.0, 0.8, 0.0])
        v2 = np.array([0.8, 1.8, 0.0])
        arrow1 = Arrow(ORIGIN, v1, buff=0, color=RED, stroke_width=8)
        arrow2 = Arrow(ORIGIN, v2, buff=0, color=GREEN, stroke_width=8)
        span_line = Line(-2.4 * v1, 2.4 * v1, color=RED, stroke_width=5)
        lattice = VGroup()
        for i in range(-2, 3):
            for j in range(-2, 3):
                lattice.add(Dot(i * v1 + j * v2, radius=0.04, color=TEAL))
        caption = make_caption("One nonzero vector spans a line.")

        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(Create(plane), GrowArrow(arrow1), Create(span_line), FadeIn(caption))
        self.play(GrowArrow(arrow2), Transform(caption, make_caption("Add an independent vector, and combinations fill the plane.")))
        self.play(FadeIn(lattice, lag_ratio=0.02, run_time=paced(2.2)))
        self.wait(paced(1.1))


class NullSpaceCollapse(Scene):
    def construct(self):
        title = make_title("Null Space Directions Disappear", "Different inputs can collapse to the same output.")
        plane = make_plane()
        p1 = np.array([1.2, 0.8, 0.0])
        p2 = np.array([0.6, 1.4, 0.0])
        arrow1 = Arrow(ORIGIN, p1, buff=0, color=BLUE, stroke_width=8)
        arrow2 = Arrow(ORIGIN, p2, buff=0, color=PURPLE, stroke_width=8)
        dot1 = Dot(p1, color=BLUE, radius=0.08)
        dot2 = Dot(p2, color=PURPLE, radius=0.08)
        connector = DashedLine(p1, p2, color=GOLD, dash_length=0.15, stroke_width=5)
        group = VGroup(arrow1, arrow2, dot1, dot2, connector)
        caption = make_caption("These two inputs are different before the transformation.")

        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(Create(plane), GrowArrow(arrow1), GrowArrow(arrow2), FadeIn(dot1), FadeIn(dot2), Create(connector), FadeIn(caption))
        self.play(Transform(caption, make_caption("A singular matrix collapses their difference into the null space.", TEAL)))
        self.play(ApplyMatrix([[1, 1], [0, 0]], group), run_time=paced(2.8))
        self.wait(paced(1.1))


class OrthonormalCoordinates(Scene):
    def construct(self):
        title = make_title("Orthonormal Axes Remove Skew", "Perpendicular unit directions make geometry cleaner.")
        plane = make_plane()
        basis1 = Arrow(ORIGIN, [1.8, 0.2, 0], buff=0, color=RED, stroke_width=8)
        basis2 = Arrow(ORIGIN, [0.9, 1.6, 0], buff=0, color=GREEN, stroke_width=8)
        point = Arrow(ORIGIN, [2.7, 1.8, 0], buff=0, color=GOLD, stroke_width=8)
        skew_cell = Polygon(ORIGIN, basis1.get_end(), basis1.get_end() + basis2.get_end(), basis2.get_end(), color=TEAL, fill_color=TEAL_LIGHT, fill_opacity=0.28, stroke_width=4)
        frame = VGroup(basis1, basis2, point, skew_cell)
        caption = make_caption("A skewed basis works, but distances and angles are awkward.")

        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(Create(plane), GrowArrow(basis1), GrowArrow(basis2), GrowArrow(point), DrawBorderThenFill(skew_cell), FadeIn(caption))
        self.play(Transform(caption, make_caption("Rotate and rescale to an orthonormal basis.")))
        self.play(ApplyMatrix([[1, -0.5], [-0.1, 1.2]], frame), run_time=paced(2.6))
        self.play(Transform(caption, make_caption("Now the axes are cleaner, and geometry is easier to read.", TEAL)))
        self.wait(paced(1.1))


class DiagonalDynamics(Scene):
    def construct(self):
        title = make_title("Repeated Dynamics Reveal The Dominant Direction", "Diagonalization explains why the motion simplifies.")
        plane = make_plane()
        theta = np.deg2rad(30)
        A = rotation_matrix(theta) @ np.array([[1.35, 0], [0, 0.65]]) @ rotation_matrix(-theta)
        eigenline = Line(
            -4 * np.array([np.cos(theta), np.sin(theta), 0]),
            4 * np.array([np.cos(theta), np.sin(theta), 0]),
            color=GOLD,
            stroke_width=5,
        )
        vector = np.array([1.3, 2.2, 0.0])
        arrow = Arrow(ORIGIN, vector, buff=0, color=TEAL, stroke_width=8)
        history = VGroup()
        caption = make_caption("Repeated multiplication bends the state toward the dominant eigenvector.")

        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(Create(plane), Create(eigenline), GrowArrow(arrow), FadeIn(caption))
        current = vector
        for _ in range(4):
            history.add(Dot(current, radius=0.05, color=BLUE))
            new = np.array([*(A @ current[:2]), 0])
            self.play(FadeIn(history[-1]), Transform(arrow, Arrow(ORIGIN, new, buff=0, color=TEAL, stroke_width=8)), run_time=paced(1.1))
            current = new
        self.wait(paced(1.1))


class MarkovFlow(Scene):
    def construct(self):
        title = make_title("Probability Mass Flows Through The Network", "Repeated multiplication settles toward a steady pattern.")
        positions = [LEFT * 3 + DOWN * 0.6, ORIGIN + UP * 1.0, RIGHT * 3 + DOWN * 0.6]
        outlines = VGroup()
        labels = VGroup()
        for i, pos in enumerate(positions, start=1):
            outlines.add(Circle(radius=0.62, color=INK, stroke_width=4).move_to(pos))
            labels.add(Text(str(i), color=INK, font_size=28).move_to(pos))

        edges = VGroup(
            CurvedArrow(positions[0] + UP * 0.2, positions[1] + LEFT * 0.2, angle=-0.5, color=TEAL),
            CurvedArrow(positions[1] + RIGHT * 0.2, positions[2] + UP * 0.1, angle=-0.5, color=TEAL),
            CurvedArrow(positions[2] + DOWN * 0.2, positions[0] + DOWN * 0.2, angle=-0.45, color=TEAL),
            CurvedArrow(positions[1] + DOWN * 0.2, positions[0] + UP * 0.1, angle=-0.4, color=GOLD),
            CurvedArrow(positions[2] + LEFT * 0.2, positions[1] + RIGHT * 0.1, angle=-0.4, color=GOLD),
        )

        states = [
            np.array([1.0, 0.0, 0.0]),
            np.array([0.2, 0.6, 0.2]),
            np.array([0.24, 0.38, 0.38]),
            np.array([0.28, 0.34, 0.38]),
            np.array([0.29, 0.34, 0.37]),
        ]

        def mass_group(state):
            group = VGroup()
            for prob, pos in zip(state, positions):
                radius = 0.12 + 0.42 * np.sqrt(prob)
                fill = Circle(radius=radius, fill_color=TEAL_LIGHT, fill_opacity=0.9, stroke_color=TEAL, stroke_width=3).move_to(pos)
                group.add(fill)
            return group

        masses = mass_group(states[0])
        caption = make_caption("At first, all the mass sits at one node.")

        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(Create(edges), Create(outlines), FadeIn(labels), FadeIn(masses), FadeIn(caption))
        for state in states[1:-1]:
            self.play(Transform(masses, mass_group(state)), run_time=paced(1.2))
        self.play(
            Transform(masses, mass_group(states[-1])),
            Transform(caption, make_caption("After several steps, the distribution stabilizes.", TEAL)),
            run_time=paced(1.4),
        )
        self.wait(paced(1.1))


class PCAProjection(Scene):
    def construct(self):
        title = make_title("PCA Keeps The Dominant Direction", "A cloud of points can be summarized by its main axis.")
        plane = make_plane()
        points = [
            np.array([-2.5, -1.8, 0]), np.array([-2.0, -1.1, 0]), np.array([-1.4, -1.2, 0]),
            np.array([-0.8, -0.3, 0]), np.array([-0.1, -0.1, 0]), np.array([0.7, 0.5, 0]),
            np.array([1.1, 0.7, 0]), np.array([1.8, 1.0, 0]), np.array([2.4, 1.8, 0]),
        ]
        dots = VGroup(*[Dot(point, radius=0.06, color=BLUE) for point in points])
        direction = np.array([1.0, 0.7, 0.0])
        unit = direction / np.linalg.norm(direction)
        line = Line(-4 * unit, 4 * unit, color=TEAL, stroke_width=6)

        projected = []
        for point in points:
            t = np.dot(point[:2], direction[:2]) / np.dot(direction[:2], direction[:2])
            projected.append(np.array([*(t * direction[:2]), 0]))
        projected_dots = VGroup(*[Dot(point, radius=0.06, color=GOLD) for point in projected])
        caption = make_caption("The point cloud has one dominant direction of variation.")

        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(Create(plane), FadeIn(dots, lag_ratio=0.04), Create(line), FadeIn(caption))
        self.play(Transform(dots, projected_dots), Transform(caption, make_caption("Projecting onto that line keeps the main pattern in one dimension.", TEAL)), run_time=paced(2.4))
        self.wait(paced(1.1))


class ContinuousPhasePortrait(Scene):
    def construct(self):
        title = make_title("Continuous Systems Flow Through Time", "Trajectories move every instant, not in jumps.")
        plane = make_plane()
        seeds = [np.array([2.4, 0.6, 0]), np.array([0.8, 2.2, 0]), np.array([-2.2, 0.7, 0]), np.array([-1.0, -2.1, 0])]
        colors = [TEAL, GOLD, BLUE, PURPLE]

        dots = VGroup()
        traces = VGroup()
        for seed, color in zip(seeds, colors):
            dot = Dot(seed, color=color, radius=0.07)
            dots.add(dot)
            traces.add(TracedPath(dot.get_center, stroke_color=color, stroke_width=4, dissipating_time=0))

        def spiral_path(seed):
            return ParametricFunction(
                lambda t: np.array([
                    np.exp(-0.18 * t) * (np.cos(1.2 * t) * seed[0] - np.sin(1.2 * t) * seed[1]),
                    np.exp(-0.18 * t) * (np.sin(1.2 * t) * seed[0] + np.cos(1.2 * t) * seed[1]),
                    0,
                ]),
                t_range=[0, 4.8],
                color=GRID,
                stroke_opacity=0,
            )

        caption = make_caption("Each point traces a continuous trajectory through the phase plane.")

        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(Create(plane), FadeIn(caption))
        self.add(*traces)
        self.add(*dots)
        self.play(*[MoveAlongPath(dot, spiral_path(seed)) for dot, seed in zip(dots, seeds)], run_time=paced(4.8), rate_func=linear)
        self.play(Transform(caption, make_caption("This is the geometric meaning of a phase portrait.", TEAL)))
        self.wait(paced(1.1))


class ConditioningSensitivity(Scene):
    def construct(self):
        title = make_title("Ill Conditioning Magnifies Small Changes", "Close inputs can lead to widely separated solutions.")
        left_plane = make_plane().scale(0.55).shift(LEFT * 3.3)
        right_plane = make_plane().scale(0.55).shift(RIGHT * 3.3)
        left_label = Text("data", color=INK, font_size=24).next_to(left_plane, UP, buff=0.25)
        right_label = Text("solution", color=INK, font_size=24).next_to(right_plane, UP, buff=0.25)

        p1 = left_plane.c2p(1.1, 0.55)
        p2 = left_plane.c2p(1.1, 0.8)
        q1 = right_plane.c2p(1.1, 0.55)
        q2 = right_plane.c2p(1.1, 2.1)

        d1 = Dot(p1, color=BLUE, radius=0.08)
        d2 = Dot(p2, color=PURPLE, radius=0.08)
        out1 = Dot(q1, color=BLUE, radius=0.08)
        out2 = Dot(q2, color=PURPLE, radius=0.08)
        caption = make_caption("These inputs are very close together.")

        self.play(FadeIn(title, shift=DOWN * 0.2))
        self.play(Create(left_plane), Create(right_plane), FadeIn(left_label), FadeIn(right_label), FadeIn(d1), FadeIn(d2), FadeIn(caption))
        self.play(
            TransformFromCopy(d1, out1),
            TransformFromCopy(d2, out2),
            Transform(caption, make_caption("An ill-conditioned problem can spread those tiny differences into large output changes.", RED)),
            run_time=paced(2.4),
        )
        self.wait(paced(1.1))
