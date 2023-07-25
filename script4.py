import sys   
sys.path.append('/home/ale/project/hackmeeting2023/')   
import bpy
del sys.modules['game_of_life']
import game_of_life

ON = 255
OFF = 0

def init_grease_pencil() -> bpy.types.GPencilLayer:
    sel_obj = bpy.context.selected_objects[0];
    if sel_obj is not None and sel_obj.type == 'GPENCIL':
        gpencil = sel_obj.data 
        #gp_layer = gpencil_data.layers.new("lines")
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
    #gp_frame = gp_layer.frames.new(bpy.context.scene.frame_current)
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
    #pts = [(0.0, 0.0, -square_size), (0.0, 0.0, 0.0), (-square_size, 0.0, 0), (-square_size, 0.0, -square_size)]
    #pts = [(0.0, 0.0, square_size), (0.0, 0.0, 0.0), (square_size, 0.0, 0), (square_size, 0.0, square_size)]
    #pts = [(0.0, 0.0, 0.0), (0.0, 0.0, -square_size), (square_size, 0.0, -square_size), (square_size, 0.0, 0.0)]
    x_b = (square_size + space_between_segment) * x
    z_b = (square_size + space_between_segment) * y
    pts = [(x_b, 0.0, -z_b), (x_b, 0.0, -(z_b + square_size)), (x_b + square_size, 0.0, -(z_b + square_size)), (x_b + square_size, 0.0, -z_b)]

    gp_stroke.points.add(len(pts))

    for item, value in enumerate(pts):
        gp_stroke.points[item].co = value


def draw_square(gp_frame):
    gp_stroke = gp_frame.strokes.new()
    gp_stroke.line_width = 12
    gp_stroke.start_cap_mode = 'ROUND'
    gp_stroke.end_cap_mode = 'ROUND'
    gp_stroke.use_cyclic = True

    #pts = [(0.0, 0.0, -1.0), (0.0, 0.0, 1.0), (-1.0, 0.0, -0.5), (0.5, 0.0, -0.5)]
    #pts = [(0.0, 0.0, -1.0), (0.0, 0.0, 2.0), (-1.0, 0.0, -0.5), (0.5, 0.0, -0.5)]
    # x, y, z: x and z only
    pts = [(0.0, 0.0, -1.0), (0.0, 0.0, 0.0), (-1.0, 0.0, 0), (-1.0, 0.0, -1.0)]

    gp_stroke.points.add(len(pts))

    for item, value in enumerate(pts):
        gp_stroke.points[item].co = value


def draw_matrix(grid, frame):
    for i in range(N):
        for j in range(N):
            if grid[i, j] == ON:
                draw_square_in_position(i, j, frame)
    
#gp_frame = init_frame()
#draw_square(gp_frame)
num_of_frames = 100

gp_layer = init_grease_pencil()

N = 21
grid = game_of_life.init_grid(N)

for f in range(num_of_frames):
    frame = gp_layer.frames.new(f)
    frame.clear()
    grid = game_of_life.update(grid, N)
    draw_matrix(grid, frame)

#frame = gp_layer.frames.new(1)
#for i in range(32):
#    for j in range(22):
#        draw_square_in_position(i, j, frame)

#draw_square_in_position(1,0)
#draw_square_in_position(2,0)
#draw_square_in_position(0,1)
#draw_square_in_position(1,1)
#draw_square_in_position(2,1)


#gp_stroke.points[0].pressure = 10
#gp_stroke.points[0].vertex_color = (1.0, 0.0, 0.0, 1.0)
#gp_stroke.points[-1].pressure = 10
#gp_stroke.points[-1].vertex_color = (0.0, 1.0, 0.0, 1.0)

#print(game_of_life.greet("Alice"))