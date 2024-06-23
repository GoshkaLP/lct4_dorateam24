class ColorsUtility:
    def rgb_to_hex(self, rgb):
        return "#{:02x}{:02x}{:02x}".format(*rgb)

    def hex_to_rgb(self, hex_color):
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))

    def interpolate_color(self, color_start, color_end, factor):
        rgb_start = self.hex_to_rgb(color_start)
        rgb_end = self.hex_to_rgb(color_end)
        rgb_interpolated = (
            round(rgb_start[0] + (rgb_end[0] - rgb_start[0]) * factor),
            round(rgb_start[1] + (rgb_end[1] - rgb_start[1]) * factor),
            round(rgb_start[2] + (rgb_end[2] - rgb_start[2]) * factor),
        )
        return self.rgb_to_hex(rgb_interpolated)
