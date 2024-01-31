# Takes a spritesheet as input and slices it into individual frames
# and stitches the frames into a gif
#
# Usage: python GifMaker.py <path to spritesheet> <path to output gif>
#
# Example: python GifMaker.py ./spritesheet.png ./output.gif
#
# Dependencies: Pillow
#
from sys import argv
from PIL import Image
# operation = 1
# while operation != 0:
print("Operations:")
print("1. Slice spritesheet")
print("2. Flip gif")
print("3. Split gif to subgifs")
print("4. Erase frames from end of gif")
operation = int(input("Operation: "))
if operation == 1:
    # Gif framerate
    fps = 10
    # Read the spritesheet from the first argument
    spritesheet = Image.open(argv[1])
    # The width of the spritesheet
    spritesheet_width = spritesheet.width
    # The height of the spritesheet
    spritesheet_height = spritesheet.height
    # The number of frames per row in the spritesheet read from command line
    frames_per_row = int(input("Frames per row: "))
    # The number of frames per column in the spritesheet
    frames_per_column = int(input("Frames per column: "))
    # The size of each frame in the spritesheet
    frame_width = spritesheet_width // frames_per_row
    frame_height = spritesheet_height // frames_per_column
    # The index of the current frame
    frame_index = 0
    # Iterate over the rows of frames in the spritesheet
    for row in range(frames_per_column):
        frames = []

        # Iterate over the columns of frames in the spritesheet
        for column in range(frames_per_row):
            # The x coordinate of the current frame in the spritesheet
            x = (column * (frame_width))
            # The y coordinate of the current frame in the spritesheet
            y = (row * (frame_height))
            # Print the coordinates of the current frame
            print(f"({x}, {y})")
            # The bounding box of the current frame in the spritesheet
            bounding_box = (x, y, x + frame_width, y + frame_height)
            # Crop the current frame from the spritesheet
            frame = spritesheet.crop(bounding_box)
            # Add the current frame to the list of frames
            frames.append(frame)
        # Print the index of the current frame
        print(f"Row {row}")
        gif = Image.new("RGBA", (frame_width, frame_height))
        frames[0].save(argv[2] + str(row) + ".gif", append_images=frames[1:], save_all=True, duration=1000 // fps, loop=0, optimize=False, disposal=2)

elif operation == 2:
    # Read the gif from the first argument
    gif = Image.open(argv[1])
    flipped_frames = []
    # Iterate over the frames in the gif
    for frame_index in range(gif.n_frames):
        # Go to the current frame
        gif.seek(frame_index)
        # Flip the current frame
        flipped_frame = gif.transpose(Image.FLIP_LEFT_RIGHT)
        # Add the flipped frame to the list of flipped frames
        flipped_frames.append(flipped_frame)
        print(f"Flipped frame {frame_index}")
    # Clear gif
    gif = Image.new("RGBA", (gif.width, gif.height)) 
    # Save the flipped frame to the gif
    flipped_frames[0].save(argv[2] + ".gif", append_images=flipped_frames[1:], save_all=True, duration=1000 // 10, loop=0, optimize=False, disposal=2)
elif operation == 3:
    number_of_subgifs = int(input("Number of subgifs: "))
    # Read the gif from the first argument
    gif = Image.open(argv[1])
    # The width of the gif
    gif_width = gif.width
    # The height of the gif
    gif_height = gif.height
    # The number of frames in the gif
    number_of_frames = gif.n_frames
    number_of_frames_per_subgif = number_of_frames // number_of_subgifs
    # Split the gif into subgifs
    for subgif_index in range(number_of_subgifs):
        subgif = Image.new("RGBA", (gif_width, gif_height))
        frames = []
        for frame_index in range(number_of_frames_per_subgif):
            gif.seek(frame_index + (subgif_index * number_of_frames_per_subgif))
            frame = gif.copy()
            frames.append(frame)
        frames[0].save(argv[2] + str(subgif_index) + ".gif", append_images=frames[1:], save_all=True, duration=1000 // 10, loop=0, optimize=False, disposal=2)
elif operation == 4:
    # Read the gif from the first argument
    gif = Image.open(argv[1])
    # The number of frames in the gif
    number_of_frames = gif.n_frames
    # Print the number of frames in the gif
    print(f"Number of frames: {number_of_frames}")
    # The number of frames to erase
    number_of_frames_to_erase = int(input("Number of frames to erase: "))
    # The number of frames in the gif after erasing
    number_of_frames_after_erasing = number_of_frames - number_of_frames_to_erase
    # The width of the gif
    gif_width = gif.width
    # The height of the gif
    gif_height = gif.height
    # The frames to keep
    frames = []
    # Iterate over the frames in the gif
    for frame_index in range(number_of_frames_after_erasing):
        # Go to the current frame
        gif.seek(frame_index)
        # Add the current frame to the list of frames
        frames.append(gif.copy())
        print(f"Kept frame {frame_index}")
    # Clear gif
    gif = Image.new("RGBA", (gif_width, gif_height)) 
    # Save the kept frames to the gif
    # gif.save(argv[2], append_images=frames, save_all=True, duration=1000 // 10, loop=0, optimize=False, disposal=2)
    frames[0].save(argv[2], append_images=frames[1:], save_all=True, duration=1000 // 10, loop=0, optimize=False, disposal=2)
    
