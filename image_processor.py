# import Image
from PIL import Image


class Colors(object):
	class Color(object):
		def __init__(self, value):
			self.value = value

		def __str__(self):
			return "%s : %s" % (self.__class__.__name__, self.value)

	class Red(Color): pass
	class Blue(Color): pass
	class Green(Color): pass
	class Yellow(Color): pass
	class White(Color): pass
	class Gray(Color): pass
	class Black(Color): pass
	class Pink(Color): pass
	class Teal(Color): pass

class ColorWheel(object):
	def __init__(self, rgb):
		r, g, b = rgb

		self.rgb = (Colors.Red(r), Colors.Green(g), Colors.Blue(b), )
	
	def estimate_color(self):
		dominant_colors = self.get_dominant_colors()

		total_colors = len(dominant_colors)
		
		if total_colors == 1:
			return dominant_colors[0]
		elif total_colors == 2:
			color_classes = [x.__class__ for x in dominant_colors]

			if Colors.Red in color_classes and Colors.Green in color_classes:
				return Colors.Yellow(dominant_colors[0].value)
			elif Colors.Red in color_classes and Colors.Blue in color_classes:
				return Colors.Pink(dominant_colors[0].value)
			elif Colors.Blue in color_classes and Colors.Green in color_classes:
				return Colors.Teal(dominant_colors[0].value)
		elif total_colors == 3:
			if dominant_colors[0].value > 200:
				return Colors.White(dominant_colors[0].value)
			elif dominant_colors[0].value > 100:
				return Colors.Gray(dominant_colors[0].value)
			else:
				return Colors.Black(dominant_colors[0].value)
		else:
			print("Dominant Colors : %s" % dominant_colors)
	
	def get_dominant_colors(self):
		max_color = max([x.value for x in self.rgb])

		return [x for x in self.rgb if x.value >= max_color * .9]

def process_image(image):
	image_color_quantities = {}

	width, height = image.size

	# for x in range(width):
		# for y in range(height):

	width_margin = int(width - (width * .65))
	height_margin = int(height - (height * .65))
	# print height
	# print range(height_margin, height - height_margin)
	for x in range(width_margin, width - width_margin):
		for y in range(height_margin, height - height_margin):
			r, g, b = image.getpixel((x, y))

			key = "%s:%s:%s" % (r, g, b, )

			key = (r, g, b, )

			image_color_quantities[key] = image_color_quantities.get(key, 0) + 1

	total_assessed_pixels = sum([v for k, v in image_color_quantities.items() if v > 10])

	# strongest_color_wheels = [(ColorWheel(k), v / float(total_pixels) * 100, ) for k, v in test.items() if v > 30]
	strongest_color_wheels = [(ColorWheel(k), v / float(total_assessed_pixels) * 100, ) for k, v in image_color_quantities.items() if v > 10]

	final_colors = {}

	for color_wheel, strength in strongest_color_wheels:
		# print "%s => %s" % (strength, [str(x) for x in color_wheel.get_dominant_colors()], )

		# print "%s => %s" % (strength, color_wheel.estimate_color(), )

		color = color_wheel.estimate_color()

		final_colors[color.__class__] = final_colors.get(color.__class__, 0) + strength

	for color, strength in final_colors.items():
		print("%s - %s" % (color.__name__, strength, ))

	image.show()

if __name__ == '__main__':
	image = Image.open("./5Lc5U45J83M53J53Hcc1e9614e8836ffd1910.jpg")

	process_image(image)
