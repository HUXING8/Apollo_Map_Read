import output.map_pb2
from google.protobuf import text_format
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def get_pb_from_text_file(filename, pb_value):
    """Get a proto from given text file."""
    with open(filename, 'r') as file_in:
        return text_format.Merge(file_in.read(), pb_value)


def draw_lane_boundary(lane, ax, color_val):
    for curve in lane.left_boundary.curve.segment:
        if curve.HasField('line_segment'):
            px = []
            py = []
        for p in curve.line_segment.point:
            px.append(float(p.x))
            py.append(float(p.y))
        ax.plot(px, py, ls='-', c=color_val, alpha=0.5, picker=True)
    for curve in lane.right_boundary.curve.segment:
        if curve.HasField('line_segment'):
            px = []
            py = []
            for p in curve.line_segment.point:
                px.append(float(p.x))
                py.append(float(p.y))
            ax.plot(px, py, ls='-', c=color_val, alpha=0.5, picker=True)


def draw_lane_central(lane, ax, color_val, alpha_val = 0.5):
    for curve in lane.central_curve.segment:
        if curve.HasField('line_segment'):
            px = []
            py = []
        for p in curve.line_segment.point:
            px.append(float(p.x))
            py.append(float(p.y))
        line2d, = ax.plot(px, py, ls='-', linewidth=5, c=color_val, alpha=alpha_val, picker=True)

def draw_polygon_boundary(polygon, ax, color_val):
    px = []
    py = []
    for point in polygon.point:
      px.append(point.x)
      py.append(point.y)

    if px:
      px.append(px[0])
      py.append(py[0])

    ax.plot(px, py, ls='-', linewidth=2, c=color_val, alpha=0.5, picker=True)

def draw_stop_line(line_segment, ax, color_val):
    px = []
    py = []
    for p in line_segment.point:
      px.append(float(p.x))
      py.append(float(p.y))
    ax.plot(px, py, 'o-', linewidth=1, c=color_val, picker=True)

def draw_polygon(polygon, ax, color_val):
    pxy = []
    for point in polygon.point:
      pxy.append([point.x, point.y])
    polygon = patches.Polygon(pxy, True)
    ax.add_patch(polygon)

if __name__ == "__main__":
    map_pb = output.map_pb2.Map()
    res = get_pb_from_text_file("apollo_map.txt",map_pb)

    fig,ax = plt.subplots()

    # customize your interested data
    for i,lane in enumerate(res.lane):
        draw_lane_central(lane, ax, 'red', alpha_val = 0.5)
        draw_lane_boundary(lane, ax, 'green')

    for junction in res.junction:
        draw_polygon_boundary(junction.polygon, ax, 'c')

    for signal in res.signal:
        for stop_line in signal.stop_line:
            for curve in stop_line.segment:
                draw_stop_line(curve.line_segment, ax, "tomato")

    for crosswalk in res.crosswalk:
        draw_polygon(crosswalk.polygon, ax, 'c')

    for stop_sign in res.stop_sign:
      for stop_line in stop_sign.stop_line:
        for curve in stop_line.segment:
            draw_stop_line(curve.line_segment, ax, "tomato")
    
    plt.show()
    # plt.savefig("map_img.png",dpi=200)

