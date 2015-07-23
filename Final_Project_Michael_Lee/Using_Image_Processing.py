from PIL import Image
import os, sys
import pprint
import time
import multiprocessing

def crop_reduce_and_invert_vertically(
	image, start, end, number_of_boxes_in_Y, 
	width, height, flip=False
	):
	pixel_corner_locations = []
	regions = []
	for i in range(start, end):
		for j in range(0, number_of_boxes_in_Y):
			"""
			Generally, we want even mapping so we want to keep the box sizes equal. 
			Use 160 partitions for maximum effect (8 x 5 boxes).
			"""
			box = ((width*i), (height*j), (width*(i+1)), (height*(j+1)))
			if flip:
				image_crop_flipped = image.crop(box).transpose(Image.FLIP_TOP_BOTTOM)
				regions.append(image_crop_flipped)
			else:
				image_crop = image.crop(box)
				regions.append(image_crop)
			pixel_corner_locations.append(box)
	return regions, pixel_corner_locations

def unpack_into_bits(image, width, height):
	bit_sequence = [image[i].getpixel((j,k)) for i in range(len(image)) 
	for j in range(width) for k in range(height)]
	return bit_sequence

if __name__ == '__main__':
	
	im = Image.open("water_1280.bmp")
	pix = im.load()
	# The picture needs to be inverted on one half in order to make correct comparisons
	# with the antinode pair.
	inverted_picture = crop_reduce_and_invert_vertically(im, 0, 1, 1, 640, 800, True)[0][0]

	begin_time1 = time.time()
	box_width = 8
	box_height = 10

	# splits into 640 squares on the left hemisphere
	west_hemi, w_locations = crop_reduce_and_invert_vertically(inverted_picture, 
		0, 80, 80, box_width, box_height)
	# splits into 640 squares on the right hemisphere
	east_hemi, e_locations = crop_reduce_and_invert_vertically(im, 80, 160, 80, 
		box_width, box_height)

	west_unpacked = unpack_into_bits(west_hemi, box_width, box_height)
	east_unpacked = unpack_into_bits(east_hemi, box_width, box_height)
	compared_sequences = map(lambda x,y: x+y, west_unpacked, east_unpacked)

	# count(2) for land-land, count(1) for land-water, count(0) for water-water
	probability_of_water = compared_sequences.count(0)/float(len(compared_sequences))

	print "The probability of hitting water on both sides is %f" % probability_of_water
	print "%s seconds\n" % (time.time() - begin_time1)