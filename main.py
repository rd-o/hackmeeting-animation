import sys

sys.path.append('/home/ale/project/hackmeeting2023/hackmeeting-animation')
import bpy

# del sys.modules['game_of_life']
import game_of_life

ON = 255
OFF = 0


def init_grease_pencil() -> bpy.types.GPencilLayer:
    sel_obj = bpy.context.selected_objects[0];
    if sel_obj is not None and sel_obj.type == 'GPENCIL':
        gpencil = sel_obj.data
        # gp_layer = gpencil_data.layers.new("lines")
        gp_layer = gpencil.layers.active
        mat = bpy.data.materials.new(name="Black")
        bpy.data.materials.create_gpencil_data(mat)
        gpencil.materials.append(mat)
        mat.grease_pencil.show_fill = True
        mat.grease_pencil.fill_color = (0.0, 0.0, 0.0, 1.0)
        mat.grease_pencil.color = (0.0, 0.0, 0.0, 1.0)
    else:
        print('Select GPencil object')

    return gp_layer


def init_frame():
    gp_layer = init_grease_pencil()
    # gp_frame = gp_layer.frames.new(bpy.context.scene.frame_current)
    gp_frame = gp_layer.frames[0]

    gp_frame.clear()

    return gp_frame


def draw_square_in_position(x, y, frame):
    gp_stroke = frame.strokes.new()
    gp_stroke.line_width = 12
    gp_stroke.start_cap_mode = 'ROUND'
    gp_stroke.end_cap_mode = 'ROUND'
    gp_stroke.use_cyclic = True
    square_size = 0.1
    space_between_segment = 0.02

    # x, y, z: x and z only
    x_b = (square_size + space_between_segment) * x
    z_b = (square_size + space_between_segment) * y
    y_b = -0.02
    pts = [(x_b, y_b, -z_b),
           (x_b, y_b, -(z_b + square_size)),
           (x_b + square_size, y_b, -(z_b + square_size)),
           (x_b + square_size, y_b, -z_b)]

    gp_stroke.points.add(len(pts))

    for item, value in enumerate(pts):
        gp_stroke.points[item].co = value


def draw_square(gp_frame):
    gp_stroke = gp_frame.strokes.new()
    gp_stroke.line_width = 12
    gp_stroke.start_cap_mode = 'ROUND'
    gp_stroke.end_cap_mode = 'ROUND'
    gp_stroke.use_cyclic = True

    # x, y, z: x and z only
    pts = [(0.0, 0.0, -1.0), (0.0, 0.0, 0.0), (-1.0, 0.0, 0), (-1.0, 0.0, -1.0)]

    gp_stroke.points.add(len(pts))

    for item, value in enumerate(pts):
        gp_stroke.points[item].co = value


def draw_matrix(grid, frame, n, m):
    for i in range(n):
        for j in range(m):
            if grid[i, j] == ON:
                draw_square_in_position(i, j, frame)


num_of_frames = 100

gp_layer = init_grease_pencil()

n = 32
m = 22
grid = game_of_life.init_grid(n)

for f in range(num_of_frames):
    frame = gp_layer.frames.new(f + 1)
    frame.clear()
    draw_matrix(grid, frame, n, m)
    grid = game_of_life.update(grid, n, m)

